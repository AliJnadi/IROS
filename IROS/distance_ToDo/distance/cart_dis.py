import rclpy
from rclpy.node import Node

# TODO: Import messages that you need for the task
# from  import 
# from  import 

class Cart_Dis(Node):
    init_pos = []
    cur_pos = []

    cart_distance = None

    def __init__(self):
        # TODO: Set the node name
        # super().__init__("")

        # TODO: Create subscribers and publisher
        # self.create_subscription(, , self.__init_pos_sub, 5)
        # self.create_subscription(, , self.__cur_pos_sub, 5)
        # self.dist_pub = self.create_publisher(, , 5)

    def __init_pos_sub(self, msg:Point):
        self.init_pos = msg

    def __cur_pos_sub(self, msg:Point):
        self.cur_pos = msg

        if self.init_pos != []:
            # TODO: Extract iniitial and current positions
            # x_i, y_i, z_i =  self.init_pos.x, , 
            # x, y, z = , , 

            # TODO: Caluculate the distance
            # self.cart_distance = 
            
            # TODO: Create the message and publish it
            res_msg = Float32MultiArray()
            # res_msg.data = [, , , , , , ]
            # self.dist_pub.publish()



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