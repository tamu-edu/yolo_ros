# Copyright (C) 2023  Miguel Ángel González Santamarta

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory("yolo_bringup"),
                        "launch",
                        "yolo.launch.py",
                    )
                ),
                launch_arguments={
                    "model": LaunchConfiguration("model", default="yolov8s-seg.pt"),
                    "device": LaunchConfiguration("device", default="cuda:0"),
                    "enable": LaunchConfiguration("enable", default="True"),
                    "threshold": LaunchConfiguration("threshold", default="0.5"),                    
                    "use_tracking": LaunchConfiguration("use_tracking", default="False"),
                    "input_image_topic": LaunchConfiguration(
                        "input_image_topic", default="/my_camera/pylon_ros2_camera_node/image_rect"
                    ),
                    "image_reliability": LaunchConfiguration(
                        "image_reliability", default="2"
                    ),
                    "namespace": LaunchConfiguration("namespace", default="yolo"),
                    "half" : LaunchConfiguration("half", default = "True"),
                }.items(),
            )
        ]
    )
