import schedule
from datetime import datetime, timedelta
from TransmitRF import transmit_code
import time

codes = {
    'one_on':'001010000111011101100001000000101',
    'one_off':'001010000111011101011110111111111',
    'two_on':'001010000111011101101101000011101',
    'two_off':'001010000111011101010010111100111',
    'three_on':'001010000111011101100101000001101',
    'three_off':'001010000111011101011010111110111',
    'four_on':'001010000111011101100011000001001',
    'four_off':'001010000111011101011100111111011',
    'five_on':'001010000111011101101011000011001',
    'five_off':'001010000111011101010100111101011',
}

long_delay = 0.000885
short_delay = 0.000289
long_activate = 0.000913
short_activate = 0.000309
extended_delay = 0.00443

def change_status(code):
    values = code.split('_')
    #print('Changing light {} to status {}'.format(values[0], values[1]))
    transmit_code(codes[code])

schedule.every().day.at("17:00").do(lambda: change_status('three_on'))
schedule.every().day.at("17:00").do(lambda: change_status('four_on'))
schedule.every().day.at("17:00").do(lambda: change_status('five_on'))
schedule.every().day.at("01:00").do(lambda: change_status('three_off'))
schedule.every().day.at("00:00").do(lambda: change_status('four_off'))
schedule.every().day.at("00:00").do(lambda: change_status('five_off'))

while True:
    schedule.run_pending()
    time.sleep(1)
