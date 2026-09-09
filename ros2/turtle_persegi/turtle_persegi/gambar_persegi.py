from math import radians

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class GambarPersegi(Node):
    def __init__(self):
        super().__init__('gambar_persegi')
        self.i = 0
        self.j = 0
        self.state = 0
        self.pub = self.create_publisher(Twist, "turtle1/cmd_vel", 1)
        self.timer = self.create_timer(0.016, self.timer_callback)

    def destruct(self) -> None:
        self.destroy_node()
        rclpy.shutdown()

    def timer_callback(self) -> None:
        if self.i == 8:
            self.publish(0.0, 0.0)
            self.destruct()
            return

        if self.i % 2 == 0:
            self.publish(10.0, 0.0)
        else:
            self.publish(0.0, 9.8)

        print(self.i, self.j)

        self.j += 1

        if self.j == 10:
            self.i += 1
            self.j = 0


    def publish(self, linear, angular) -> None:
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    gambar_persegi = GambarPersegi()

    rclpy.spin(gambar_persegi)

if __name__ == '__main__':
    main()
