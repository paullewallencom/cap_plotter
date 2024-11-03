import machine
import utime

analog_value = machine.ADC(28)

n = 1
while (n<1000):
    reading = analog_value.read_u16()
    print(reading)
    utime.sleep(0.0005)
    n = n + 1