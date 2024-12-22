import imaplib
import email
from email.header import decode_header


def receiveMail():
	imap_server =  "mail.smarttech.sn"
	imap_port = 993
	user = "mohamed@smarttech.sn"
	user_password = "Passer2024@"
	

	try:
		mail = imaplib.IMAP4_SSL(imap_server, imap_port)
		mail.login(user, user_password)
		print("Connexion reussie")


		mail.select("inbox")

		status, messages = mail.search(None, "UNSEEN")

		if status == "OK":
			message_ids = messages[0].split()

			if not message_ids:
				print("Pas de nouveaux messages")
			else:
				print(f"Vous avez {len(message_ids)} nouveaux messages")
				for msg_id in message_ids:
					_, msg_data = mail.fetch(msg_id, "(RFC822)")
					for response_part in msg_data:
						if isinstance(response_part, tuple):
						    # Analyser le message
						    msg = email.message_from_bytes(response_part[1])

						    # Décoder le sujet du message
						    subject, encoding = decode_header(msg["Subject"])[0]
						    if isinstance(subject, bytes):
						        subject = subject.decode(encoding if encoding else "utf-8")
						    from_ = msg.get("From")

						    print("Sujet:", subject)
						    print("De:", from_)

		else:
			print("Pas de nouveaux message")

	except Exception as error:
		print(f"Erreur lors de la reception: {error}")

receiveMail()

