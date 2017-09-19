from web import settings
import os
from models import Blacklist
from License import bf
from Routing.models import Routing


def update_squid(https=False):
    os.system("sudo chmod 666 /etc/squid/squid.conf")
    proxy_conf = open(settings.SQUID_CONF, 'w')
    squid_conf = '''http_port 127.0.0.1:8080
http_port 3128 intercept

cache_mem 512 MB
cache_dir aufs /var/cache/squid 460800 256 128
maximum_object_size_in_memory 32 KB
memory_cache_mode disk
store_dir_select_algorithm least-load
minimum_object_size 0 bytes
maximum_object_size 5120 MB
cache_swap_low 96
cache_swap_high 98
memory_replacement_policy heap LRU
cache_replacement_policy heap LFUDA
coredump_dir /var/cache/squid
memory_pools off
range_offset_limit 5120 MB
quick_abort_min -1
range_offset_limit -1

acl CONNECT method CONNECT
acl PURGE method PURGE
acl GET method GET
acl FTP proto FTP
acl localnet src 192.168.0.0/16 172.16.0.0/12 10.0.0.0/8
acl mac_allows arp "/etc/firehol/mac_allow"
acl SSL_ports port 443
acl Safe_ports port 80
acl Safe_ports port 21
acl Safe_ports port 443
acl Safe_ports port 70
acl Safe_ports port 210
acl Safe_ports port 1025-65535
acl Safe_ports port 280
acl Safe_ports port 488
acl Safe_ports port 591
acl Safe_ports port 777
acl aron_server dst "/etc/squid/aron_server"
acl windowsupdate dstdomain sls.update.microsoft.com.akadns.net
acl windowsupdate dstdomain windowsupdate.microsoft.com
acl windowsupdate dstdomain .update.microsoft.com
acl windowsupdate dstdomain download.windowsupdate.com
acl windowsupdate dstdomain redir.metaservices.microsoft.com
acl windowsupdate dstdomain images.metaservices.microsoft.com
acl windowsupdate dstdomain c.microsoft.com
acl windowsupdate dstdomain www.download.windowsupdate.com
acl windowsupdate dstdomain wustat.windows.com
acl windowsupdate dstdomain crl.microsoft.com
acl windowsupdate dstdomain sls.microsoft.com
acl windowsupdate dstdomain productactivation.one.microsoft.com
acl windowsupdate dstdomain ntservicepack.microsoft.com
acl wuCONNECT dstdomain www.update.microsoft.com
acl wuCONNECT dstdomain sls.microsoft.com

http_access deny !Safe_ports
http_access deny CONNECT !SSL_ports
http_access allow localhost manager
http_access deny manager
http_access allow PURGE localhost
http_access deny PURGE
http_access allow FTP
http_access allow CONNECT wuCONNECT localnet
http_access allow CONNECT wuCONNECT localhost
http_access allow windowsupdate localnet
http_access allow windowsupdate localhost

client_dst_passthru on\n'''
    proxy_conf.write(squid_conf)
    if https is True:
        squid_conf = '''https_port 3129 intercept ssl-bump generate-host-certificates=on dynamic_cert_mem_cache_size=16MB cert=/etc/squid/aron-proxy.pem
sslproxy_cert_error allow all
acl DiscoverSNIHost at_step SslBump1
ssl_bump peek DiscoverSNIHost
ssl_unclean_shutdown on
sslproxy_version 1
sslproxy_options NO_SSLv3,SINGLE_DH_USE
sslproxy_flags DONT_VERIFY_PEER
sslproxy_cipher EECDH+ECDSA+AESGCM:EECDH+aRSA+AESGCM:EECDH+ECDSA+SHA384:EECDH+ECDSA+SHA256:EECDH+aRSA+SHA384:EECDH+aRSA+SHA256:EECDH+aRSA+RC4:EECDH:EDH+aRSA:HIGH:!RC4:!aNULL:!eNULL:!LOW:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS
ssl_bump server-first all
sslcrtd_program /usr/lib/squid/ssl_crtd -s /var/lib/ssl_db -M 16MB sslcrtd_children 10 startup=1 idle=1\n'''
        proxy_conf.write(squid_conf)
    squid_conf = '''
negative_ttl 5 minutes
positive_dns_ttl 15 hours
negative_dns_ttl 1 minutes

store_id_program /usr/lib/squid/storeid_file_rewrite /etc/squid/url_patterns
store_id_children 50 startup=45 idle=5 concurrency=10
store_id_access deny all
store_id_bypass off

refresh_pattern ^http://wupdate.squid.internal/.* 1814400 100% 1814400 override-expire override-lastmod ignore-reload ignore-no-store ignore-must-revalidate ignore-private ignore-auth
refresh_pattern ^http://apple.aron.squid.internal/.* 43200 100% 10080 override-expire override-lastmod ignore-reload ignore-no-store ignore-must-revalidate ignore-private ignore-auth
refresh_pattern ^http://android.aron.squid.internal/.* 43200 100% 10080 override-expire override-lastmod ignore-reload ignore-no-store ignore-must-revalidate ignore-private ignore-auth
refresh_pattern ^http://yt.aron.squid.internal/.* 43200 100% 10080 override-expire override-lastmod ignore-reload ignore-no-store ignore-must-revalidate ignore-private ignore-auth
refresh_pattern ^http://speedtest.aron.squid.internal/.* 43200 100% 10080 override-expire override-lastmod ignore-reload ignore-no-store ignore-must-revalidate ignore-private ignore-auth
refresh_pattern ^http://audio.aron.squid.internal/.* 43200 20% 10080 override-expire override-lastmod ignore-reload ignore-no-store ignore-must-revalidate ignore-private ignore-auth
refresh_pattern ^http://video.aron.squid.internal/.* 43200 20% 10080 override-expire override-lastmod ignore-reload ignore-no-store ignore-must-revalidate ignore-private ignore-auth
refresh_pattern ^http://files.aron.squid.internal/.* 43200 20% 10080 override-expire override-lastmod ignore-reload ignore-no-store ignore-must-revalidate ignore-private ignore-auth
refresh_pattern ^http://windows-dll.aron.squid.internal/.* 43200 20% 10080 override-expire override-lastmod ignore-reload ignore-no-store ignore-must-revalidate ignore-private ignore-auth
refresh_pattern ^http://blogs.aron.squid.internal/.* 1440 20% 14400 override-expire override-lastmod ignore-reload ignore-no-store ignore-must-revalidate ignore-private ignore-auth
refresh_pattern ^http://office.aron.squid.internal/.* 1440 20% 14400 override-expire override-lastmod ignore-reload ignore-no-store ignore-must-revalidate ignore-private ignore-auth
refresh_pattern ^http://images.aron.squid.internal/.* 1440 20% 14400 override-expire override-lastmod ignore-reload ignore-no-store ignore-must-revalidate ignore-private ignore-auth
refresh_pattern ^http://av-data.aron.squid.internal/.* 10800 80% 10800 override-expire override-lastmod ignore-reload ignore-no-store ignore-must-revalidate ignore-private ignore-auth
refresh_pattern ^http://av-upd.aron.squid.internal/.* 0 20% 1440 override-expire override-lastmod ignore-reload ignore-no-store ignore-must-revalidate ignore-private ignore-auth
refresh_pattern ^http://fb.aron.squid.internal/.* 0 20% 1440
refresh_pattern -i .*(begin|start)\=[1-9][0-9].* 0 0% 0
refresh_pattern -i (cgi-bin|mrtg|graph) 0 0% 0
refresh_pattern -i \.(lst|ui|ini|list)$ 0 0% 0
refresh_pattern -i .(htm?l|css|js)$ 1440 40% 40320
refresh_pattern ^ftp:             1440    20%     10080
refresh_pattern ^gopher:  1440    0%      1440
refresh_pattern -i (/cgi-bin/|\?) 0       0%      0
refresh_pattern .         0       20%     4320

reload_into_ims on

cache_effective_user proxy
cache_effective_group proxy\n'''
    proxy_conf.write(squid_conf)
    if Blacklist.objects.count() > 0:
        bl_file = open('/etc/squid/black_domain', 'w')
        for item in range(0, Blacklist.objects.count()):
            bl_file.write(Blacklist.objects.values()[item]['domain'] + '\n')
        bl_file.close()
        squid_conf = 'acl bl_domain dstdomain "/etc/squid/black_domain"\n'
        squid_conf += 'http_access deny bl_domain\n'
        proxy_conf.write(squid_conf)
    if not str(Routing.objects.values()[0]['mode']) == 'Routing':
        squid_conf = "http_access allow localnet"
    if not str(Routing.objects.values()[0]['mode']) == 'Proxy/Classes':
        squid_conf = "http_access allow mac_allows"
    proxy_conf.write(squid_conf)
    squid_conf = '''
http_access deny all !aron_server

client_persistent_connections off
server_persistent_connections on
follow_x_forwarded_for allow all\n'''
    proxy_conf.write(squid_conf)
    squid_conf = 'access_log daemon:/' + settings.DATABASES.values()[0]['HOST'] + '/' + settings.DATABASES.values()[0]['NAME'] + '/' + \
        'aron_logs/' + settings.DATABASES.values()[0]['USER'] + '/' + \
        settings.DATABASES.values()[0]['PASSWORD'] + ' squid\n'
    proxy_conf.write(squid_conf)
    squid_conf = '''
logfile_daemon /usr/lib/squid/log_db_daemon
forwarded_for on
shutdown_lifetime 1
cache_mgr no-reply@aron.proxy.it
visible_hostname Aron-Proxy
dns_nameservers 8.8.8.8 8.8.4.4
via on

qos_flows tos local-hit=0x30
digest_generation off
request_header_access Surrogate-Capability deny all'''
    proxy_conf.write(squid_conf)
    proxy_conf.close()
    os.system("sudo /etc/init.d/squid restart")
    file_save = open(settings.SQUID_CONF + '.aron', 'wb')
    file_save.write(bf.crypt(open(settings.SQUID_CONF, 'r').read()))
    file_save.close()
    os.system("sudo echo "" > /etc/squid/squid.conf")
