# 基于ROS2实现的Mybot机器人仿真及实体机器人

## 1.介绍
...
environment:
os: Linux 20.04
robot-os: ros2-foxy
python version: python3.8
...

## 2.安装运行

### 2.1 下载编译


```
git clone https://github.com/sirlddf/mybot.git
cd mybot
rosdep install --from-paths src -y
colcon build
```

### 2.2 运行测试    

#### 仿真
```
source install/setup.bash
ros2 launch mybot_description gazebo.launch.py
```

#### Nav2
```
source install/setup.bash
ros2 launch mybot_navigation2 navigation2.launch.py use_sim_time:=True
```
