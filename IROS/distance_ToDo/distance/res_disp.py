import rclpy
from rclpy.node import Node

# TODO: Import messages that you need for the task
# from  import

class Res_Disp(Node):
    init_pos = []
    cur_pos = []

    cart_distance = None

    def __init__(self):
        # TODO: Set the node name
        # super().__init__("")

        # TODO: Create subscriber
        # self.create_subscription(, , self.__res_disp_sub, 5)

    def __res_disp_sub(self, msg:Float32MultiArray):
        # TODO: Extract data from the message 
        # msg = msg.???
        # x_i, y_i, z_i = , , 
        # x, y, z = , , 
        # dist = 

        self.get_logger().info(f'\nInitial position : ({x_i}, {y_i} {z_i}) \n' + 
                               f'Current position : ({x}, {y} {z}) \n' +
                               f'Distance : {dist} \n' + 
                               f'----------------------------------------------')


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