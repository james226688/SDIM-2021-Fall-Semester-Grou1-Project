import CoverOpen1
import TrashMotion0
import ExpansionLink1
import time
def Combine():
    print("CoverOpen1 starts!")
    CoverOpen1.BigMouth()
    print("CoverOpen1 finishes!")
    time.sleep(10)#90
    print("TreashMotions starts!")
    TrashMotion0.GreenMove1()
    print("TreashMotions finishes!")
    print("Wait for RobotArm")
    time.sleep(10)#90
    print("Keep going!")
    TrashMotion0.GreenMove3()
    time.sleep(3)
    TrashMotion0.RedMove1()
    time.sleep(10)
    ExpansionLink1.Loop(2)
    time.sleep(3)
    TrashMotion0.RedMove3()
    print("Finish!")

Combine()
