#!/usr/bin/env python

"""
This script is a simple python node which advertizes ros service
server rospy_word_count
"""
#-*- encoding: utf-8 -*-
__author__ = 'mohammad wasil'

import rospy
from ros_custom_msgs.srv import CountWords, CountWordsResponse

def server_callback(req):
  rospy.loginfo("Received request: %s", req.words.data)
  
  words = req.words.data.split(" ")
  resp = CountWordsResponse()

  if req.count_articles.data:
    english_articles = ['a', 'an', 'the'] 
    resp.num_articles.data = len([word for word in words if word in english_articles])

  resp.num_words.data = len(words) - resp.num_articles.data

  return resp

if __name__ == '__main__':
  rospy.init_node("rospy_simple_server_node", anonymous=False)
  rospy.Service("rospy_word_count", CountWords, server_callback)  
  rospy.spin()
