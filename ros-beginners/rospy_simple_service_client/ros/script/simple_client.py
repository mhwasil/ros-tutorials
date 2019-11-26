#!/usr/bin/env python

"""
This script is a simple python node which calls ros service
rospy_word_count and send request to the server.
"""
#-*- encoding: utf-8 -*-
__author__ = 'mohammad wasil'

import rospy
from ros_custom_msgs.srv import CountWords, CountWordsRequest

if __name__ == '__main__':

  #you are not necessarilt inilitialize node
  #since service client does not have to be a node
  rospy.init_node("rospy_simple_client_node", anonymous=False)
  rate = rospy.Rate(10)

  while not rospy.is_shutdown():
    rospy.wait_for_service('rospy_word_count')
    try:
      word_count = rospy.ServiceProxy('rospy_word_count', CountWords)

      req = CountWordsRequest()
      req.words.data =  "a test from the client node for a simple server client"
      req.count_articles.data = True

      resp = word_count.call(req)

      rospy.loginfo("Result -> Num of words: %s"%resp.num_words.data)
      rospy.loginfo("Result -> Num of articles: %s"%resp.num_articles.data)

    except rospy.ServiceException, e:
      print "Service call failed: %s"%e

    rate.sleep()
