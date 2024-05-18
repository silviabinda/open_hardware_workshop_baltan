# This file is executed on every boot (including wake-boot from deepsleep)

# "Computing History - Ada" by Silvia Binda, 2024

import machine
import time
from machine import Pin, SoftI2C, PWM
from i2c_lcd import I2cLcd
import _thread
import urandom  # Import the urandom module for randomness

# Setup
ledPin = Pin(2, Pin.OUT)
ledPin.value(1)  # Turn the blue LED on
SPEAKER_PIN = 25
speaker = PWM(Pin(SPEAKER_PIN), freq=440, duty=0)

# I2C and LCD setup
I2C_ADDR = 0x27
totalColumns = 16
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
lcd = I2cLcd(i2c, I2C_ADDR, 2, totalColumns)

# Constants
title = "  ADA LOVELACE"
ada_born = 1815
ada_died = 1852
my_message = ("Ada Lovelace, an English mathematician and writer, is often referred to as "
              "'the first programmer' because she helped revolutionize the trajectory of "
              "the computer industry. She is considered the first person to recognize "
              "that computers had a much larger potential than mathematical calculation. "
              "In 1979, a computer language called 'Ada', made on behalf of the U.S. "
              "Department of Defense, was even named after her. (source: https://mit.edu)")

def pad_string(text, width):
    return text + ' ' * (width - len(text))


def scale_frequency(year):
    # Scale the year to a more audible frequency range
    return int((year - 1800) * 10 + 200)  # Example scaling

def play_melody():
    base_freqs = [scale_frequency(ada_born), scale_frequency(ada_died)]
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < 5000:  # Play for about 5 seconds
        freq = urandom.choice(base_freqs) + urandom.randint(-50, 50)  # Add some random variation
        dur = urandom.randint(100, 500)  # Duration between 100 ms and 500 ms
        speaker.freq(freq)
        speaker.duty(512)
        time.sleep_ms(dur)
        speaker.duty(0)
        time.sleep_ms(urandom.randint(50, 150))  # Random pause between notes
    # Consider not deinitializing if this will be called repeatedly
    # speaker.deinit()


def display_message_segments():
    lcd.putstr(title)
    words = my_message.split()
    line = ""
    index = 0
    first_run = True

    while True:
        if first_run:
            _thread.start_new_thread(play_melody, ())
            first_run = False
            
        if index < len(words):
            next_word = words[index]
            if len(line) + len(next_word) + 1 <= totalColumns:
                line += " " + next_word if line else next_word
            else:
                lcd.move_to(0, 1)
                lcd.putstr(pad_string(line, totalColumns))
                time.sleep(2)
                line = next_word
            index += 1
        else:
            if line:
                lcd.move_to(0, 1)
                lcd.putstr(pad_string(line, totalColumns))
                time.sleep(2)
            line = ""
            index = 0
            time.sleep(1)
            _thread.start_new_thread(play_melody, ())  # Restart melody

# Main execution
try:
    _thread.start_new_thread(play_melody, ())  # Start melody in a separate thread
    display_message_segments()
except Exception as e:
    print("Error:", e)


