#!/usr/bin/env python
import rospy
import actionlib
import random
import sys
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseActionGoal
from actionlib_msgs.msg import *
import time
import roslaunch
from geometry_msgs.msg import Twist
import math
from std_msgs.msg import Int64
# from project4.msg import spawn


def rotate():
    current_angle = 0
    relative_angle = 5.0265482
    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0.8
    t0 = time.time()
    #t0 = datetime.now().microsecond
    while(current_angle < relative_angle):
        pub.publish(twist)
        t1 = time.time()
	#t1 = datetime.now().microsecond
        current_angle = 0.8*(t1-t0)
    twist.angular.z = 0
    pub.publish(twist)

def RandSpawn():
    global spawn_x
    global spawn_y
    package = 'gazebo_ros'
    executable = 'spawn_model'
    arguments = '-urdf -model jackal -param robot_description '
    spawn_location = [  '-x 0.0 -y 0.0 -z 1.0',
                        '-x 3.0 -y -4.0 -z 1.0',
                        '-x 7.0 -y 7.0 -z 1.0',
                        '-x -1.0 -y 6.0 -z 1.0']

    location = random.choice(spawn_location)
    #location = '-x 0 -y 7 -z 1.0'
    arguments += location

    #coords = [int(s) for s in location.split() if s.isdigit()]
    #spawn_x = coords[0]
    #spawn_y = coords[1]

    l = []
    for t in location.split():
	try:
	    l.append(float(t))
	except ValueError:
	    pass

    spawn_x = l[0]
    spawn_y = l[1]
    pub = rospy.Publisher('chatter', spawn, queue_size=10)
    msg=spawn()
    msg.spawnx=spawn_x
    msg.spawny=spawn_y
    rospy.loginfo(msg)
    pub.publish(msg)

    time.sleep(10)

    node = roslaunch.core.Node(package, executable, args=arguments)

    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()

    process = launch.launch(node)

    print('Spawned at ' + location)
    print(process.is_alive())

    time.sleep(3)
    process.stop()

def DestNav(x,y):
    mvbs = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    mvbs.wait_for_server()
    rospy.loginfo("server ready")
    dest = MoveBaseGoal()

    dest.target_pose.header.frame_id = "map"
    dest.target_pose.header.stamp = rospy.Time.now()

    dest.target_pose.pose.position.x = x
    dest.target_pose.pose.position.y = y
    dest.target_pose.pose.position.z = 0
    dest.target_pose.pose.orientation.x = 0.0
    dest.target_pose.pose.orientation.y = 0.0
    dest.target_pose.pose.orientation.z = 0.0
    dest.target_pose.pose.orientation.w = 1.0

    rospy.loginfo("Sending goal location ...")
    mvbs.send_goal(dest)

    mvbs.wait_for_result(rospy.Duration(100))


if __name__ == "__main__":
    try:
        rospy.init_node("test_random")
	rate = rospy.Rate(50)
	pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
	twist = Twist()

	#way_x = [3,-5,-3,-7.2,6]
	#way_y = [-4,8,3,-4.36,8]

	RandSpawn()

	rotate()

	if spawn_y < -1:
	    DestNav(6.7-spawn_x, 6.7-spawn_y)
	    DestNav(0-spawn_x, 0-spawn_y)
	    DestNav(6.7-spawn_x, 6.7-spawn_y)
	    DestNav(-5-spawn_x, 8-spawn_y)
            DestNav(-6-spawn_x, 3-spawn_y)
	    DestNav(-7.2-spawn_x,-4.36-spawn_y)
            DestNav(6-spawn_x, -8-spawn_y)
	else:
	    DestNav(6.7-spawn_x, 6.7-spawn_y)
	    DestNav(4-spawn_x, -4-spawn_y)
	    DestNav(6.7-spawn_x, 6.7-spawn_y)
            DestNav(0-spawn_x, 0-spawn_y)
            DestNav(6.7-spawn_x, 6.7-spawn_y)
            DestNav(-5-spawn_x, 8-spawn_y)
            DestNav(-6-spawn_x, 3-spawn_y)
            DestNav(-7.2-spawn_x,-4.36-spawn_y)
            DestNav(6-spawn_x, -8-spawn_y)

    except rospy.ROSInterruptException:
	pass
