import serial
import time
import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
for p in ports:
    if 'Arduino' in p[1]:
        arduino = p[0]
arduinoData = serial.Serial(arduino,9600)

time.sleep(3)
def led_on():
    on = 1
    if on == 1:
        arduinoData.write(b'1')