#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import os
import npyscreen
import MySQLdb
from Crypto.Cipher import AES
from web import settings
import base64
import hashlib
import base58
import libnacl.public
import libnacl.secret
import datetime
import uuid
import gzip
import netifaces
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.core import mail
from django.db import transaction
from subprocess import call

XID_PREFIX = b'\x5f'
KEY_PREFIX = b'\xba'
SECRET_PREFIX = b'\xff'


def crypt(data):
    block_size = 32
    padding = '{'
    pad = lambda s: s + (block_size - len(s) % block_size) * padding
    encode_aes = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    cipher = AES.new(settings.SECRET_KEY[:32])
    encoded = encode_aes(cipher, str(data))
    return encoded


def decrypt(crypt_data):
    padding = '{'
    decode_aes = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(padding)
    cipher = AES.new(settings.SECRET_KEY[:32])
    decoded = decode_aes(cipher, str(crypt_data))
    return decoded


def generate_keypair(sk=None):
    if sk:
        keypair = libnacl.public.SecretKey(sk=sk)
    else:
        keypair = libnacl.public.SecretKey()

    return keypair.pk, keypair.sk


def string_to_secret(sk_str):
    val = base58.b58decode(sk_str)

    if len(val) != 35:
        return None

    prefix = val[0]
    if prefix != SECRET_PREFIX:
        return None

    key = val[1:33]
    sha256 = hashlib.sha256()
    sha256.update(SECRET_PREFIX)
    sha256.update(key)
    s = sha256.digest()

    if val[-2:] != s[:2]:
        return None

    return key


def string_to_key(pk_str):
    val = base58.b58decode(pk_str)

    if len(val) != 35:
        return None

    prefix = val[0]
    if prefix != KEY_PREFIX:
        return None

    key = val[1:33]
    sha256 = hashlib.sha256()
    sha256.update(KEY_PREFIX)
    sha256.update(key)
    s = sha256.digest()

    if val[-2:] != s[:2]:
        return None

    return key


def validate(key, secret):
    if key and secret:
        sk = string_to_secret(secret)
        pk = string_to_key(key)
        (vpk, vsk) = generate_keypair(sk=sk)
        if vpk == pk and vsk == sk:
            return 0
        return 1


def secret_to_string(key):
    sha256 = hashlib.sha256()
    sha256.update(SECRET_PREFIX)
    sha256.update(key)
    sum = sha256.digest()
    result = SECRET_PREFIX + key + sum[:2]

    return base58.b58encode(result)


def key_to_string(key):
    sha256 = hashlib.sha256()
    sha256.update(KEY_PREFIX)
    sha256.update(key)
    sum = sha256.digest()
    result = KEY_PREFIX + key + sum[:2]

    return base58.b58encode(result)

db = MySQLdb.connect(settings.DATABASES.values()[0]['HOST'],
                     settings.DATABASES.values()[0]['USER'],
                     settings.DATABASES.values()[0]['PASSWORD'],
                     settings.DATABASES.values()[0]['NAME'])
cursor = db.cursor()


class AronSupport(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())


class MainForm(npyscreen.FormWithMenus):
    def create(self):
        info = "Benvenuto nel supporto \"ARON PROXY\".\nPer utilizzare questa tool, esegua il tasto \"Control+X\" per accedere al Menu Principale."
        npyscreen.notify_confirm(info)
        self.menu = self.add_menu(name="Accesso Menu", shortcut="^X")
        self.menu.addItemsFromList([
            ("1- Impostazione Attuale", self.info),
            ("2- Impostazione Rete",   self.network),
            ("3- Reset account existente", self.pwd_reset),
            ("4- Ripristina Aron Proxy", self.restore),
            ("5- Assistenza Remota", self.remote_session),
            ("6- Esci dalla console", self.exit_application),
        ])

    def info(self):
        try:
            sql_ctx = 'SELECT * from aron.License_license LIMIT 1;'
            cursor.execute(sql_ctx)
            r_db = cursor.fetchall()

            txt = "Nome cliente: %s\n" % r_db[0][1]
            txt += "Nominativo: %s\n" % r_db[0][2]
            txt += "Provincia: %s\n" % r_db[0][3]
            active = validate(decrypt(r_db[0][4]), decrypt(r_db[0][5]))
            today = datetime.datetime.today()
            if active is 0 \
                    and datetime.date(int(decrypt(r_db[0][6])[:4]), int(decrypt(r_db[0][6])[6:7]), int(decrypt(r_db[0][6])[9:10])) \
                            > datetime.date(today.year, today.month, today.day):
                active = 'Attiva\n'
            else:
                active = 'Inattiva\n'
            txt += "Licenza: %s\n" % active
            txt += "Scadenza: %s\n" % decrypt(r_db[0][6])
            if decrypt(r_db[0][7]) is 0:
                txt += "Numero dispositivi massimo: Illimitati\n"
            else:
                txt += "Numero dispositivi massimo: %s\n" % decrypt(r_db[0][7])
        except:
            txt = "Licenza: - NON ATTIVA -"
        npyscreen.notify_confirm(txt)

    def network(self):
        dev_eth = []
        for dev in range(1, 5):
            dev_eth.append(netifaces.interfaces()[dev])
        net = npyscreen.Form(name="Impostazione Rete per Default, Selezione il modo delle interfaccie", lines=0, columns=0, minimum_lines=24, minimum_columns=80)
        iface0 = net.add(npyscreen.TitleSelectOne, max_height=4, name="Rete WAN:",
                         values=dev_eth, scroll_exit=True)
        iface1 = net.add(npyscreen.TitleSelectOne, max_height=4, name="Rete LAN1:",
                         values=dev_eth, scroll_exit=True)
        net.edit()
        try:
            config = open('/etc/network/interfaces', 'w')
            config.write(str('auto lo %s %s\n'
                             'iface lo inet loopback\n'
                             'iface %s inet dhcp\n'
                             'iface %s inet static\n'
                             '    address 192.168.50.1\n'
                             '    network 255.255.255.0\n\n') %
                         (str(iface0.get_selected_objects()[0]), str(iface1.get_selected_objects()[0]),
                          str(iface0.get_selected_objects()[0]), str(iface1.get_selected_objects()[0]))
            )
            config.close()
            call(["sudo", "/etc/init.d/networking", "stop"])
            call(["sudo", "/etc/init.d/networking", "start"])
            config = open('/etc/dhcp/dhcpd.conf', 'w')
            config.write(str('ddns-update-style none;\n'
                             'authoritative;\n'
                             'option domain-name "aron.proxy.local";\n'
                             'option domain-name-servers 8.8.8.8, 8.8.4.4;\n'
                             'default-lease-time 28800;\n'
                             'max-lease-time 28800;\n'
                             'log-facility local7;\n\n'
                             'subnet 192.168.50.0 netmask 255.255.255.0 {\n'
                             '  interface %s;\n'
                             '  range 192.168.50.10 192.168.50.254;\n'
                             '  option routers 192.168.50.1;\n'
                             '}\n') %
                         (str(iface1.get_selected_objects()[0])))
            config.close()
            call(["sudo", "/etc/init.d/isc-dhcp-server", "restart"])
            npyscreen.notify_confirm("Impostazione Rete riuscita.")
        except:
            npyscreen.notify_confirm("Impostazione Rete non riuscita.")

    def pwd_reset(self):
        reset_form = npyscreen.Form(name="Reset Password", lines=0, columns=0, minimum_lines=24, minimum_columns=80)
        user_list = []
        check_user = "SELECT username FROM aron.auth_user;"
        cursor.execute(check_user)
        exist = cursor.fetchall()
        for line in range(0, len(exist)):
            user_list.append(exist[line][0])
        select = reset_form.add(npyscreen.TitleSelectOne, max_height=4, name="Utente:",
                         values=user_list, scroll_exit=True)
        password = reset_form.add(npyscreen.TitlePassword, name="Password:")
        password_confirm = reset_form.add(npyscreen.TitlePassword, name="Conferma:")
        pwd = PBKDF2PasswordHasher()
        reset_form.edit()
        if password.get_value() == password_confirm.get_value() and password.get_value() != '':
            sql_ctx = "UPDATE aron.auth_user SET password=\"%s\" WHERE username=\"%s\";" % \
                      (str(pwd.encode(password.get_value(), str(uuid.uuid4()), 12)),
                       str(select.get_selected_objects())[2:-2])
            cursor.execute(sql_ctx)
            db.commit()
            npyscreen.notify_confirm("La password per l'utente %s e' stata cambiata." %
                                     str(select.get_selected_objects())[1:-1])
        else:
            npyscreen.notify_confirm("La password NON sono uguale. Controllare di nuovo")

    def remote_session(self):
        sql_ctx = 'SELECT * from aron.License_license LIMIT 1;'
        cursor.execute(sql_ctx)
        r_db = cursor.fetchall()
        try:
            active = validate(decrypt(r_db[0][4]), decrypt(r_db[0][5]))
            if active is 0:
                pwd = settings.DATABASES.values()[0]['PASSWORD']
                os.system("echo root:%s | sudo chpasswd" % pwd)
                pwd_support = decrypt('ASA3R74rBh1JXn9ZtuoqP65HKl7UB7q+yofylSaOkVA=')
                try:
                    os.system(
                        "sshpass -p \"%s\" ssh -o \"StrictHostKeyChecking no\" -N -f -R 8022:localhost:22 support@domain.tld" % pwd_support)
                    ctx = 'Attiva sessione remota per il cliente: %s, la password per accedere: %s' % (str(r_db[0][0]), str(pwd))
                    mail.send_mail('Richiesta assistenza Remota Aron Proxy.', ctx,
                                   settings.DEFAULT_FROM_EMAIL, ['user@domain.tld'], fail_silently=True)
                    npyscreen.notify_confirm("Aperta sessione con l'assistenza remota. E' stata inviata una mail con la richiesta.")
                except:
                    npyscreen.notify_confirm("Sessione Remota non 'e stato riaggiungibile.")
        except:
            npyscreen.notify_confirm("La sessione remota non puo' essere attiva finche' non sia attiva la Licenza.")

    def restore(self):
        try:
            if os.path.isfile(str(settings.STATICFILES_DIRS[0] + '/' + 'config.aron.factory.prx')):
                load_f = gzip.open(str(settings.STATICFILES_DIRS[0] + '/' + 'config.aron.factory.prx'), 'rb')
                ctx = decrypt(load_f.read())
                with transaction.atomic():
                    cursor.execute(ctx)
                load_f.close()
                mac_file = open(settings.FIREHOL_DIR + 'mac_allow', 'w')
                sql_ctx = 'SELECT mac from aron.Network_management;'
                _db = MySQLdb.connect(settings.DATABASES.values()[0]['HOST'],
                                      settings.DATABASES.values()[0]['USER'],
                                      settings.DATABASES.values()[0]['PASSWORD'],
                                      settings.DATABASES.values()[0]['NAME'])
                cur = _db.cursor()
                cur.execute(sql_ctx)
                manager = cur.fetchall()
                mac_file.write(str(manager[0][0] + '\n'))
                mac_file.close()
                call(["sudo", "firehol", "restart"])
                proxy_conf = open(settings.SQUID_CONF, 'w')
                squid_conf = 'http_port 3128 intercept\n' \
                             'acl localnet src 192.168.0.0/16 172.16.0.0/12 10.0.0.0/8\n' \
                             'acl localnet src fc00::/7\n' \
                             'acl localnet src fe80::/10\n' \
                             'acl SSL_ports port 443\n' \
                             'acl Safe_ports port 80\n' \
                             'acl Safe_ports port 21\n' \
                             'acl Safe_ports port 443\n' \
                             'acl Safe_ports port 70\n' \
                             'acl Safe_ports port 210\n' \
                             'acl Safe_ports port 1025-65535\n' \
                             'acl Safe_ports port 280\n' \
                             'acl Safe_ports port 488\n' \
                             'acl Safe_ports port 591\n' \
                             'acl Safe_ports port 777\n' \
                             'acl CONNECT method CONNECT\n' \
                             'http_access allow localnet\n' \
                             'http_access deny all\n' \
                             'negative_ttl 5 minutes\n' \
                             'positive_dns_ttl 15 hours\n' \
                             'negative_dns_ttl 1 minutes\n' \
                             'shutdown_lifetime 1\n' \
                             'cache_mgr no-reply@aron.proxy.it\n' \
                             'visible_hostname Aron-Proxy\n' \
                             'dns_nameservers 8.8.8.8 8.8.4.4\n' \
                             'access_log none\n'
                proxy_conf.write(squid_conf)
                proxy_conf.close()
                call(["sudo", "/etc/init.d/squid", "restart"])
                call(["sudo", "/etc/init.d/apache2", "restart"])
                call(["sudo", "chmod", "666", "/etc/squid/squid.conf"])
                npyscreen.notify_confirm("Ripristino di configurazione per default.")
            else:
                npyscreen.notify_confirm("Il file non essiste perche ancora non e' stata attivata la licenza.")
        except:
            npyscreen.notify_confirm("E' stato riscontrato un errore nella importazione del file.")

    def exit_application(self):
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()


def main():
    console = AronSupport()
    console.run()


if __name__ == '__main__':
    main()
