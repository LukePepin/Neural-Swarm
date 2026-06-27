#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SwarmTelemetryNode(Node):
    def __init__(self):
        super().__init__('swarm_telemetry_node')
        self.get_logger().info('Swarm Telemetry Node started (Micro-ROS interface).')
        
        # Subscribes to telemetry from the Arduino Alviks via micro-ROS
        self.telemetry_sub = self.create_subscription(
            String,
            '/alvik_swarm/telemetry',
            self.telemetry_callback,
            10
        )
        
    def telemetry_callback(self, msg):
        self.get_logger().info(f'Received telemetry from Alvik: {msg.data}')
        # TODO: Parse telemetry for battery life, ESP32 status, and MARL agent decisions

def main(args=None):
    rclpy.init(args=args)
    node = SwarmTelemetryNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
