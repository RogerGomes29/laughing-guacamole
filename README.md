# Laughing-Guacamole </br>
## EE 5900 - Intro to robotics </br>
### Project 5 Team 1

#### Working with the Jackal

#####Task for the Project

0. [ ] Connect to a real Jackal and drive it using rviz

0. [ ] Integrate the LM291 with Jackal in rviz

0. [ ] Build URDF model including mass for the **SICK LM291**

0. [ ] Publish laser scan data in appropriate frame

0. [ ] To develop autonomous mapping routine of any of EERC floor

0. [ ] Use of *GPS* **Extra**

0. [x] Driving Jackal (use: sudo apt-get install ros-indigo-jackal-simulator ros-indigo-jackal-desktop)

#### Team starring:

*Deep*

*Sabari*

*Roger*

#####Setting Up the Workspace
```
$ cd catkin_ws/src
$ catkin_init_workspace
$ cd ..
$ git submodule init
$ git submodule update
```
Finally, the project can be built as follow:

```
$ catkin_make
$ source devel/setup.bash
```
