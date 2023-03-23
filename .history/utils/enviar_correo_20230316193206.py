from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

def enviar_correo(destinatario, titulo, cuerpo):
    mensaje = MIMEMultipart
    email_emisor = 'inyeniushhm455@gmail.com'
    password_email_emisor = 'XXXXXXXXX'

    # Agregando el cuerpo a nuestro mensaje
    mensaje['Subject'] = titulo

    # Agregando el cuerpo anuestro mensaje
    mensaje.attach(MIMEText(cuerpo))

    #                   SERVIDOR      | PUERTO
    # outlook > outlook.office365.com | 587
    # hotmail > smtp.live.com         | 587
    # gmail >   smtp.gmail.com        | 587
    # icloud >  smtp.mail.me.com      | 587
    # yahoo >   smtp.mail.yahoo.com   | 587

    emisor = SMTP('smtp.gmail.com', 587)

    emisor.starttls()

    emisor.login(user= email_emisor, password= password_email_emisor)

    emisor.sendmail(email= email_emisor, to_addrs=destinatario, msg=mensaje.as_string())