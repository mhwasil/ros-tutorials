#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "roscpp_simple_publisher_node");
  ros::NodeHandle nh;
  ros::Publisher publisher = nh.advertise<std_msgs::String>("roscpp_pub_sub/event_out", 1);
  ros::Rate loop_rate(10);
  while(ros::ok())
  {
    std_msgs::String msg;
    msg.data = "Kiriman data dari node roscpp_simple_publisher_node";
    publisher.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
    
  }

  return 0;

}
