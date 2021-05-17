from Timers import Pomodoro

while True:

	print('Welcome to Pomodoro')
	#Se especifica tiempo de duración del short break y del long break
	#notification type: os, telegram
	pruebita = Pomodoro(4,7, 'OS')
	pruebita.timer()

	while True:
		var = input('This Cycle has finished, do you want to do it again?(y/n): ')
		if str(var) == 'y' or str(var) == 'n':
			exit = var
			break
		else:
			print('This choice is not valid, please type it again')
		

	if exit == 'n':
		print('Thanks for using Pomodoro')
		break
