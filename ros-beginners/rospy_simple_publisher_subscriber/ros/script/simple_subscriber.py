#!/usr/bin/env python
"""
This script is a simple python node which subscribes to
rospy_pub_sub/event_out topic
"""
#-*- encoding: utf-8 -*-
__author__ = 'mohammad wasil'

import rospy
from std_msgs.msg import String

def pub_sub_callback(msg):
    rospy.loginfo("Data yang diterima: %s", msg.data)

if __name__ == '__main__':
    '''
    Initilize node and string type publish topic at the loop rate of 10Hz.
    '''
    
    rospy.init_node("rospy_simple_subscriber_node", anonymous=False)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        rospy.Subscriber("rospy_pub_sub/event_out", String, pub_sub_callback)
        
        rate.sleep()

