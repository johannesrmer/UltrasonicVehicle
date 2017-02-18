
#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#GPIO Pins zuweisen
GPIO_SYNCH = 25

GPIO_TRIGGER = 23
GPIO_ECHO = 24


#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_SYNCH, GPIO.IN)

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
    			#GPIO.output(GPIO_SYNCH, True)
    			#time.sleep(0.00001)
    			#GPIO.output(GPIO_SYNCH,False)
			while GPIO.input(GPIO_SYNCH) == 0:
				pass
			while GPIO.input(GPIO_SYNCH) == 1:
				pass

			SendSignal()
	except KeyboardInterrupt:
		print("Messung vom User gestoppt")
		GPIO.cleanup()

    
