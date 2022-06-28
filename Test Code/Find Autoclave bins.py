'''
DP-2 Activity (Part 1 - Determine xyz coordinates for cube and sphere pick-up location)
- Commands are meant to be typed in the Python Shell
Aryan Patel
Patea156
400295849



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
## *******************************************
## DO NOT EDIT ANY OF THE CODE ABOVE THIS LINE
## *******************************************


'''Goal is to determine the location of autoclave bins
'''
"In list first is green, then red, then blue)"
def get_locations(): #function for location of autoclave
    postions = []
    arm.home()
    time.sleep(3)
    for i in range(1,4): #for three autoclaves loop 
        arm.home()
        time.sleep(3)
        deg =[-90, 158,90] #rotate according to what degree each of the autoclave is at
        arm.control_gripper(45)
        time.sleep(1)
        arm.rotate_base(deg[i-1]) #iterate through the deg list to tell arm which angle to turn with reference to 0 deg
        time.sleep(2)
        arm.rotate_elbow(-47) #bend elbow
        time.sleep(2)
        arm.rotate_shoulder(47) #bend shoulder
        time.sleep(2)
        arm.control_gripper(-45) #open gripper
        time.sleep(2)
        if i == 1: # this is the first bin it is green and it will print the location
            print("Green Location: " , arm.effector_position()) 
            positions.append(arm.effector_position())
        if i == 2: # this is the second bin it is red and it will print the location
            print("Red Location: " , arm.effector_position())
            positions.append(arm.effector_position())
        if i ==3: #this is the third bin it is blue and it will print location of the blue bin
            print("Blue Location: " , arm.effector_position())
           positions.append(arm.effector_position()) 
            
        arm.home()
    return positions

    
    












