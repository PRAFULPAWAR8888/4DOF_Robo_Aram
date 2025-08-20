import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rcl_interfaces.msg import SetParametersResult


class SimpleParameter(Node):
    def __init__(self):
        super().__init__('simple_parameter_node')

        # Declare parameters
        self.declare_parameter("simple_int_param", 28)
        self.declare_parameter("simple_string_param", "Praful")

        # Register callback for parameter change
        self.add_on_set_parameters_callback(self.on_set_parameters)

    def on_set_parameters(self, params):
        result = SetParametersResult()
        result.successful = True

        for param in params:
            if param.name == "simple_int_param" and param.type_ == Parameter.Type.INTEGER:
                self.get_logger().info(f"Integer parameter changed to: {param.value}")
            elif param.name == "simple_string_param" and param.type_ == Parameter.Type.STRING:
                self.get_logger().info(f"String parameter changed to: {param.value}")

        return result


def main():
    rclpy.init()
    node = SimpleParameter()
    rclpy.spin(SimpleParameter)
    SimpleParameter.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
