#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>

#include <chrono>

using namespace std::chrono_literals;

class SimplePublisher : public rclcpp::Node {
public:
    SimplePublisher() 
    : Node("simple_publisher"), counter_(0) {
        publisher_ = create_publisher<std_msgs::msg::String>("chatter", 10);
        timer_ = create_wall_timer(
            1s, std::bind(&SimplePublisher::publishMessage, this)
        );
        RCLCPP_INFO(get_logger(), "Publisher initialized at 1 Hz");
    }

private:
    void publishMessage() {
        std_msgs::msg::String message;
        message.data = "Hello ROS 2 : " + std::to_string(counter_++);
        publisher_->publish(message);
    }

    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    unsigned int counter_;
};

int main(int argc, char* argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<SimplePublisher>());
    rclcpp::shutdown();
    return 0;
}