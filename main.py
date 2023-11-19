# pico computer 

import machine
import utime

# Initialize USB Serial

# NOT USED - PRINTING GOES OVER SERIAL PORT ANYWAYS 
usb_serial = machine.UART(0, baudrate=115200)

def main():
    n = '-'
    while True:
        n += '-'
        print(n)
        utime.sleep(1)

if __name__ == "__main__":
    main()
