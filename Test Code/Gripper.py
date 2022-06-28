'''

'''
import time
import sys
sys.path.append('../')

from Common_Libraries.p2_lib import *

import os
from Common_Libraries.repeating_timer_lib import repeating_timer

def update_sim ():
    try:
        arm.ping()
    except Exception as error_update_sim:
        print (error_update_sim)

arm = qarm()

update_thread = repeating_timer(2, update_sim)
## Import the MuscleGUILib, turtle, and time modules
from MuscleGUILib import *


'''
Initialize an object of EMGSim() from the MuscleGUILib module
'''
emg = EMGSim()

## Write code below this line

def control_gripper():#control the effector to pick up or drop off
    time.sleep(2)
    threshold = 0.5  #threshold
    action = 0      #set a variable, in the while loop below, the user must control the gripper to close/open to stop the while loop
    while action != 1: #after user do 1 action, the while loop will stop
        emg.update()#to keep obtain the lastest value from the sensor 
        time.sleep(0.25)
        emg.leftArm = arm.emg_left()
        emg.rightArm = arm.emg_right()
        if emg.leftArm > threshold and emg.rightArm < threshold: #only left arm flex, the gripper will close
            arm.control_gripper(45)#close the gripper
            action +=1 #the variable =1 so that the while loop will stop
        elif emg.rightArm > threshold and emg.leftArm < threshold:#only the left arm flex, the gripper will open
            arm.control_gripper(-45)#open the gripper
            action +=1#the variable =1 so that the while loop will stop
    time.sleep(2)
