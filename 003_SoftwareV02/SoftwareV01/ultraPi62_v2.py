#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#GPIO Pins zuweisen
#GPIO_TRIGGER_1 = 18
#GPIO_ECHO_1 = 16
GPIO_TRIGGER_2 = 23
GPIO_ECHO_2 = 20


#Richtung der GPIO-Pins festlegen (IN / OUT)
#GPIO.setup(GPIO_TRIGGER_1, GPIO.OUT)
#GPIO.setup(GPIO_ECHO_1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_2, GPIO.OUT)
GPIO.setup(GPIO_ECHO_2, GPIO.IN)


def distanz():
	
	# setze Trigger auf HIGH
	#GPIO.output(GPIO_TRIGGER_1, True)
	GPIO.output(GPIO_TRIGGER_2, True)
	

	# setze Trigger nach 0.01ms aus LOW  ##original 0.00001 
	time.sleep(0.00001)
	#GPIO.output(GPIO_TRIGGER_1, False)
	GPIO.output(GPIO_TRIGGER_2, False)
	

	# speichere Startzeit
	while GPIO.input(GPIO_ECHO_2) == 0 :#or GPIO.input(GPIO_ECHO_1) == 0:
		pass
	StartZeit = time.time()

	# speichere Ankunftszeit
	while GPIO.input(GPIO_ECHO_2) == 1 :#or GPIO.input(GPIO_ECHO_1) == 1:
		pass
	StopZeit = time.time()

	# Zeit Differenz zwischen Start und Ankunft
	TimeElapsed = StopZeit - StartZeit
	# mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren

	distanz = (TimeElapsed * 34300)

	return distanz

if __name__ == '__main__':
	try:
		while True:
			abstand = distanz()
			print ("Gemessene Entfernung = %.6f cm" % abstand)
			time.sleep(0.1)

		# Beim Abbruch durch STRG+C resetten
	except KeyboardInterrupt:
		print("Messung vom User gestoppt")
		GPIO.cleanup()

# calor  Trig  Echo
# Blue   18    16
# Green  23    20
# Pink   24    21
