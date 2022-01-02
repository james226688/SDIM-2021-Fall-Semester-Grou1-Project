import RobotArmMotion0
import time

RobotArmMotion0.Reset0()
time.sleep(3)
RobotArmMotion0.Test1()
time.sleep(3)
RobotArmMotion0.CatchAndRelease(1)
time.sleep(3)
RobotArmMotion0.Release()
time.sleep(3)
RobotArmMotion0.CatchAndRelease(0)
time.sleep(3)
RobotArmMotion0.Reset1()