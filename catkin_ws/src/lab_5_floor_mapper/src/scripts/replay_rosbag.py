#!/usr/bin/env python
#Credits: Credits for the intial version of the python script reused for this project goes to Project 4 Group 1 members. Surya, James and Derek.

#EE5900: Intro to Robotics
#Lab 5: Working with Jackal

#Group 1:
#  Roger Gomes (Team Lead)
#  Sabari Manohar
#  Deep Doshi

#Description of Changes: Changes in this script has been done to save the map and read the bag file from appropriate package directories.


# -------------------------Description:-------------------------
# Replay script to play back the bag file and save a map.
#
#
# |-Intro to Robotics - EE5900 - Spring 2017
#   |-Assignment #4
#     |-Project #4 Group #1
#       |-Surya (Team Lead)
#       |-James
#       |-Derek

import rospy
import roslaunch
from random import randint
import time
import os

#function that runs the map saver. Saves the map to the maps folder under the new
#name newMap
def save():
   package ='map_server'
   executable ='map_saver'

   node = roslaunch.core.Node(package, executable, args="-f "+str(os.path.dirname(os.path.realpath(__file__)))[:-7]+"maps/mapped_floor")


   launch = roslaunch.scriptapi.ROSLaunch()
   launch.start()

   process = launch.launch(node)
   while process.is_alive():
       print process.is_alive()

#function that replays the bag file
def replay():

    package ='rosbag'
    executable ='play'

    node = roslaunch.core.Node(package, executable, args=str(os.path.dirname(os.path.realpath(__file__)))[:-7]+"bags/scanned.bag")

    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()

    process = launch.launch(node)
    while process.is_alive():
        print process.is_alive()


if __name__ == '__main__':
    try:
        rospy.init_node('replay', anonymous=False)
	replay()	#replay bag file
        save()	#save the new map

    except rospy.ROSInterruptException:
        rospy.loginfo("map_navigation node terminated.")
