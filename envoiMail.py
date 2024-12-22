import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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


sendMail("TEST", "Ceci est un test d'envoi par python", "samba@smarttech.sn")
