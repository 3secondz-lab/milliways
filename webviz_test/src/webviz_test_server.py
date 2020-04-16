#!/usr/bin/env python3

"""
    Webviz Test Server
    Jinsun Park
    (zzangjinsun@3secondz.com)
"""

import sys
sys.path.insert(0, "/home/rnd/catkin_ws/install/lib/python3/dist-packages")

import rospy
import std_msgs
from math import pi as M_PI
from math import sin

from dynamic_reconfigure.server import Server
from webviz_test.cfg import WebvizTestParamsConfig


def callback(config, level):
    rospy.loginfo("Reconfigure request : {amplitude}, {freq}, {phase}, {name}, {flag}, {int}, {size}".format(**config))

    return config


if __name__ == "__main__":
    rospy.init_node("webviz_test_server", anonymous=False)

    srv = Server(WebvizTestParamsConfig, callback)
    rospy.spin()
