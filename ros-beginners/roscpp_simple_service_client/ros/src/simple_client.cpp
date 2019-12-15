#include <ros/ros.h>
#include <ros_custom_msgs/CountWords.h>

int main (int argc, char **argv)
{
  ros::init(argc, argv, "roscpp_simple_client_node");
  ros::NodeHandle nh;
  ros::ServiceClient service_client = nh.serviceClient<ros_custom_msgs::CountWords>("roscpp_word_count");
  ros::Rate loop_rate(10);
  while(ros::ok())
  {
    ros_custom_msgs::CountWords srv;
    srv.request.words.data = "A sample request from a client for a simple service client test";
    srv.request.count_articles.data = true;

    if (service_client.call(srv))
    {
      ROS_INFO_STREAM("Result -> Num of words: "<<srv.response.num_words.data);
      ROS_INFO_STREAM("Result -> Num of articles: "<<srv.response.num_articles.data);
    }
    else
    {
      ROS_ERROR("Failed to call the service server");
    }

    loop_rate.sleep();
  }
  return 0;
}
