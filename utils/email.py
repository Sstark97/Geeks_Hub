""" Archivo para el manejo de correos electrónicos. """
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def send_register_email(email):
    """ Envía un correo electrónico de registro. """
    smtp_address = 'smtp.gmail.com'
    smtp_port = 465

    email_address = getenv('EMAIL')
    email_password = getenv('EMAIL_PASSWORD')

    print(email_address)
    print(email_password)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        # Conexión con el servidor de correos.
        server.login(email_address, email_password)
        # Envío del correo.
        server.sendmail(email_address, email, 'Registro de la Cuenta')
