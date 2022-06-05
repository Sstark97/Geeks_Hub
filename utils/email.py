""" Archivo para el manejo de correos electrónicos. """
import smtplib, ssl
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def send_register_email(email):
    """ Envía un correo electrónico de registro. """
    smtp_address = 'smtp.gmail.com'
    smtp_port = 465

    email_address = getenv('EMAIL')
    email_password = getenv('EMAIL_PASSWORD')
