import time
import sys
import RPi.GPIO as GPIO

one_on =  '001010000111011101100001000000101'
one_off = '001010000111011101011110111111111'
two_on =  '001010000111011101101101000011101'
two_off = '001010000111011101010010111100111'
three_on =  '001010000111011101100101000001101'
three_off = '001010000111011101011010111110111'
four_on =  '001010000111011101100011000001001'
four_off = '001010000111011101011100111111011'
five_on =  '001010000111011101101011000011001'
five_off = '001010000111011101010100111101011'

long_delay = 0.000885
short_delay = 0.000289
long_activate = 0.000913
short_activate = 0.000309
extended_delay = 0.00443

NUM_ATTEMPTS = 10
TRANSMIT_PIN = 13

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    for t in range(NUM_ATTEMPTS):
        for i in code:
            if i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(short_activate)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(long_delay)
            elif i == '0':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(long_activate)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(short_delay)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(extended_delay)
    GPIO.cleanup()

if __name__ == '__main__':
    #for argument in sys.argv[1:]:
        #exec('transmit_code(' + str(argument) + ')')
    transmit_code(four_off)
