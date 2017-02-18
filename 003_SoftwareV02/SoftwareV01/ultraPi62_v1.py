#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#GPIO Pins zuweisen
GPIO_TRIGGER_1 = 18
GPIO_ECHO_1 = 16
GPIO_TRIGGER_2 = 23
GPIO_ECHO_2 = 20


#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER_1, GPIO.OUT)
GPIO.setup(GPIO_ECHO_1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_2, GPIO.OUT)
GPIO.setup(GPIO_ECHO_2, GPIO.IN)


def Listen():
	
	# setze Trigger auf HIGH
	GPIO.output(GPIO_TRIGGER_1, True)
	GPIO.output(GPIO_TRIGGER_2, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER_1, False)
	GPIO.output(GPIO_TRIGGER_2, False)

	zeit = time.time()
	while GPIO.input(GPIO_ECHO_2) != 1 or GPIO.input(GPIO_ECHO_1) != 1:
		pass	

	return (time.time() - zeit) * 34300

if __name__ == '__main__':
	try:
		while True:
			zeit = Listen()
			print (zeit)
			time.sleep(0.1)

		# Beim Abbruch durch STRG+C resetten
	except KeyboardInterrupt:
		print("Messung vom User gestoppt")
		GPIO.cleanup()

# calor  Trig  Echo
# Blue   18    16
# Green  23    20
# Pink   4     5
