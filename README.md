# Projet FT_OTP
Ce projet est un générateur de mots de passe à usage unique (OTP) basé sur l'algorithme HOTP (HMAC-based One-Time Password). Il est conçu pour être utilisé avec une clé hexadécimale de 64 caractères, qui est stockée de manière sécurisée dans un fichier. Le programme peut générer un nouvel OTP à chaque fois qu'il est demandé, en utilisant le temps actuel comme compteur.

Fonctionnalités
Génération de mots de passe à usage unique (OTP) : Le programme génère un OTP à chaque fois qu'il est demandé.

Stockage sécurisé de la clé : La clé hexadécimale de 64 caractères est stockée de manière sécurisée dans un fichier.

Interface graphique : Le programme comprend une interface graphique simple qui permet à l'utilisateur d'entrer la clé et de générer l'OTP.

Utilisation
Lancer le programme en utilisant la commande suivante:

Copy code
python3 ft_otp.py
Dans l'interface graphique, entrez la clé hexadécimale de 64 caractères dans le champ de saisie, puis cliquez sur le bouton "Generate OTP" pour générer le mot de passe à usage unique.

Dépendances
Ce programme dépend des modules Python suivants :

secrets
Tkinter
time
hmac
hashlib
base64
fait par chajjar42
