import time
import RPi.GPIO as GPIO

# Set up the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

RED = GPIO.PWM(18, 100)
GREEN = GPIO.PWM(23, 100)
BLUE = GPIO.PWM(24, 100)

with open('text.txt', 'r') as f:
    more_dict = eval(f.read())
    morse_dict = {
        'A': 'SL',
        'B': 'LSSS',
        'C': 'LSLS',
        'D': 'LSS',
        'E': 'S',
        'F': 'SSLS',
        'G': 'LLS',
        'H': 'SSSS',
        'I': 'SS',
        'J': 'SLLL',
        'K': 'LSL',
        'L': 'SLSS',
        'N': 'LS',
        'M': 'LL',
        'O': 'LLL',
        'P': 'SLLS',
        'Q': 'LLSL',
        'R': 'SLS',
        'S': 'SSS',
        'T': 'L',
        'U': 'SSL',
        'V': 'SSSL',
        'W': 'SLL',
        'X': 'LSSL',
        'Y': 'LSLL',
        'Z': 'LLSS'
    }