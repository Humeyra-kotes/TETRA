#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RemoteControllerNode(Node): #1
    def __init__(self):
        super().__init__("remote_controller_node") #2
        self.subscriber_ = self.create_subscription(String, "channel_something", 
                                                    self.callback_television,10)
        self.get_logger().info("Remote controller has been subscribed !")
        
    def callback_television(self,msg):
        self.get_logger().info(msg.data)

def main (args=None):
    rclpy.init(args=args)
    node=RemoteControllerNode() # 3
    rclpy.spin(node)
    rclpy.shutdown()



if __name__ == "__main__":
    main()
