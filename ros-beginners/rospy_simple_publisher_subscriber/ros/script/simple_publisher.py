#!/usr/bin/env python
"""
This script is a simple python node which publishes
a std_msgs string.
"""
#-*- encoding: utf-8 -*-
__author__ = 'mohammad wasil'

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    '''
    Initilize node and string type publish topic at the loop rate of 10Hz.
    '''
    
    rospy.init_node("rospy_simple_publisher_node", anonymous=False)
    rate = rospy.Rate(10)
    pub = rospy.Publisher("rospy_pub_sub/event_out", String, queue_size=1)
    
    while not rospy.is_shutdown():
        string_msg = "Kiriman data dari rospy_simple_publisher_node"
        pub.publish(string_msg)
        rate.sleep()

