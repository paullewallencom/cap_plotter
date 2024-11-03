from machine import Pin
import utime

counter = 0

SAMPLING_TIME = 1 #seconds

pulsePin = Pin(15, Pin.IN, Pin.PULL_DOWN)

def ihandler(pulsePin):
    global counter
    counter += 1
    #print("run")

pulsePin.irq(trigger = Pin.IRQ_RISING, handler = ihandler)

while True:
    utime.sleep(SAMPLING_TIME)
    pulse_per_sample = counter
    pulse_per_sec = pulse_per_sample / SAMPLING_TIME
    print("Pulse Frequency (samples/sec): ", pulse_per_sec)
    counter = 0