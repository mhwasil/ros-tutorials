cmake_minimum_required(VERSION 2.8.3)
project(ros_custom_msgs)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  std_msgs
  message_generation
)

#add_action_files(DIRECTORY action
#   FILES
#     DetectScene.action
#)
 
#add_message_files(
#   FILES
#	    contoh_msg.msg
#)

# Generate services in the 'srv' folder
add_service_files(
  FILES
    CountWords.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
    std_msgs  # Or other packages containing msgs
)

# Define that it's a catkin package So that it can be found by pkg 
# that is dependent on this package
catkin_package(
  CATKIN_DEPENDS
    message_runtime
)
