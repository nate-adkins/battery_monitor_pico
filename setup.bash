# cp RPI_PICO-20231005-v1.21.0.uf2 /media/$USER/RPI-RP2
ampy --port /dev/ttyACM0 put main.py 
ampy --port /dev/ttyACM0 run main.py 
