# This file is executed on every boot (including wake-boot from deepsleep)
import machine, network, utime, neopixel, time
import ubinascii
from pye import pye

# gpio==
from machine import Pin, ADC #ws2812, piezo
np = neopixel.NeoPixel(Pin(16), 4, timing=1)
adc = ADC(Pin(34))

print("")
print("Starting WiFi ...")
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("SSID", "PASSWORD")
while not sta_if.isconnected():
    utime.sleep_ms(100)

print("WiFi started")
utime.sleep_ms(500)
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()

def red():
  print("red")
  n = np.n
  for i in range(n):
    np[i] = (255, 0, 0)
  np.write()

def green():
  print("green")
  n = np.n
  for i in range(n):
    np[i] = (0, 255, 0)
  np.write()

def blue():
  print("blue")
  n = np.n
  for i in range(n):
    np[i] = (0, 0, 255)
  np.write()

def off():
  n = np.n
  for i in range(n):
    np[i] = (0, 0, 0)
  np.write()

threshold = 100
color = (255,0,0)

def blink(color):
    for i in range(np.n):
        np[i] = color
    np.write()
    time.sleep_ms(500)
    for i in range(np.n):
        np[i] = (0, 0, 0)
    np.write()

def listen():
    #print(adc.read())
    if adc.read() < threshold:
      blink(color)
      time.sleep_ms(150)
      


def main():
  print("mac address", mac)
  off()

  try:
    while True:
      listen()
      time.sleep_ms(25)

  except (KeyboardInterrupt):
    print('\n', "Exit on Ctrl-C: Good bye!")

  finally:
    print('\n', "Disconnecting.")
   
if __name__ == "__main__":
    main()
