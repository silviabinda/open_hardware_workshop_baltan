# Simple LED Blinking Code

# Connection Scheme for the LED and ESP32:
# - Connect the anode (longer leg) of the LED to GPIO pin 18 of the ESP32.
# - Connect the cathode (shorter leg) of the LED to one end of a current-limiting resistor (e.g. 220 ohms).
# - Connect the other end of the resistor to the GND pin of the ESP32.

import machine  # Import the machine module to control hardware components
import time  # Import the time module to add delays

# First, we need to define the pin for the LED, for example the GPIO 18 on our ESP32
led = machine.Pin(18, machine.Pin.OUT)
# 'machine.Pin' initializes a pin; '18' is the GPIO pin number where the LED is connected
# 'machine.Pin.OUT' sets the pin mode to output, meaning it will send out a signal to control the LED

# Start the main loop to blink the LED.
while True:
    led.value(1)  # Turn the LED on by setting the pin's value to 1 (high)
    time.sleep(1)  # Wait for 1 second (1000 milliseconds) while the LED is on
    led.value(0)  # Turn the LED off by setting the pin's value to 0 (low)
    time.sleep(1)  # Wait for 1 second (1000 milliseconds) while the LED is off
