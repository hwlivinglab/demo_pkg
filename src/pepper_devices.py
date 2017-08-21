#!/usr/bin/env python
# Title : pepper_iot.py
# Author : Clarissa Cremona
# Date : 09/06/2017
# Version : 1.0

import rospy, qi, argparse
import os
import sys
import time
import naoqi
from naoqi import *
from diagnostic_msgs.msg import KeyValue # this is the message type /iot_updates uses
from std_msgs.msg import Empty


def callback(data):

	import std_srvs
	from std_srvs.srv import Empty
#	print("in callback")
#	animatedProxy.say("Someone is at the door")
	rospy.wait_for_service('/devices/switch_1/on')
	try:
		switch_1 = rospy.ServiceProxy('/devices/switch_1/on', Empty)
		response = switch_1()

	except rospy.ServiceException, e:
	 	print "Service call failed: %s"%e

def devices_callback(data):
    if(data.key == "Hall_Intcm" and data.value == "ON"): # Drawer opened
        bell_ring()
    elif(data.key == "Ktch_light" and data.value == "ON"):
        kitchen_light()
    elif(data.key == "Ktch_B1_Cupboard" and data.value == "OFF"):
        kitchen_cupboard1()

def bell_ring():
    animatedProxy.say("There is someone at the door")

def kitchen_light():
    animatedProxy.say("The kitchin light is on")

def kitchen_cupboard1():
    animatedProxy.say("The first kitchin cupboard is open")

def listener():
    rospy.init_node('bell_listener', anonymous=True) # create node to subscribe to topic
    rospy.Subscriber("/devices/bell", Empty, callback) # subscribe to topic /iot_updates
    rospy.Subscriber("/iot_updates", KeyValue, devices_callback)
    rospy.spin() # keeps python from exiting until node is stopped

if __name__ == '__main__':
    from naoqi import ALProxy
    # Create a local broker, connected to the remote naoqi
    broker = ALBroker("pythonBroker", "192.168.1.129", 9999, "pepper.local", 9559)
    #global newModule
    #newModule = myModule("newModule")
    tts = ALProxy("ALTextToSpeech", "pepper.local", 9559) # initialise speech proxy
    tts.setParameter("speed", 100) # set speed of speech
    animatedProxy = ALProxy("ALAnimatedSpeech", "pepper.local", 9559) # initialise animated speech proxy
    postureProxy = ALProxy("ALRobotPosture", "pepper.local", 9559) # initialise posture proxy
    motionProxy = ALProxy("ALMotion", "pepper.local", 9559) # initialise motion proxy
    tabletProxy = ALProxy("ALTabletService", "pepper.local", 9559)
    #recogProxy = ALProxy("ALSpeechRecognition", "pepper.local", 9559) # initialise speech recognition proxy

    basicProxy = ALProxy("ALBasicAwareness", "pepper.local", 9559) # initialise basic awareness proxy
    basicProxy.setEnabled(True) # enable basic awareness # set tracking mode to move
    basicProxy.setEngagementMode("FullyEngaged")

    #recogProxy.subscribe("Test_ASR")
    memProxy = ALProxy("ALMemory","pepper.local",9559)
    #memoryProxy.subscribeToEvent(event_name, "newModule", "Dialog/Answered")
    while True:
        listener()
