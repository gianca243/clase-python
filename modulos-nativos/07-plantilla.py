from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

# plantilla = """
#     <b>hola mundo $usuario</b>
# """
plantilla = Path(r".\modulos-nativos\plantilla.html").read_text
template = Template(plantilla)
# cuerpo = template.substitute({
#     "usuario": "chanchito feliz"
# })

path = Path("")
mime_image = MIMEImage(path.read_bytes())

mensaje = MIMEMultipart()

mensaje["from"] = "Hola mundo"
mensaje["to"] = "gianca243@gmail.com"
mensaje["subject"] = "Esta es una prueba"
cuerpo = MIMEText("cuerpo del mensaje")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # identifica
    smtp.starttls()  # encripta

    smtp.login("gianca243@gmail.com", "password")
    smtp.send_message(mensaje)
    print("Mensaje enviado")
