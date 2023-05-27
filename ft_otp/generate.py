import hashlib
import hmac
import time
import sys
import binascii
import os
from hotp import HOTP

'''
Cette fonction génère un mot de passe à usage unique en lisant la clé du fichier spécifié et 
en utilisant le temps actuel comme compteur pour l'algorithme HOTP.
'''

def generate_otp(file_name):
    with open(file_name, 'r') as f:
        hex_key = f.read().strip()
    if len(hex_key) != 64:
        print("error: Key must be 64 hexadecimal characters.")
    return HOTP(hex_key, int(time.time() // 30))