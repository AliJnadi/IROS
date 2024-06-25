import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

class Hello_World_Sub(Node):
     def __init__(self):
        super().__init__('HW_sub_node')

        self.create_subscription(String, 'HW_topic', self.__hw_sub_callback, 10)

     def __hw_sub_callback(self, msg:String):
         data = msg.data
         self.get_logger().info(f'Message recieved: {data}')
    
def main():
    rclpy.init()

    try:
        node = Hello_World_Sub()
        rclpy.spin(node)
        node.destroy_node()
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()