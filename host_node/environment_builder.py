#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid, Odometry
import numpy as np

class EnvironmentBuilder(Node):
    def __init__(self):
        super().__init__('environment_builder')
        self.get_logger().info('Environment Builder Node started.')
        
        # In a swarm, we might have multiple Alviks. We can subscribe to a generic topic
        # or use namespace subscriptions for each robot in the swarm.
        self.scan_sub = self.create_subscription(
            LaserScan,
            '/alvik_swarm/scans',
            self.scan_callback,
            10
        )
        
        self.odom_sub = self.create_subscription(
            Odometry,
            '/alvik_swarm/odometry',
            self.odom_callback,
            10
        )
        
        self.map_pub = self.create_publisher(OccupancyGrid, '/reconstructed_map', 10)
        
        # 2D Occupancy Grid representation
        self.grid_resolution = 0.05 # 5cm per cell
        self.grid_size = (1000, 1000)
        self.map_data = np.zeros(self.grid_size, dtype=np.int8)

    def scan_callback(self, msg):
        # TODO: Ingest 1D/2D ToF data from Arduino Alvik and raytrace to update map
        pass

    def odom_callback(self, msg):
        # TODO: Track poses of the swarm agents to register their scans correctly
        pass

def main(args=None):
    rclpy.init(args=args)
    node = EnvironmentBuilder()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
