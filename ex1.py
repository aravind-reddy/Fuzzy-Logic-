#publisher
class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        self.pub=self.create_publisher(Twist, '/cmd_vel',10)
        time =0.5
        self.timer=self.create_timer(time, self.timer_callback)
    def timer_callback(self):
        msg=Twist()
        msg.linear.x= 0.5
        msg.angular.z=0.5
        self.pub.publish(msg)
        self.get_logger().info(msg)

def main(args=None):
    rclpy.init(args=args)
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown()


if __name__=='__main__':
    main()




from launch import LaunchDescription 
from launch_ros.actions import Node 
def generate_launch_description():
    return LaunchDescription([Node(package='publisher_pkg',
                                   executable='simple_publisher',
                                   output='screen')])




##subcrbers
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan 
from rclpy.qos import ReliabilityPolicy, QoSProfile


class SimpleSubcriber(Node):
    def __init__(self):
        super().__init__('simple_subcriber')
        self.sub=self.create_subscription(LaserScan, /scan, self.listener_callback, QoSProfile())
    def listener_callback(self, msg):
        self.get_logger().info(msg)

def main(args=None):
    rclpy.init(args=args)
    simple_subcriber == SimpleSubcriber()
    rclpy.spin(simple_subcriber)
    simple_subcriber.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()

from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([Node(package ='subcriber_pkg',
                                   executable='simple_subcriber',
                                   output= 'screen'),])

#modify the setup file
"simple_subcriber = subcriber_pkg.simple_subcriber:main"
#complie the package using colcon build and do source 
colcon build --packages-select subrciber_pkg


#broadcasting the transform frames
 
import rclpy
import sys
from rclpy.node import Node



