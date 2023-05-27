import hashlib
import hmac
import time
import sys
import binascii
import os
import qrcode
from store import store_key
from generate import generate_otp
from tkinter import Tk, Label, Button, Entry, StringVar, END, W, E

'''
La classe FtOtp représente l'interface graphique pour l'application. 
Elle a une méthode generate_otp qui est appelée lorsque l'utilisateur clique sur le bouton "Generate OTP", 
lit la clé de l'entrée, génère l'OTP et l'affiche.
'''

class OTPGui:
    def __init__(self, master):
        self.master = master
        master.title("OTP Generator")

        self.key_label = Label(master, text="Key")
        self.key_entry = Entry(master)
        self.key_button = Button(master, text="Generate QR Code", command=self.generate_qr)

        self.otp_button = Button(master, text="Generate OTP", command=self.generate_otp)
        self.otp_text = StringVar()
        self.otp_label = Label(master, textvariable=self.otp_text)

        self.key_label.grid(row=0, column=0)
        self.key_entry.grid(row=0, column=1)
        self.key_button.grid(row=0, column=2)

        self.otp_button.grid(row=1, column=0)
        self.otp_label.grid(row=1, column=1)

    def generate_qr(self):
        key = self.key_entry.get()
        store_key('ft_otp.key', key)
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(key)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save('qr.png')

    def generate_otp(self):
        key_file = 'ft_otp.key'
        otp = generate_otp(key_file)
        self.otp_text.set(otp)