import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")
        self.pub_ = self.create_publisher(String, "chatter", 10)
        self.counter_ = 0
        self.frequency_ = 1.0  # Hz
        self.get_logger().info("Publishing at %.1f Hz" % self.frequency_)
        self.timer_ = self.create_timer(1.0 / self.frequency_, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = "Hello ROS 2 - counter: %d" % self.counter_
        self.get_logger().info(msg.data)
        self.pub_.publish(msg)
        self.counter_ += 1

def main():
    rclpy.init()
    node = SimplePublisher()  # ✅ Avoid reusing class name
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
