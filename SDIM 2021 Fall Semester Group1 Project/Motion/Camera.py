import os
import sys
import re

#sudo mplayer tv://
b = "image.jpg"
a=os.system("fswebcam --no-banner -r 640x480 " + b +".jpg")
#a=os.system("fswebcam --no-banner -r 640x480 image.jpg")
#a=os.system("fswebcam --no-banner -r 640x480 /home/pi/Desktop/image3.jpg")
print (a)
