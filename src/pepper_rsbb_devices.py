#!/usr/bin/env python
#Title: pepper_rsbb_devices.py
# Date : 09/06/2017
# Version : 1.0

import rospy, qi, argparse
import os
import sys
import time
import naoqi
import std_srvs
from std_srvs.srv import Empty

def serviceCall():
    rospy.wait_for_service('/devices/switch_1/on')
    try:
        switch_1 = rospy.ServiceProxy('/devices/switch_1/on', Empty)
        response = switch_1()

    except rospy.ServiceException, e:
         print "Service call failed: %s"%e

def dialog1():
    ALDialog = ALProxy("ALDialog", "pepper.local", 9559)
    topic_content = ('topic: ~switch()\n'
					'language: enu\n'
					'concept:(choice) [yes no "yes please" "no thank you"]\n'
                    'u: (yes [please]) Great!^stopTag(body language)\n'
                    'u: (no ["thank you"]) Okay.')
    topic_name = ALDialog.loadTopicContent(topic_content)
    ALDialog.activateTopic(topic_name)
    ALDialog.subscribe('switch_dialog')
    time.sleep(5)
    ALDialog.unsubscribe('switch_dialog')
    ALDialog.deactivateTopic(topic_name)
    ALDialog.unloadTopic(topic_name)
    return


if __name__ == '__main__':
#    from naoqi i


        serviceCall()
