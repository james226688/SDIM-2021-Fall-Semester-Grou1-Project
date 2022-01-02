import Motion0
import time

def Loop(number):
    for x in range(number):
        Motion0.MotionMove(17,27,22,0,18,100)
        time.sleep(3)
        Motion0.MotionMove(17,27,22,1,16,100)
        time.sleep(1)
