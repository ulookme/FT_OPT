import os
import sys

'''
Cette fonction stocke une clé hexadécimale dans un fichier.
Le nom du fichier et la clé sont passés en paramètres.
'''


def store_key(file_name, hex_key):
    with open(file_name, 'w') as f:
        f.write(hex_key)
    print(f"Key was successfully saved in {file_name}.")
  