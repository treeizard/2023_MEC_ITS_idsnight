#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class RobotSubscriber(Node):
    def __init__(self):
        super().__init__("robot_sub_node")
        # Robot Subscriber Node
        self.sub = self.create_subscription(Twist, "/cmd_vel_joy", self.robot_response, 10)
    
    # The feed back response from the robot
    def robot_response(self, msg):
        cmd_velocity = msg.linear.x
        cmd_angvel = msg.angular.z
        print("Robot has received the message")
        print("Linear Velocity:"+str(cmd_velocity))
        print("Angular Velocity:"+str(cmd_angvel))

def main(arg = None):
    rclpy.init()
    robot_sub = RobotSubscriber()
    print("Waiting for data to be published from the joystick")
    

    try:
        rclpy.spin(robot_sub)
    except KeyboardInterrupt:
        print("Terminating Node ...")
        robot_sub.destroy_node()

if __name__ == '__main__':
    main()