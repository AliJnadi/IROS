import rclpy
from rclpy.node import Node
# TODO import message types that you need for publishers and subscriber

# Import the module from Grid_World
from .Grid_World import Grid_World

# Publish world as image
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class World(Node):
    def __init__(self):
        # TODO: Set the node name
        super().__init__('')

        self.world_4_5 = Grid_World()

        # Display the world
        self.img = self.world_4_5.world_update()
        
        # Timer and publisher for publishing the image
        self.img_pub = self.create_publisher(Image, 'world_img', 1)
        self.create_timer(0.1, self.__img_timer)

        # TODO: Create publisher for state and score, Publish both of them every 1 second in seperate messages.

        # TODO: Create sbscriber for the command.

        # TODO: Create timer for state and score publishing every 1 sec.

    # TODO: command function which recieve the command from user
    def __commands(self, comm):
        # TODO: Add commands here, also do not forget to modify the player position by set old position to 0 and new one to 1
        
        # Do not delete or modify this
        self.img = self.world_4_5.world_update()

    # TODO: state timer function
    def __state_score_timer(self):
        ...

    # You can now preview the image using rqt, do not modify or delete this code
    def __img_timer(self):
        msg = CvBridge().cv2_to_imgmsg(self.img, "bgr8")
        self.img_pub.publish(msg)

def main():
    rclpy.init()
    
    # TODO: Create the node ........
    try:
        ...
    finally:
        ...

if __name__ == '__main__':
    main()