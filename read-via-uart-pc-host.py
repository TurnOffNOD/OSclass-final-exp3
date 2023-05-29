#!/usr/bin/python3

import serial

WAKEUP_DEV_FRAME = bytes.fromhex("55 55 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FF 03 FD D4 14 01 17 00")

DET_CARD_FRAME = bytes.fromhex("00 00 FF 04 FC D4 4A 01 00 E1 00")
#print(type(detect_card_frame))
#print(detect_card_frame)

uart_port = serial.Serial('/dev/ttyUSB0', 115200, 8, 'N', 1)

flag =uart_port.is_open

if flag:
    print("serial port", uart_port.name, " open Successfully.")
else:
    print("serial port", uart_port.name, " open Failed.")

uart_port.write(WAKEUP_DEV_FRAME)
wakeup_ack = uart_port.read(15)
#for i in bytes(wakeup_ack):
    #print('%2s' % (hex(i)), end=" ")
    #print(type(hex(i)))
print((wakeup_ack.hex(' ')).upper())


uart_port.write(DET_CARD_FRAME)
det_card_frame_ack = uart_port.read(6)
print((det_card_frame_ack.hex(" ")).upper())
print((det_card_frame_ack.hex(" ")).upper())

while uart_port.in_waiting == 0:
    pass
    

card_detected_respond =uart_port.read(19)
print((card_detected_respond.hex(" ")).upper())