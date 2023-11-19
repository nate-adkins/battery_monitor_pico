# host computer code (serial_communication.py)

import serial, time 

def main():
    serial_port = '/dev/ttyACM0'  
    baud_rate = 115200  
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    while True:
        if ser.in_waiting > 0:
            received_message = ser.readline().decode('utf-8').strip()
            print(received_message)

if __name__ == "__main__":
    main()

