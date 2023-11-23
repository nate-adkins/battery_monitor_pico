# pico computer 

from machine import Pin, UART
import utime, _thread

# Initialize USB Serial

def main():


    def flash_led():

        led_pin = Pin(25, Pin.OUT)

        def dash():
            led_pin.value(1)
            utime.sleep_ms(400)
            led_pin.value(0)
            utime.sleep_ms(100)

        def dot():
            led_pin.value(1)
            utime.sleep_ms(100)
            led_pin.value(0)
            utime.sleep_ms(400)

        def space():
            utime.sleep_ms(500)

        while True:
            morse_message = '--. --- --- -.. ' # morse code "GOOD"
            for char in morse_message:
                if char == '-':
                    dash()
                elif char == '.':
                    dot()
                elif char == ' ':
                    space()


    # _thread.start_new_thread(flash_led, ())

    tx_pin = Pin(0)
    rx_pin = Pin(1)

    print(Pin(0))

    usb_serial = UART(0, 115200)
    usb_serial.init(baudrate=115200, bits=8, parity=None, stop=1, tx=tx_pin, rx=rx_pin) # init with given parameter
    n = True
    while True:
        usb_serial.write('n')
        # print(n)
        utime.sleep(1)
        n = not n 


if __name__ == "__main__":
    main()