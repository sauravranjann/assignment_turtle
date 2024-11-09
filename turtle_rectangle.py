#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from time import sleep

def move_straight(linear_speed, duration):
    # Initialize message
    vel_msg = Twist()
    vel_msg.linear.x = linear_speed
    vel_msg.angular.z = 0.0
    
    # Publish the message for a set duration
    for _ in range(duration):
        velocity_publisher.publish(vel_msg)
        sleep(0.1)

def turn_90_degrees():
    # Initialize message
    vel_msg = Twist()
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 1.57  # Roughly 90 degrees per second

    # Publish the message for a set duration to complete a 90 degree turn
    duration = 10  # Adjust to achieve a full 90-degree turn
    for _ in range(duration):
        velocity_publisher.publish(vel_msg)
        sleep(0.1)

def draw_rectangle():
    # Define dimensions
    length = 4  # Length of the rectangle
    breadth = 2  # Breadth of the rectangle
    
    # Repeat the sequence to form a rectangle
    for _ in range(2):
        move_straight(1.0, length * 10)  # Adjust duration for length
        turn_90_degrees()
        move_straight(1.0, breadth * 10)  # Adjust duration for breadth
        turn_90_degrees()

if __name__ == "__main__":
    # Initialize the ROS node
    rospy.init_node('turtle_rectangle', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    # Allow time for setup
    rospy.sleep(2)
    
    # Draw the rectangle
    draw_rectangle()

    # Stop the turtle after completing the rectangle
    stop_msg = Twist()
    velocity_publisher.publish(stop_msg)
    rospy.spin()
