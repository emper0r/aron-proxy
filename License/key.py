from __future__ import absolute_import, division, print_function, unicode_literals
import hashlib
import base58
import libnacl.public
import libnacl.secret

XID_PREFIX = b'\x5f'
KEY_PREFIX = b'\xba'
SECRET_PREFIX = b'\xff'

def generate_keypair(sk=None):
    """
    Generate a random key pair.
    :return:
    """
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
