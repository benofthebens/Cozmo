import cozmo
import cozmo.util

def say_hello(robot: cozmo.robot.Robot):
   
    robot.drive_straight(
        distance=cozmo.util.distance_mm(50),
        speed=cozmo.util.speed_mmps(10)
     ).wait_for_completed()
cozmo.run_program(say_hello)