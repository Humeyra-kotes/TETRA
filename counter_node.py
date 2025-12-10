#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class CounterNode(Node): #1
    def __init__(self):
        super().__init__("counter_node") #2
        self.counter_= 0
        self.create_timer(1,self.timer_callback)

    def timer_callback(self):
        # counter = counter+1
        self.counter_+=1
        self.get_logger().info("Hello World - "+str(self.counter_))

def main(args=None):
    rclpy.init(args=args)
    node = CounterNode() # 3
    rclpy.spin(node)
    rclpy.shutdown()



if __name__ == "__main__":
    main()
 