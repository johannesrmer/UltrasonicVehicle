#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#GPIO Pins zuweisen
GPIO_TRIGGER_G = 23
GPIO_ECHO_G = 20
GPIO_TRIGGER_B = 18 
GPIO_ECHO_B = 16
synchGpio = 25


#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER_G, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER_B, GPIO.OUT)
GPIO.setup(GPIO_ECHO_G, GPIO.IN)
GPIO.setup(GPIO_ECHO_B, GPIO.IN)
GPIO.setup(synchGpio, GPIO.OUT)


def Synch():
	GPIO.output(synchGpio, True)
	time.sleep(0.001)
	GPIO.output(synchGpio, False)

	
	
def Distanz():
	# setze Trigger auf HIGH
	GPIO.output(GPIO_TRIGGER_G, True)
	GPIO.output(GPIO_TRIGGER_B, True)

	# setze Trigger nach 0.01ms aus LOW
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER_G, False)
	GPIO.output(GPIO_TRIGGER_B, False)



	# speichere Startzeit
	while GPIO.input(GPIO_ECHO_B) == 0:
		pass
	StartZeit = time.time()

	# speichere Ankunftszeit
	while GPIO.input(GPIO_ECHO_B) == 1:
		pass
	StopZeit = time.time()

	# Zeit Differenz zwischen Start und Ankunft
	TimeElapsed = StopZeit - StartZeit
	# mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
	# und durch 2 teilen, da hin und zurueck
	distanz = (TimeElapsed * 34300) #/ 2 #hier auskomentiert da in eine richtung gemessen wird

	return distanz

def Distanz2(): 
        #Rueckwelle des Sensors der im weg liegt.
	GPIO.output(GPIO_TRIGGER_G, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER_G, False)

	while GPIO.input(GPIO_ECHO_G) == 0:
		pass
	StartZeit = time.time()
	
	while GPIO.input(GPIO_ECHO_G) == 1:
		pass
	StopZeit = time.time()
	
	TimeElapsed = StopZeit - StartZeit 
	distanz = (TimeElapsed * 34300) / 2 #man beachte die /2 :-D

	return distanz 

if __name__ == '__main__':
	try:
		while True:
			Synch()
			abstand = Distanz()
			print ("Gemessene Entfernung 1 = %.6f cm" % abstand)
			time.sleep(0.1)# hier minimieren
			abstand2 = Distanz2()
			print("Gemessene Entfernung 2 = %.6f cm" % abstand2)
			time.sleep(0.1)# hier nicht unbedingt! 

		# Beim Abbruch durch STRG+C resetten
	except KeyboardInterrupt:
		print("Messung vom User gestoppt")
		GPIO.cleanup()