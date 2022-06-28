import random
from MuscleGUILib import *
emg = EMGSim()
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
######################################################
#this function is purely used as a primary step to determine the locations of bins
#it was used only to determine locations and is not called anywhere else in the code
threshold = 0.5 #threshold value defined globally for use in EMG functions
#Aryan Patel
def get_locations(): # get location of both the large and small bins 
    small_positions = [] # empty list for the small and large bins
    large_positions = []
    arm.home()
    time.sleep(3)
    arm.open_green_autoclave(True) # open bins
    arm.open_red_autoclave(True)
    arm.open_blue_autoclave(True)
    
    for i in range(1,4): # iterate through for the 3 small locations
        arm.home()
        time.sleep(3) # sleep for the first few seconds to slow down arm
        deg =[-90, 158,90]
        arm.control_gripper(45)
        time.sleep(1)
        arm.rotate_base(deg[i-1]) #the degree for each of the locations
        time.sleep(2)
        arm.rotate_elbow(-47) # rotate elbow
        time.sleep(2)
        arm.rotate_shoulder(46) # rotate shoulder
        time.sleep(2)
        arm.control_gripper(-45)
        time.sleep(2)
        if i == 1:
            print("Green Location: " , arm.effector_position())
            small_positions.append(arm.effector_position()) #add the location to the small position list
            
        if i == 2:
            print("Red Location: " , arm.effector_position())
            small_positions.append(arm.effector_position()) #add location to small positions list
        if i ==3:
            print("Blue Location: " , arm.effector_position())
            small_positions.append(arm.effector_position()) #add location to small positions list
        arm.home()

    for i in range(1,4): # iterate through for 3 large locations
        arm.home()
        time.sleep(2)
        deg =[-90, 158,90]
        arm.control_gripper(45) #open gripper
        time.sleep(1)
        arm.rotate_base(deg[i-1]) #rotate for each location
        time.sleep(2)
        arm.rotate_shoulder(21) # move shoulder
        time.sleep(2)
        arm.rotate_elbow(18) # move elbow
        time.sleep(2)
        arm.control_gripper(-45)
        time.sleep(2)
        if i == 1:
            print("Large Green Location: " , arm.effector_position()) # add locations to the large positoin list
            large_positions.append(arm.effector_position())
            
        if i == 2:
            print("Large Red Location: " , arm.effector_position()) # add location to the large positions list
            large_positions.append(arm.effector_position())
        if i ==3:
            print("Large Blue Location: " , arm.effector_position()) # add location to the large positions list
            large_positions.append(arm.effector_position())
        arm.home()
        arm.open_green_autoclave(False) # close bins
        arm.open_red_autoclave(False)
        arm.open_blue_autoclave(False)
    return small_positions,large_positions #return the list with small postions and large postions


#Aryan Patel
def get_final_postions(shape): #this function will return locations given container id when called on in the other functions
    small_positions = [[-0.6139,0.248,0.3811],[0.0,-0.6621,0.3811],[0.0,0.6621,0.3811]]
    large_positions = [[-0.411,0.1661,0.2032],[0.0,-0.4433,0.2032],[0.0,0.4433,0.2032]] 
    if shape ==1: #when container id is passed the function will return its location depending on id 
        return small_positions[0]
    if shape==2: #repeats for every id and index in list
        return small_positions[1]
    if shape==3:
        return small_positions[2]
    if shape==4:
        return large_positions[0]
    if shape==5:
        return large_positions[1]
    if shape==6:
        return large_positions[2]
#Feichen Zhou
def control_gripper_close():#control the effector to pick up
    time.sleep(2)
    
    action = 0      #set a variable, in the while loop below, the user must control the gripper to close/open to stop the while loop
    while action != 1: #after user do 1 action, the while loop will stop
        emg.update()#to keep obtain the lastest value from the sensor 
        time.sleep(0.25)
        emg_leftArm = arm.emg_left() #get value for both arms
        emg_rightArm = arm.emg_right()
        if emg_leftArm > threshold and emg_rightArm == 0: #only LEFT ARM flex, the gripper will close
            arm.control_gripper(45)#close the gripper
            action +=1 #the variable =1 so that the while loop will stop
    time.sleep(2)
#Feichen Zhou 
def control_gripper_open():#control the effector to pick up or drop off
    time.sleep(2)
    
    action = 0      #set a variable, in the while loop below, the user must control the gripper to close/open to stop the while loop
    while action != 1: #after user do 1 action, the while loop will stop
        emg.update()#to keep obtain the lastest value from the sensor 
        time.sleep(0.25)
        emg_leftArm = arm.emg_left() #get value for both arms
        emg_rightArm = arm.emg_right()
        if emg_rightArm == 0 and emg_leftArm > threshold:#only the LEFT ARM is flexed, the gripper will open
            arm.control_gripper(-45)#open the gripper
            action +=1#the variable =1 so that the while loop will stop
    time.sleep(2)

#Feichen Zhou
def go_pickup_container():
    start_position=[0.5304, 0.0, 0.0257]
    
    action = 0      #set a variable, in the while loop below, the user must control the gripper to close/open to stop the while loop
    while action != 1: #after user do 1 action, the while loop will stop
        emg.update()#to keep obtain the lastest value from the sensor 
        time.sleep(0.25)
        emg_leftArm = arm.emg_left() #get value for both arms
        emg_rightArm = arm.emg_right()
        if emg_leftArm > threshold and emg_rightArm > threshold: #if BOTH ARMS are flexed go to pickup container
            arm.move_arm(start_position[0],start_position[1],start_position[2])
            action +=1 #the variable =1 so that the while loop will stop
    time.sleep(2)
    
#Aryan Patel/Feichen Zhou
def go_target_position(shape):
    
    action = 0      #set a variable, in the while loop below, the user must control the gripper to close/open to stop the while loop
    if shape == 1 or shape == 2 or shape == 3:
        target_position = get_final_postions(shape) #go to positions for smaller container id
    if shape == 4 or shape == 5 or shape == 6:
        target_position = get_final_postions(shape) #position for larger container id
    while action != 1: #after user do 1 action, the while loop will stop
        emg.update()#to keep obtain the lastest value from the sensor 
        time.sleep(0.25)
        emg_leftArm = arm.emg_left() #get value for both arms
        emg_rightArm = arm.emg_right()
        if emg_leftArm > threshold and emg_rightArm > threshold: #go to target position if BOTH ARMS are flexed
            arm.move_arm(target_position[0],target_position[1],target_position[2])
            action +=1 #the variable =1 so that the while loop will stop
    time.sleep(2)
    
#Feichen Zhou
def open_autoclave(shape):
    
    action = 0      #set a variable, in the while loop below, the user must control the gripper to close/open to stop the while loop
    while action != 1: #after user do 1 action, the while loop will stop
        emg.update()#to keep obtain the lastest value from the sensor 
        time.sleep(0.25)
        emg_leftArm = arm.emg_left() #get value for both arms
        emg_rightArm = arm.emg_right()
        if emg_leftArm ==0 and emg_rightArm > threshold: #only RIGHT ARM is flexed open the corresponding autoclave bin given container id
            if shape == 4:
                arm.open_red_autoclave(True)
                action +=1 #the variable =1 so that the while loop will stop
            elif shape == 5:
                arm.open_green_autoclave(True)
                action +=1 #the variable =1 so that the while loop will stop
            elif shape ==6:
                arm.open_blue_autoclave(True)
                action +=1 #the variable =1 so that the while loop will stop
    time.sleep(2)
    
#Feichen Zhou
def close_autoclave(shape):
   
    action = 0      #set a variable, in the while loop below, the user must control the gripper to close/open to stop the while loop
    while action != 1: #after user do 1 action, the while loop will stop
        emg.update()#to keep obtain the lastest value from the sensor 
        time.sleep(0.25)
        emg_leftArm = arm.emg_left() #get value for both arms
        emg_rightArm = arm.emg_right()
        if emg_leftArm == 0 and emg_rightArm > threshold: #if only RIGHT ARM is flexed close bin 
            if shape == 4:
                arm.open_red_autoclave(False)
                action +=1 #the variable =1 so that the while loop will stop
            elif shape == 5:
                arm.open_green_autoclave(False)
                action +=1 #the variable =1 so that the while loop will stop
            elif shape ==6:
                arm.open_blue_autoclave(False)
                action +=1 #the variable =1 so that the while loop will stop
    time.sleep(2)
    
#Aryan Patel/Feichen Zhou
def Move_endEffector(shape):
    if shape == 1 or shape == 2 or shape == 3: #given the id is for a small container
        target_position = get_final_postions(shape) #go to positons returned by location function
        go_pickup_container() #call function to pickup container
        time.sleep(2)
        control_gripper_close() #call close gripper function
        arm.move_arm(0.4064,0.0,0.4826)#home position
        time.sleep(2)
        go_target_position(shape) #call function and pass container id 
        control_gripper_open() #call open gripper function
        arm.home()
    if shape == 4 or shape == 5 or shape == 6: #given id is for a large container
        target_position = get_final_postions(shape) #go to drop off location
        go_pickup_container()
        time.sleep(2)
        control_gripper_close()
        arm.move_arm(0.4064,0.0,0.4826)#home position
        time.sleep(2)
        open_autoclave(shape) #open bin corresponding to id of container
        time.sleep(2)
        go_target_position(shape)
        time.sleep(2)
        control_gripper_open()
        arm.home()
        time.sleep(2)
        close_autoclave(shape) #call function to close the bin corresponding to container id
        
#main program below
#Aryan Patel/Feichen Zhou
def main():
    inventory= [1,2,3,4,5,6] #inventory of the id of each container
    random.shuffle(inventory) #go through and shuffle inventory for random order


    for shape in inventory: #iterate through new shuffled list to store containers
        
        arm.spawn_cage(shape) #calling functions that control arm
        time.sleep(2)
        Move_endEffector(shape)
        time.sleep(2)
        
    print("All six containers are placed!") 

main() #call main function for the container placement cycle
