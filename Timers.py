import time
#from notificacion import *
from notificacion_manager import Notification

class Pomodoro:
	'''Clase donde se definen los timers utilizados en el pomodoro'''

	def __init__(self, short_break, long_break, notification_type):

		self.time_s = 10
		self.time_cd = self.time_s
		self.short_break = short_break
		self.long_break = long_break
		self.counter = 1
		self.notification = Notification()
		self.notification_type = notification_type
		self.title = "Time is up!"
		self.short_msg = "Take a 5 minutes break!"
		self.long_msg = "Now take a 15 minutes break!"

	def timer(self):
		'''Ciclo principal de duración fija = 25 minutos'''
		while True:
			print(self.time_cd)
			time.sleep(1)
			self.time_cd -= 1

			if self.time_cd == 0:

				if self.counter <= 4:
					#Llama a short break timer
					self._short_break_timer()
					print(f"counter {self.counter}")
					#llamamos a reset time_cd
					#seconds_cd = seconds
					self._reset_time_cd()
					#Llamamos increase_counter
					self._increase_counter()
					#counter += 1
				elif self.counter > 4:
			
					#Llamamos al long break timer
					self._long_break_timer()
					break

	def _short_break_timer(self):
		'''Timer para break corto que se genera entre los ciclos de 
		timer principal'''
		#print("Time's up!, take a break")
		#notify("Time is up!", "Take a 5 minutes break!")
		if self.notification_type.upper() == 'TELEGRAM':
			self.notification.notifyTg(self.title + ', '+ self.short_msg)
		elif self.notification_type.upper() == 'OS':
			self.notification.notifyOs(self.title, self.short_msg)
		
		while self.short_break > 0:
			print(f"5 mins Break: {self.short_break}")
			time.sleep(1)
			self.short_break -= 1
		
	def _long_break_timer(self):
		'''Timer para break largo que se genera cuando se ha iterado
		4 veces en el ciclo principal y el contador llega a 4'''
		#print("Time's up!, nos it's time for a longer break")
		#notify("Time is up!", "Now take a longer break!")
		if self.notification_type.upper() == 'TELEGRAM':
			self.notification.notifyTg(self.title + ', '+ self.long_msg)
		elif self.notification_type.upper() == 'OS':
			self.notification.notifyOs(self.title, self.long_msg)

		while self.long_break > 0:
			print(f"Longer Break: {self.long_break}")
			time.sleep(1)
			self.long_break -= 1

	def _reset_time_cd(self):
		'''Igualamos time_cd a time para reiniciar el ciclo principal'''
		self.time_cd = self.time_s

	def _increase_counter(self):
		'''Incrementa el counter en 1'''
		self.counter += 1
		

#pruebita = Pomodoro(4,7)
#pruebita.timer()
