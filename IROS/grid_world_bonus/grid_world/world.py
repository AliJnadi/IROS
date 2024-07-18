import rclpy
from rclpy.node import Node
# TODO import message types that you need for publishers and subscriber
from std_msgs.msg import Float32, Float32MultiArray, String

from numpy import random

# Import the module from Grid_World
from .Grid_World import Grid_World

import cv2

# Publish world as image
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class World(Node):
    def __init__(self):
        # TODO: Set the node name as world_node
        super().__init__('world_node')

        self.world_4_5 = Grid_World()

        # Display the world
        self.img = self.world_4_5.world_update()
        
        # Timer and publisher for publishing the image
        self.img_pub = self.create_publisher(Image, 'world_img', 1)
        self.create_timer(0.1, self.__img_timer)

        # TODO: Create publisher for state and score, Publish both of them every 1 second in seperate messages.
        self.score_pub = self.create_publisher(Float32, 'player_score', 5)
        self.state_pub = self.create_publisher(Float32MultiArray, 'world_State', 5)
        self.create_timer(1, self.__state_score_timer)

        # TODO: Create sbscriber for the command.
        self.create_subscription(String, 'world_cmd', self.__commands, 5)

        # Image display
        self.create_timer(0.1, self.__img_cv_timer)

    # TODO: command function which recieve the command from user
    def __commands(self, comm:String):
        # TODO: Add commands here, also do not forget to modify the player position by set old position to 0 and new one to 1
        comm = comm.data
        
        # There is 20% probability that player won't move according to the givven command
        if random.random() < 0.2:
            commands_list = [x for x in ['u', 'd', 'l', 'r'] if x != comm]
            comm = random.choice(commands_list)

        if comm == 'u':
            new_pos = (self.world_4_5.player[0] - 1, self.world_4_5.player[1]) 
            if new_pos[0] < 0 or self.world_4_5.state[new_pos] == -1:
                new_pos = self.world_4_5.player 
        elif comm == 'd':
            new_pos = (self.world_4_5.player[0] + 1, self.world_4_5.player[1]) 
            if new_pos[0] >= self.world_4_5.rows or self.world_4_5.state[new_pos] == -1:
                new_pos = self.world_4_5.player 
        elif comm == 'l':
            new_pos = (self.world_4_5.player[0], self.world_4_5.player[1] - 1) 
            if new_pos[1] < 0 or self.world_4_5.state[new_pos] == -1:
                new_pos = self.world_4_5.player 
        elif comm == 'r':
            new_pos = (self.world_4_5.player[0], self.world_4_5.player[1] + 1) 
            if new_pos[1] >= self.world_4_5.cols or self.world_4_5.state[new_pos] == -1:
                new_pos = self.world_4_5.player

        if new_pos != self.world_4_5.player:
            self.world_4_5.state[self.world_4_5.player] = 0
            self.world_4_5.player = new_pos
            self.world_4_5.state[self.world_4_5.player] = 1


        # Do not delete or modify this
        self.img = self.world_4_5.world_update()

    # TODO: state timer function
    def __state_score_timer(self):
        score_msg = Float32()
        score_msg.data = 1.0 * self.world_4_5.score
        self.score_pub.publish(score_msg)
       
        state_msg = Float32MultiArray()
        state_msg.data = (1.0 * self.world_4_5.state).flatten().tolist()
        self.state_pub.publish(state_msg)

    def __img_cv_timer(self):
        cv2.imshow('WORLD', self.img)
        keypressed = cv2.waitKey(1)

        if keypressed == 26 or keypressed == ord('q'):
            exit()

    # You can now preview the image using rqt, do not modify or delete this code
    def __img_timer(self):
        msg = CvBridge().cv2_to_imgmsg(self.img, "bgr8")
        self.img_pub.publish(msg)

def main():
    rclpy.init()
    
    try:
        node = World()    
        rclpy.spin(node)
        node.destroy_node()
    finally:
        rclpy.shutdown()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()