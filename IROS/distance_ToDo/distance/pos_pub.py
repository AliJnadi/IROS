import rclpy
from rclpy.node import Node

# TODO: Import messages that you need for the task
# from  import

import random

class Pos_Pub(Node):
    init_pos = []
    cur_pos = []

    def __init__(self):
        # TODO: Set the node name
        # super().__init__("")

        # TODO: Create the publishers
        # self.init_pos_pub = self.create_publisher(, , 5)
        # self.cur_pos_pub = self.create_publisher(, , 5)

        # TODO: randomly generate the initial position by generate a random number between (-5, 5)
        self.init_pos = Point()
        # self.init_pos.x = random.???????
        # self.init_pos.y = 
        # self.init_pos.z = 

        self.cur_pos = self.init_pos

        # TODO: Create timers
        # self.create_timer(, self.__initial_timer)
        # self.create_timer(, self.__publish_timer)

    def __initial_timer(self):
        # TODO: Publish the initial position
        # self.init_pos_pub.publish()

    def __publish_timer(self):
        # Update current position then publish it by adding a arndom number between (-1, 1)
        # self.cur_pos.x += random.????????
        # self.cur_pos.y += 
        # self.cur_pos.z += 

        # self.cur_pos_pub.publish()

def main():
    rclpy.init()

    try:
        # TODO: Create node object
        # node =
        rclpy.spin(node)
        node.destroy_node()
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()