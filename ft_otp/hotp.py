import hashlib
import hmac
import time
import sys
import binascii
import os

'''
Cette fonction implémente l'algorithme HOTP, 
tel que décrit dans la RFC 4226. 
Elle prend une clé K et un compteur C comme entrées, 
et retourne un mot de passe à usage unique de 6 chiffres.

'''

def HOTP(K, C, digits=6):
    K_bytes = binascii.unhexlify(K)
    C_bytes = C.to_bytes(8, 'big')
    hmac_sha1 = hmac.new(key=K_bytes, msg=C_bytes, digestmod=hashlib.sha1).hexdigest()
    O = int(hmac_sha1[-1], 16)
    DynamicBinaryCode = int(hmac_sha1[O * 2:O * 2 + 8], 16) & 0x7fffffff
    return str(DynamicBinaryCode)[-digits:]