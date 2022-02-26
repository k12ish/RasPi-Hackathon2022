
import RPi.GPIO as GPIO  
from time import sleep    
GPIO.setmode(GPIO.BCM)     
num = 23
GPIO.setup(num, GPIO.IN)

def is_stealing():   
    return (not GPIO.input(num))
         
