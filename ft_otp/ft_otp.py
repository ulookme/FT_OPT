import sys
import binascii
import os
from hotp import HOTP
from store import store_key
from generate import generate_otp
from interface_opt import OTPGui
import hashlib
import hmac
import time
import sys
import binascii
import os
import qrcode
import secrets
from tkinter import Tk, Label, Button, Entry, StringVar, END, W, E

'''
Cette fonction est le point d'entrée du programme. 
Elle prend les arguments de la ligne de commande, 
effectue les vérifications nécessaires, 
et appelle les fonctions appropriées en fonction des arguments.
Elle crée l'interface graphique et la lance.
'''

# Fonction principale
def main(args):
    if len(args) < 3:
        root = Tk()
        my_gui = OTPGui(root)
        root.mainloop()
    else:
        action = args[1]
        nom_fichier = args[2]
        if action == '-g':
            with open(nom_fichier, 'r') as f:
                hex_key = f.read().strip()
            if len(hex_key) != 64:
                raise ValueError("La clé doit être de 64 caractères hexadécimaux.")
            store_key('ft_otp.key',hex_key)

        elif action == '-k':
            with open(nom_fichier, 'r') as f:
                hex_key = f.read().strip()
            if len(hex_key) != 64:
                # Générer une clé hexadécimale aléatoire de 64 caractères
                key = secrets.token_hex(32)
                # Ouvrir le fichier en mode d'écriture et écrire la clé
                with open('ft_otp.key', 'w') as f:
                    f.write(key)
                print("optien generate auto pour demos.")
            else:
                print(generate_otp(nom_fichier))
            #print(generate_otp(nom_fichier))
        else:
            print("Action invalide. Utilisez -g pour stocker la clé, ou -k pour générer un OTP.")

if __name__ == "__main__":
    main(sys.argv)