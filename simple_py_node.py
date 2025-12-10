#!/usr/bin/env python3

# 1. Library
import rclpy
from rclpy.node import Node

# 2. Method
def main(args=None):
    rclpy.init(args=args)
    node = Node("py_node")

    #print("Hello World!")
    node.get_logger().info("Hello Word!")

    rclpy.spin(node)
    rclpy.shutdown()


# 3."if___name___"block
if __name__ =="__main__":
    main()