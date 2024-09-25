
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
import os

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    joy = Node(
        package='virtual_joystick',
        executable='vjoy_node',
        parameters=[{'use_sim_time': use_sim_time}],
    )
 
   
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),        
        joy
   ])