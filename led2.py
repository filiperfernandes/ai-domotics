import RPi.GPIO as GPIO
import time, subprocess
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

def led_on(pin):

	print ("LED on")
	GPIO.output(pin,GPIO.HIGH)

def led_off(pin):

	print ("LED off")
	GPIO.output(pin,GPIO.LOW)

led_on(18)
time.sleep(1)
led_off(18)

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
		return ("1")
	else:
		return ("0")

def mpcCommand(cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        return  p.stdout.read()

