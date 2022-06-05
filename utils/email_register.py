""" Archivo para el manejo de correos electrónicos. """
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def generate_email(email):
    """ Genera el HTML de un correo electrónico """
    email_address = getenv('EMAIL')
    # on crée un e-mail
    message = MIMEMultipart("alternative")
    # on ajoute un sujet
    message["Subject"] = "Registro de la Cuenta"
    # un émetteur
    message["From"] = email_address
    # un destinataire
    message["To"] = email

    texte = '''
            Bonjour 
            Ma super newsletter
            Cdt
            mon_lien_incroyable
            '''

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
