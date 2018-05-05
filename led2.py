import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

def led_on():

	print ("LED on")
	GPIO.output(18,GPIO.HIGH)

def led_off():

	print ("LED off")
	GPIO.output(18,GPIO.LOW)

led_on()
time.sleep(1)
led_off()

CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}
ledPin=18

def dot():
	GPIO.output(ledPin,1)
	time.sleep(0.2)
	GPIO.output(ledPin,0)
	time.sleep(0.2)

def dash():
	GPIO.output(ledPin,1)
	time.sleep(0.5)
	GPIO.output(ledPin,0)
	time.sleep(0.2)

def talk(input):
	for letter in input:
			for symbol in CODE[letter.upper()]:
				if symbol == '-':
					dash()
				elif symbol == '.':
					dot()
				else:
					time.sleep(0.5)
			time.sleep(0.5)


def state(pin):
	st = GPIO.input(int(pin))
	
	if (st == True):
		return ("Ligado")
	else:
		return ("Desligado")
