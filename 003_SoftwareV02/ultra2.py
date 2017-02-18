#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#GPIO Pins zuweisen
GPIO_TRIGGER_1 = 23
GPIO_ECHO_1 = 24
synchGpio = 25
startZeit = 0

#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER_1, GPIO.OUT)
GPIO.setup(GPIO_ECHO_1, GPIO.IN)
GPIO.setup(synchGpio, GPIO.IN)

def Synch():
	while GPIO.input(synchGpio)==0:
		pass	
	startZeit = time.time()
	return startZeit

def distanz():
	# setze Trigger auf HIGH
	GPIO.output(GPIO_TRIGGER_1, True)
	# setze Trigger nach 0.01ms aus LOW  ##original 0.00001 
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER_1, False)

	while GPIO.input(GPIO_ECHO_1) == 0:
		pass
	startZeit = time.time()

	# speichere Ankunftszeit
	while GPIO.input(GPIO_ECHO_1) == 1:
		pass
	StopZeit = time.time()

	# Zeit Differenz zwischen Start und Ankunft
	TimeElapsed = StopZeit - startZeit
	
	distanz = TimeElapsed *34300 

	return distanz #StopZeit

if __name__ == '__main__':
	last = 0

	try:
		while True:
			
			synch = Synch()
			#distance =distanz() # (distanz()-synch)*34300
			#print ("Gemessener Abstand: = %.6f cm" %distance)
			print( synch - last)
			last = synch	
			

		# Beim Abbruch durch STRG+C resetten
	except KeyboardInterrupt:
		print("Messung vom User gestoppt")
		GPIO.cleanup()

# calor  Trig  Echo
# Pink   23    24
