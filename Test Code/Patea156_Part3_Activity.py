'''
DP-2 Activity (Part 3 - Interfacing Muscle Sensor Emulator and Turtle Graphics)
'''
'''
Aryan Patel
Patea156
Nov 3, 2020
Lab B
Thurs 61
T-09
'''
## Import the MuscleGUILib, turtle, and time modules
from MuscleGUILib import *
import turtle
import time

'''
Initialize an object of EMGSim() from the MuscleGUILib module
'''
emg = EMGSim()

## Write code below this line

'''
Initialize the drawing board
Set the background color to "white"
Title the window "Turtle Graphics"
Set the size of the window to 700x700 pixels
'''

def control_gripper():#control the effector to pick up or drop off
    time.sleep(2)
    threshold = 0.5  #threshold
    action = 0      #set a variable, in the while loop below, the user must control the gripper to close/open to stop the while loop
    while action != 1: #after user do 1 action, the while loop will stop
        emg.update()#to keep obtain the lastest value from the sensor 
        time.sleep(0.25)
        eng.leftArm = arm.emg_left()
        eng.rightArm = arm.eng_right()
        if eng.leftArm > threshold and eng.rightArm < threshold: #only left arm flex, the gripper will close
            arm.control_gripper(45)#close the gripper
            action +=1 #the variable =1 so that the while loop will stop
        elif eng.rightArm > threshold and eng.leftArm < threshold:#only the left arm flex, the gripper will open
            arm.control_gripper(-45)#open the gripper
            action +=1#the variable =1 so that the while loop will stop
    time.sleep(2)









