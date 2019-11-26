cmake_minimum_required(VERSION 2.8.3)
project(roscpp_simple_publisher_subscriber)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)

catkin_package(
  LIBRARIES ${PROJECT_NAME}
  CATKIN_DEPENDS 
    roscpp 
    std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)


## Mark executables for installation
add_executable(simple_publisher_node
  ros/src/simple_publisher.cpp
)

target_link_libraries(simple_publisher_node
  ${catkin_LIBRARIES} 
)

add_dependencies(simple_publisher_node
  ${catkin_EXPORTED_TARGETS}
)

add_executable(simple_subscriber_node
  ros/src/simple_subscriber.cpp
)

target_link_libraries(simple_subscriber_node
  ${catkin_LIBRARIES} 
)

add_dependencies(simple_subscriber_node
  ${catkin_EXPORTED_TARGETS}
)
