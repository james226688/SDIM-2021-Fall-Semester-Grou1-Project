import os
import time
import sys
import re

i = 27
while(True):
    a = str(i)
    b = os.system("fswebcam --no-banner -r 640x480 /home/pi/Desktop/Photo/" + a +".jpg")
    time.sleep(5)
    i = i + 1







#