#!/usr/bin/python
from web import settings
from Crypto.Cipher import AES
import base64


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

load_f = open(decrypt('22V2vVtVeGiEZ5YtTVz7fcGKkjndAGJ/4aRyg4lC+Ks='), 'r')
try:
    ctx = decrypt(load_f.read())
    s_f = open(decrypt('22V2vVtVeGiEZ5YtTVz7ffhdOO5jCiI/dSz3IFEq0k4='), 'w')
    s_f.write(ctx)
    s_f.close()
    load_f.close()
except:
    load_f.close()