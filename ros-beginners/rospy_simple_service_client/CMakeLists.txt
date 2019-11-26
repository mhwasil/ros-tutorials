cmake_minimum_required(VERSION 2.8.3)
project(rospy_simple_service_client)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  ros_custom_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES rospy_simple_service_client
#  CATKIN_DEPENDS roscpp rospy
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

