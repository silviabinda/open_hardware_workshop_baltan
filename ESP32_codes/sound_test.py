# This is a code to simply test the functionality of the speaker and amplifier

import machine
import time
from machine import Pin

# Define the speaker pin
SPEAKER_PIN = 25

# Set up PWM for the speaker
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))

# We create a function, we name it DataSonification
def DataSonification():
    while True:
        speaker.freq(100)
        speaker.duty(512)
# info: speaker.freq determines the Frequency in Hz. Values from 0 up to 20000 (=20 kHz, which is the limit of audible range for humans)
# info: speaker.duty determines the volume and characteristics of the sound. Values from 0 to 1023 (for a 10bit PWM resolution, which is default)

# Run the function:
DataSonification() 
