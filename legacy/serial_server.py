import serial
from router import process

ser = serial.Serial("COM9", 115200, timeout=1)

print("Connected!")

while True:

    command = input("\nYou > ")

    ser.write((command + "\n").encode())

    line = ser.readline().decode(errors="ignore").strip()

    print("Nano:", line)

    reply = process(command)

    print("EWA:", reply)