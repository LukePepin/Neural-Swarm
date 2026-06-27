import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # 1. Start the Micro-ROS Agent for UDP communication with the ESP32 Alviks
        ExecuteProcess(
            cmd=['ros2', 'run', 'micro_ros_agent', 'micro_ros_agent', 'udp4', '--port', '8888'],
            output='screen'
        ),
        
        # 2. Start the Environment Builder node
        Node(
            package='lp_neural_swarm',
            executable='environment_builder.py',
            name='environment_builder',
            output='screen'
        ),
        
        # 3. Start the Swarm Telemetry node
        Node(
            package='lp_neural_swarm',
            executable='swarm_telemetry.py',
            name='swarm_telemetry_node',
            output='screen'
        ),
        
        # 4. Optional: Launch Gazebo if we are running the Digital Twin mode
        # This will be fully implemented when the SDF for Alvik is ready
        # ExecuteProcess(
        #     cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
        #     output='screen'
        # )
    ])
