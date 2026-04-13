from lcd1602 import LCD1602
from machine import I2C, Pin
from time import sleep

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
display = LCD1602(i2c, 2, 16)

while True:
    display.clear()             # Borramos la pantalla
    sleep(1)                    # Pausa de 1 segundo

    display.setCursor(0, 0)     # Cursor al inicio de la primera fila
    display.print("Hola")       # Escribimos el mensaje
    sleep(1)                    # Pausa de 1 segundo

    display.setCursor(0, 1)     # Cursor al inico de la segunda fila
    display.print("Mundo")      # Escribimos el mensaje
    sleep(1)                    # Pausa de 1 segundo