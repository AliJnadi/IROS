from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    pose_pub_node = Node(package = 'distance',         # Package name Found in setup.py
                         executable = 'pos_pub_node',  # Node name found in setup.py 
                         name = 'pose_pub_node')       # Name that you want to give to node               
    
    # TODO: Creat cart_dis_node node
    # cart_dis_node = Node(package = '',        
    #                      executable = '',
    #                      name = '')        
    
    # TODO: Creat res_disp_node node
    # res_disp_node = Node(package = '',        
    #                      executable = '', 
    #                      name = '')       

    ld.add_action(pose_pub_node)
    # TODO: Add the two other nodes to launch description
    # ld.add_action()
    # ld.add_action()
    
    return ld