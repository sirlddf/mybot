# mybot
This is a raw application of virtual navigation based on ros2
## 注意当前分支代码为foxy版本，如需humble版本请在左上角切换分支

# 基于ROS2实现的Fishbot机器人仿真及实体机器人

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
git clone https://github.com/sirlddf/mybot.git -b foxy
cd mybot
rosdep install --from-paths src -y
colcon build
```

### 2.2 运行测试

#### 在RVIZ中显示机器人模型

```
source install/setup.bash
ros2 launch mybot_description display_rviz2.launch.py
```

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
