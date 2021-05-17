import telegram
import os
#token that can be generated talking with @BotFather on telegram

class Notification:
	"""Clase que contiene los metodos para envio de mensajes en telegram"""
	def __init__(self):
		self.token = 'TELEGRAM_ID'
		self.chat_id = 229945624
		
	def _sendMessage(self):
		'''Metodo que recibe envia mensaje con token y chat id'''
		bot = telegram.Bot(token=self.token)
		bot.sendMessage(chat_id=self.chat_id, text=self.msg)
		return 'Enviado'

	def notifyTg(self, msg):
		'''Ejecutor del envío'''

		self.msg = msg
		res = self._sendMessage()
		if res == 'Enviado':
			return res
		else:
			return 'Ha ocurrido un error en el envío'

	def notifyOs(self, title, text):
		os.system("""
				  osascript -e 'display notification "{}" with title "{}"'
				  """.format(text, title))

	#notifyOs("Se acabo el tiempo!", "Tómate 5 minutos")


#nt = NotificacionTeleg()
#∫nt.ejecutaEnvio('Probando el envío desde una clase')