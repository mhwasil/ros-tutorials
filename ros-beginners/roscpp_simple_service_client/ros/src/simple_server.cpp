#include <ros/ros.h>
#include <ros_custom_msgs/CountWords.h>
#include <boost/algorithm/string.hpp>

bool serverCallback(ros_custom_msgs::CountWordsRequest &req,
                    ros_custom_msgs::CountWordsResponse &resp)
{
  ROS_INFO_STREAM("Request received: "<<req.words.data);
  
  std::vector<std::string> words;
  boost::split(words, req.words.data, boost::is_any_of("\t "));
  
  std::vector<std::string> english_articles = {"a", "an", "the"};
  int num_of_articles = 0;
  for (auto const& word: words)
  {
    std::string lower_word = boost::algorithm::to_lower_copy(word);
    if (std::find(english_articles.begin(), english_articles.end(), 
        lower_word ) != english_articles.end())
    {
      num_of_articles ++;
    }
  }
  
  resp.num_articles.data = num_of_articles;
  resp.num_words.data = words.size() - num_of_articles;
  
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "roscpp_simple_server_node");
  ros::NodeHandle nh;
  ros::ServiceServer service = nh.advertiseService("roscpp_word_count", serverCallback);
  ros::spin();
  
  return 0;
}
