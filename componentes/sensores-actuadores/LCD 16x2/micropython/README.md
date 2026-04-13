# 🚧 En construcción

Para usar la pantalla LCD con la Raspberry Pi Pico y la placa de expansión Robo Pico será necesario descargar el acrhivo "lcd1602.py" y grabarlo en la misma Pico, idealmente dentro de la carpeta "lib". Luego, desde micropython, de debe importar el código descargado como se muestra en los ejemplos incluidos en este repositorio.

```python
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
```
Esta pantalla LCD debe conectarse a cualquier conector Grove de la placa Robopico cuyos GP implementen funciones del protocolo I2C.

---

✏️ Nota interna: pendiente de validación por el equipo de Generación Tec.
