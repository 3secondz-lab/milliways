#!/usr/bin/env python3

"""
    Webviz Test Client
    Jinsun Park
    (zzangjinsun@3secondz.com)
"""

import sys
sys.path.insert(0, "/home/rnd/catkin_ws/install/lib/python3/dist-packages")

import rospy
import std_msgs
from math import pi as M_PI
from math import sin

from dynamic_reconfigure.client import Client
from webviz_test.cfg import WebvizTestParamsConfig

def callback(config):
    rospy.loginfo("Configuration callback")
    return

if __name__ == "__main__":
    rospy.init_node("webviz_test_client")

    client = Client("webviz_test_server", timeout=30, config_callback=callback)

    pub = rospy.Publisher("sin", std_msgs.msg.Float64, queue_size=1)

    r = rospy.Rate(10)
    t0 = rospy.Time.now()
    while not rospy.is_shutdown():

        config = client.get_configuration()

        A = config.amplitude
        w = config.freq
        p = config.phase
        name = config.name
        v_flag = config.flag
        v_int = config.int
        v_size = config.size

        t1 = rospy.Time.now()
        t = (t1 - t0).to_sec()

        val = std_msgs.msg.Float64()
        val.data = A*sin(2*M_PI*w*t + p)

        pub.publish(val)

        # rospy.loginfo("Name : {}, Flag : {}, Int : {}, Size : {}".format(
        #     name, v_flag, v_int, v_size
        # ))

        r.sleep()
