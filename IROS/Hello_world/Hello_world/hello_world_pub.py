import rclpy 
from rclpy.node import Node

import time

from std_msgs.msg import String

class Hello_World_Pub(Node):
     def __init__(self):
        super().__init__('HW_pub_node')

        self.hw_pub = self.create_publisher(String, 'HW_topic', 10)
        self.create_timer(1.0, self.__pub_timer)

     def __pub_timer(self):
         msg = String()
         msg.data = f"Hello World {time.ctime()}"
         self.hw_pub.publish(msg)
    
def main():
    rclpy.init()

    try:
        node = Hello_World_Pub()
        rclpy.spin(node)
        node.destroy_node()
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()