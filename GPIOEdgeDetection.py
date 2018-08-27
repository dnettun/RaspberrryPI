#GPIO 26 is used for this example
import RPi.GPIO as GPIO
import pigpio
import time

#initiate variables
pi=pigpio.pi()
BTN_B = 26
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BTN_B, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
print pi.get_mode(26)

def handle(pin):
    print GPIO.input(BTN_B) 
    pi.set_PWM_dutycycle(17, 0)
    pi.set_PWM_dutycycle(22, 155)
    pi.set_PWM_dutycycle(27, 155)
    time.sleep(1)
    pi.set_PWM_dutycycle(17, 155)
    pi.set_PWM_dutycycle(22, 155)
    pi.set_PWM_dutycycle(27, 155)
    
   

GPIO.add_event_detect(BTN_B, GPIO.BOTH, handle)


while True:
        time.sleep(1e6)