#!/usr/bin/env python

import rospy
import random
import sys
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time
import math
from datetime import datetime

def scan_callback(msg):
    global closest_range
    global maximum_range
    global complete_range

    closest_range = min(msg.ranges)
    complete_range = msg.ranges
    maximum_range = max(msg.ranges)
    print("Got the values!")


if __name__ == "__main__":
    closest_range = 1.0
    complete_range = []
    try:
        rospy.init_node("rand")
        rospy.Subscriber("/scan", LaserScan, scan_callback)
        rate = rospy.Rate(50)
        twist = Twist()
        lasermsg = LaserScan()
        while not rospy.is_shutdown():
           # print(twist.linear.x)
           # print(min(lasermsg.ranges))
           print(closest_range)
        # print(max(LaserScan.ranges))
    except rospy.ROSInterruptException:
        pass
