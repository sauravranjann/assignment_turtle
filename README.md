# About

This ROS Package can be used to control the movement of a bot inside the turtlesim package

# Installation

- Install the `turtlesim` package

    ```bash
    sudo apt-get install ros-noetic-turtlesim
    ```

- Clone this package inside a catkin workspace

    ```bash
    mkdir -p ros_ws/src 
    cd ros_ws/src
    https://github.com/sauravranjann/assignment_turtle/.git
    ```

- Compile the code and source the workspace

    ```bash
    catkin_make
    source devel/setup.bash
    ```

# Instructions to run the code

- In terminal 1

    ```bash
    roscore
    ```

- In terminal 2

    ```bash
    rosrun turtlesim turtlesim_node
    ```

- In terminal 3

    ```bash
     rosrun turtle_move turtle_rectangle.py
    ```# assignment_turtle
