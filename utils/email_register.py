""" Archivo para el manejo de correos electrónicos. """
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
from os import getenv
from dotenv import load_dotenv

load_dotenv()


def send_register_email(email):
    """ Envía un correo electrónico de registro. """
    smtp_address = 'smtp.gmail.com'
    smtp_port = 465

    email_address = getenv('EMAIL')
    email_password = getenv('EMAIL_PASSWORD')

    # on crée un e-mail
    message = MIMEMultipart("alternative")
    # on ajoute un sujet
    message["Subject"] = "Registro de la Cuenta"
    # un émetteur
    message["From"] = "Geeks Hub"
    # un destinataire
    message["To"] = email

    texte = '''
                Bienvenido a Geeks Hub
                Gracias por registrarte en nuestra plataforma.
            '''

    with open('./static/html/register_email.html', 'r', encoding="utf8") as file:
        html = file.read()

    texte_mime = MIMEText(texte, 'plain')
    html_mime = MIMEText(html, 'html')

    message.attach(texte_mime)
    message.attach(html_mime)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        # connexion au compte
        server.login(email_address, email_password)
        # envoi du mail
        server.sendmail(email_address, email, message.as_string())
