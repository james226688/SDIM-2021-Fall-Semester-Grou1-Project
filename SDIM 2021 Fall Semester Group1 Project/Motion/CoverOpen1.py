import SteeringEngine0
import Sensor0
import time
import Audioplay1
import AudioPig
#三个口分别是红外(18)上口(14)下口(15)

def BigMouth():
    while True:
        i = Sensor0.SensorInf(18) #GPIO need to change
        print(i)
        if i == 1:
            print("User Detected")
            Audioplay1.Playmusic()
            SteeringEngine0.Rotate(14,35)
            SteeringEngine0.Rotate(14,35)
            SteeringEngine0.Rotate(14,11)
            SteeringEngine0.Rotate(14,11)
            time.sleep(2)
            Audioplay1.Playmusic()
            time.sleep(5)
            Audioplay1.Playmusic()
            time.sleep(5)
            Audioplay1.Playmusic()
            time.sleep(5)
            Audioplay1.Playmusic()
            time.sleep(5)
            Audioplay1.Playmusic()
            time.sleep(5)
            Audioplay1.Playmusic()
            SteeringEngine0.Rotate(14,35)
            SteeringEngine0.Rotate(14,35)
            time.sleep(4)
            AudioPig.AudioPig12()
            time.sleep(5)#90

            SteeringEngine0.Rotate(15,35) 
            SteeringEngine0.Rotate(15,35)
            SteeringEngine0.Rotate(15,11) 
            SteeringEngine0.Rotate(15,11)
            time.sleep(5)
            SteeringEngine0.Rotate(15,35) 
            SteeringEngine0.Rotate(15,35)
            break