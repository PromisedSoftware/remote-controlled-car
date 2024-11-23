import pygame
import os
from time import sleep

from gpiozero import Servo
from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory

# Run daemon for gpio pins for more accurate movement
os.system('sudo pigpiod')
sleep(2)

# Control servo with BCM pin 17
factoryServo = PiGPIOFactory()
servo = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory = factoryServo)
servo.mid()

# Control forward motor with BCM pin 18
factoryMotorForward = PiGPIOFactory()
motorForward = PWMLED(18, pin_factory = factoryMotorForward)
motorForward.value = 0.0

# Control backward motor with BCM pin 13
factoryMotorBackward = PiGPIOFactory()
motorBackward = PWMLED(13, pin_factory = factoryMotorBackward)
motorBackward.value = 0.0

# Dummy screen for no screen aplications
os.environ["SDL_VIDEODRIVER"] = "dummy"

# Initialize pygame
pygame.init()
#Getting controller connected event
for event in pygame.event.get():
    if event.type == pygame.JOYDEVICEADDED:
        pad = pygame.joystick.Joystick(event.device_index)
pad.init()

# Functions
def ender():
    print("Ending program")
    servo.mid()
    motorForward.off()
    motorBackward.off()
    sleep(1)
    servo.detach()
    PiD = os.popen('sudo pgrep pigpiod').read().strip()
    PiD = "sudo kill " + PiD
    os.system(PiD)
    print("program terminated")

isBackwardMotorActive = False
isWorking = True
# Application loop
while isWorking:
    # loop speed reduction
    sleep(0.01)

    # When servo is installed backwards change "-0.5" to be possitive value
    servo.value = round(pad.get_axis(2),1) * -0.5

    # Motor speed that allows to run forward or backward
    if(round(pad.get_axis(1),1) <= 0 ) and not isBackwardMotorActive:
        motorForward.value = round(pad.get_axis(1),1) * -1
    elif round(pad.get_axis(1),1) >= 0 and isBackwardMotorActive:
        motorBackward.value = round(pad.get_axis(1),1)

    # Checking if button is pressed
    events=pygame.event.get()
    for event in events:
        if event.type == pygame.JOYBUTTONDOWN:
            if event.joy == pad.get_id():
                index = event.button

                # if True end program
                if index == 5: # 5 is index of button that on Dualsense stands for PS button
                    isWorking = False
                    ender()
                
                # if True disable current DC motor, and enable opposite directrion DC motor
                elif index == 4: # 4 is index of button that on Dualsense stands for "Create" button
                    isBackwardMotorActive = not isBackwardMotorActive