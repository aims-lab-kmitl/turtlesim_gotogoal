#!/usr/bin/env python3
import cmd
import math
from re import T
from turtle import distance
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2, sqrt, pow, pi
import time

cmd_vel_angular_ = Twist()
cmd_vel_linear_ = Twist()
turtle_pose_ = Pose()

def commandPostitionCallback(position):
    global turtle_pose_
    turtle_pose_ = position

def gotogoal(x, y):
    global cmd_vel_linear_, cmd_vel_angular_

    displacement = sqrt(pow(turtle_pose_.x - x, 2) + pow(turtle_pose_.y - y, 2))
    angular = atan2(abs(turtle_pose_.y - y), abs(turtle_pose_.x - x))

    if x > turtle_pose_.x :
        if y >= turtle_pose_.y :
            angular = angular
        else :
            angular = -1 * angular
    else :
        if y >= turtle_pose_.y :
            angular = pi - angular
        else :
            angular = (-1 * pi) + angular

    cmd_vel_angular_.angular.z = angular - turtle_pose_.theta
    cmd_vel_linear_.linear.x = displacement

    print("x: %f y: %f displacement: %f angular: %f" % (x, y, cmd_vel_linear_.linear.x, cmd_vel_angular_.angular.z))
    

def main():
    rospy.init_node('turtlesim_gotogoal_node', anonymous=True)
    rate = rospy.Rate(10)

    cmd_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    tuetle_pose_sub = rospy.Subscriber('/turtle1/pose', Pose, commandPostitionCallback)

    while not rospy.is_shutdown():
        time.sleep(3)
        gotogoal(5, 5)
        cmd_vel_pub.publish(cmd_vel_angular_)
        time.sleep(2)
        cmd_vel_pub.publish(cmd_vel_linear_)
        time.sleep(3)

        gotogoal(9, 5)
        cmd_vel_pub.publish(cmd_vel_angular_)
        time.sleep(2)
        cmd_vel_pub.publish(cmd_vel_linear_)
        time.sleep(3)

        gotogoal(6.5, 9.6)
        cmd_vel_pub.publish(cmd_vel_angular_)
        time.sleep(2)
        cmd_vel_pub.publish(cmd_vel_linear_)
        time.sleep(3)

        gotogoal(1.7, 8.5)
        cmd_vel_pub.publish(cmd_vel_angular_)
        time.sleep(2)
        cmd_vel_pub.publish(cmd_vel_linear_)
        time.sleep(3)

        gotogoal(5, 5)
        cmd_vel_pub.publish(cmd_vel_angular_)
        time.sleep(2)
        cmd_vel_pub.publish(cmd_vel_linear_)
        time.sleep(3)
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInitException:
        pass

