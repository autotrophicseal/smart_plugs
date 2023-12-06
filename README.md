# smart_plugs
Automated Christmas lights with Raspberry pi

Started by installing raspbian OS on my raspberry pi 4
Installed headless

## Sniffing Codes

Followed the tutorial from https://www.instructables.com/Super-Simple-Raspberry-Pi-433MHz-Home-Automation/ at first. Need a way to know the bits that get sent from the remote to the smart plug so I can mimic it with my transmitter. To do so use a 433mgh reciever and run the code that the link provides.

#### Login to pi via ssh
- ssh pi@____________

#### Prepping files for running
- create github repo and clone onto separate computer
- download all code to it and push to repo
- clone repo onto raspberry pi
- I cloned into the desktop folder idk why.
- Had to modify the print statements. For some reason the author of the code didn't correctly utilize parentheses?
- Matplotlib not installed on raspberry pi
- Tutorial said to run the following command

sudo apt-get install python-matplotlib

- This didn't work. However I changed python to python3 and only then did it run.

#### Running the code

- python ReceiveRF.py
- Generated plots. Didn't get the plots I needed (stuck at 1) so I tried a different receiever
- Still didn't get it. Turns out author had set pin numberings to BCM rather than BOARD
- changed to GPIO.setmode(GPIO.BOARD) bc I don't feel like learning numberings for bcm

Ended up getting actual data but needed to go and hook up pi to monitor so I could simply show fig and zoom in on it.
Got some good plots. Data is as follows for mine:

- 1 ON:  001010000111011101100001000000101
- 1 OFF: 001010000111011101011110111111111
- 2 ON:  001010000111011101101101000011101
- 2 OFF: 001010000111011101010010111100111
- 3 ON:  001010000111011101100101000001101
- 3 OFF: 001010000111011101011010111110111
- 4 ON:  001010000111011101100011000001001
- 4 OFF: 001010000111011101011100111111011
- 5 ON:  001010000111011101101011000011001
- 5 OFF: 001010000111011101010100111101011

Also got timing information. Stored separatelyl

I suppose you can drive past my house and mess with the christmas lights now. Congrats!

## Sending Codes

Modified the Transmit RF file to send the data I just captured. Had to tweak the timing for some of the delay's and activations but it was worth it because it works now.

## Scheduling

Utilized pythons Scheduling package to time the turning on and off of the plugs. Ran run_lights.py via ssh with nohup (i think) to ensure program continued to run despite killing of ssh terminal.


Seems to have worked so far!









