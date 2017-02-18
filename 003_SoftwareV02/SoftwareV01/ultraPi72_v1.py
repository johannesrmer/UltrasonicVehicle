#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#GPIO Pins zuweisen
GPIO_TRIGGER = 4
GPIO_ECHO = 5


#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def SendSignal():
	GPIO.output(GPIO_TRIGGER, True)
	# setze Trigger nach 0.01ms aus LOW  ##original 0.00001 
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	startZeit = time.time()
	return startZeit
	
if __name__ == '__main__':
	try:
		while True:
			zeit = SendSignal()
			print (zeit)
			time.sleep(0.001)

		# Beim Abbruch durch STRG+C resetten
	except KeyboardInterrupt:
		print("Messung vom User gestoppt")
		GPIO.cleanup()

# calor  Trig  Echo
# Blue   18    16
# Green  23    20
# Pink   4     5
