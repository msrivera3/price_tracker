from email import message
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SmptConfig:
    
    server_smtp = 'smtp.office365.com'
    port_smtp = 587
    user_smtp = 'camiloandres_kane@hotmail.com'
    password_smtp = 'Colombia2019'

        
        
    def notify(self,destiny, affair, body):


        # Crear objeto de conexión SMTP
        conexion_smtp = smtplib.SMTP(self.server_smtp, self.port_smtp)
        conexion_smtp.starttls()

        # Iniciar sesión en el servidor SMTP
        conexion_smtp.login(self.user_smtp, self.password_smtp)

        # Construir el mensaje
        message = MIMEMultipart()
        message['From'] = self.user_smtp
        message['To'] = destiny
        message['Subject'] = affair

        # Agregar el cuerpo del mensaje
        message.attach(MIMEText('Notificacion de precio: {}'.format(body), 'plain'))

        # Enviar el mensaje
        conexion_smtp.sendmail(self.user_smtp, destiny, message.as_string())

        # Cerrar la conexión SMTP
        conexion_smtp.quit()

    