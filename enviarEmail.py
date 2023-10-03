import smtplib

def enviarEmail(remitente, destinatario, mensaje):
    usuario = remitente
    password = 'vtin klyl krus tcdn' #aqui se crea una contraseña para aplicaciones 
    try:
        conexion = smtplib.SMTP('smtp.gmail.com', 587)
        conexion.starttls()
        conexion.login(usuario, password)
        print("Login correcto")
        conexion.sendmail(remitente, destinatario, mensaje)
        print("email enviado correctamente")
        conexion.quit()
    except smtplib.SMTPAuthenticationError:
        print("error de autenticacion")

if __name__ == "__main__":
    enviar("anapythondev@gmail.com", "anapythondev@gmail.com", "hola prueba desde python")