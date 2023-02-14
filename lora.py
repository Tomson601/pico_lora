import time
from machine import Pin, SPI

# SPI initialization
spi = SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(8))
# Reset initialization
rst = Pin(1, Pin.OUT)
cs = Pin(2, Pin.OUT)
# Adding LED pin
led = Pin("LED", Pin.OUT)
led.off()
# LoRa module boot up
rst.value(0)
time.sleep(0.01)
rst.value(1)

# Waiting for LoRa initialization
time.sleep(0.5)

rxdata = bytearray(1)
try:
    cs(0)  # Select peripheral.
    spi.readinto(rxdata, 0x42)  # Read **1** byte in place while writing 0x42.
    led.on()
finally:
    cs(1)  # Deselect peripheral.

print('LoRa module version: ', rxdata)

if rxdata == 0x12:
    print('LoRa module working!')
else:
    print('LoRa module, not working properly')
