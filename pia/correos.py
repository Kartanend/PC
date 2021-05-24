import smtplib
from email.mime.text import MIMEText
import logging


def env_correo(user,pwd,to,subject,text):
    """
    Envía un correo desde la dirección de origen teniendo su contraseña hacia un correo destino
    con el asunto y cuerpo recibidos.

    Args:
        user (str): Es la direccion de correo desde la cual se enviara el correo.
        pwd (str): Es la contraseña del correo de origen recibida en la variable user.
        to (str): Es la direccion de correo destino que recibira el correo.
        subject (str): Es el asunto del correo a enviar.
        text (str): Es el texto del correo a enviar.

    Prints:
        Imprime los mensajes de progreso de envio del correo.
    """
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    try:
        smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
        print("[+] Connecting To Mail Server.")
        smtpServer.ehlo()
        print("[+] Starting Encrypted Session.")
        smtpServer.starttls()
        smtpServer.ehlo()
        print("[+] Logging Into Mail Server.")
        smtpServer.login(user, pwd)
        print("[+] Sending Mail.")
        smtpServer.sendmail(user, to, msg.as_string())
        smtpServer.close()
        print("[+] Mail Sent Successfully.")
    except:
        logging.error("[-] Sending Mail Failed.")
