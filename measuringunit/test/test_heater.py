# toggle_heater.py
import time
import RPi.GPIO as GPIO

# Set up the GPIO pin for the heater control (e.g., GPIO17)
HEATER_PIN = 17

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(HEATER_PIN, GPIO.OUT)

try:
    # Turn the heater on
    GPIO.output(HEATER_PIN, GPIO.HIGH)
    print("HEATER ON")
    
    # Wait for one second
    time.sleep(1)
    
    # Turn the heater off
    GPIO.output(HEATER_PIN, GPIO.LOW)
    print("HEATER OFF")

finally:
    # Cleanup GPIO state
    GPIO.cleanup()
