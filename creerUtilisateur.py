import subprocess, sys
import mysql.connector


print("Bonjour dans le programme de creation d'utilisateur ")
username = input("Veuillez saisir le email à creer:")
password = input("Veuillez saisir le mot de passe:")

conn = mysql.connector.connect(
	host="localhost",
	user="root",
	password="root",
	database="vmail"
)

cursor = conn.cursor()


#username = "ali@smarttech.sn"
#password = "'Passer2024@'"
commandForSqlInstruct = "/home/mohamed/iRedMail-1.7.1/tools/create_mail_user_SQL.sh"+" "+username+" "+ f"'{password}'" + " > /tmp/user.sql" 

try:
	result = subprocess.run(commandForSqlInstruct, shell= True, executable = "/bin/bash", stderr = subprocess.STDOUT)
	
	with open('/tmp/user.sql', 'r') as file:
		sqlCommands = file.read()
		sqlCommands = sqlCommands.split(';')
	
	for command in sqlCommands:
		if command.strip():
			try:
				cursor.execute(command)
			except Exception as error:
				print(f"Erreur: {error}")
	
except Exception as error:
	print(f"erreur: {error}")

finally:
	conn.commit()
	print(f"Le compte {username} est cree avec succes")
	print(f"Avec le mot de passe {password}")
	subprocess.run("rm /tmp/user.sql", shell= True, executable = "/bin/bash")
	conn.close

