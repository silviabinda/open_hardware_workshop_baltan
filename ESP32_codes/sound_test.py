import machine
import time
import random # for random numbers for the frequency and duration of sounds
from machine import Pin

# Define speaker pin
SPEAKER_PIN = 25

# Set up PWM for the speaker
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))

# Initialize random seed
random.seed(int(time.time()))

def DataSonification():

    while True:
        speaker.freq(10)
        speaker.duty(512)

DataSonification()
