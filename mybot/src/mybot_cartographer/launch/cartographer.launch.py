import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    pkg_share = FindPackageShare(package='mybot_cartographer').find('mybot_cartographer')
    
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    resolution = LaunchConfiguration('resolution', default='0.05')

    publish_period_sec = LaunchConfiguration('publish_period_sec', default='1.0')

    configuration_directory = LaunchConfiguration('configuration_directory',default= os.path.join(pkg_share, 'config') )

    configuration_basename = LaunchConfiguration('configuration_basename', default='mybot_2d.lua')

    
    cartographer_node = Node(
        package='cartographer_ros',
        executable='cartographer_node',
        name='cartographer_node',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments=['-configuration_directory', configuration_directory,
                   '-configuration_basename', configuration_basename])

    occupancy_grid_node = Node(
        package='cartographer_ros',
        executable='occupancy_grid_node',
        name='occupancy_grid_node',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments=['-resolution', resolution, '-publish_period_sec', publish_period_sec])

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen')

    ld = LaunchDescription()
    ld.add_action(cartographer_node)
    ld.add_action(occupancy_grid_node)
    ld.add_action(rviz_node)

    return ld