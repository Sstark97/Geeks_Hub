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

    # Creación del mensaje
    message = MIMEMultipart("alternative")
    # Añadir un asunto
    message["Subject"] = "Registro de la Cuenta"
    # Añadir un emisor
    message["From"] = "Geeks Hub"
    # Añadir un destinatario
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
        # Conexion al servidor
        server.login(email_address, email_password)
        # Envio del correo
        server.sendmail(email_address, email, message.as_string())

def send_change_password(email, code):
    """ Envía un correo electrónico de cambio de contraseña. """
    smtp_address = 'smtp.gmail.com'
    smtp_port = 465

    email_address = getenv('EMAIL')
    email_password = getenv('EMAIL_PASSWORD')

    # Creación del mensaje
    message = MIMEMultipart("alternative")
    # Añadir un asunto
    message["Subject"] = "Cambio de Contraseña"
    # Añadir un emisor
    message["From"] = "Geeks Hub"
    # Añadir un destinatario
    message["To"] = email

    texte = f'''
                Has solicitado un cambio de contraseña.
                El Codigo de Confirmación es: {code}
                Para cambiarla, haz click en el siguiente enlace:
                http://localhost:8080/change_password_process
            '''
        
    texte_mime = MIMEText(texte, 'plain')

    message.attach(texte_mime)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        # Conexion al servidor
        server.login(email_address, email_password)
        # Envio del correo
        server.sendmail(email_address, email, message.as_string())

    
