import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

def sendMail(subject, body, to):
	smtp_server = "mail.smarttech.sn"
	smtp_port = 587
	from_email = "mohamed@smarttech.sn"
	from_password = "Passer2024@"
	
	# creation du message
	
	message = MIMEMultipart()
	message["From"] = from_email
	message["To"] = to
	message["Subject"] = subject

	message.attach(MIMEText(body, "plain"))

	try: 
		server = smtplib.SMTP(smtp_server, smtp_port)
		server.starttls()
		server.login(from_email, from_password)

		server.sendmail(from_email, to, message.as_string())
		print("Message envoyé")

	except Exception as error:
		print(f"Erreur lors de l'envoi de l'email: {error}")

	finally:
		server.quit()

print("Envoi d'email")
print("Veuillez patienter...")
time.sleep(2)

print("Veuillez saisir les informations suivantes")
print("Sujet: ")
subject = input()
print("Message: ")
body = input()
print("Destinataire: ")
to = input()
print("Envoi en cours...")
sendMail(subject, body, to)
print("Email envoyé avec succès")
