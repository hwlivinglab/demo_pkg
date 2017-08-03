#!/usr/bin/env python
# Title : speech_test.py
# Author : Clarissa Cremona
# Date : 13/06/2017
# Version : 1.0

import time
from naoqi import ALProxy


ROBOT_IP = "pepper.local"
# Creates a proxy on the speech-recognition module
asr = ALProxy("ALSpeechRecognition", ROBOT_IP, 9559)
asr.unsubscribe("Test_ASR")
memoryProxy = ALProxy("ALMemory", ROBOT_IP, 9559)


asr.setLanguage("English")

# Example: Adds "yes", "no" and "please" to the vocabulary (without wordspotting)
vocabulary = ["yes", "no", "please"]
asr.setVocabulary(vocabulary, False)

# Start the speech recognition engine with user Test_ASR
asr.subscribe("Test_ASR")
print 'Speech recognition engine started'

value = memoryProxy.getData("WordRecognized")
time.sleep(20)
print(value[0])
value = memoryProxy.getData("WordRecognized")
time.sleep(20)
print(value[0])

asr.unsubscribe("Test_ASR")


'''
import sys, select, termios, tty, rospy
from diagnostic_msgs.msg import KeyValue # this is the message type /iot_updates uses

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__ == '__main__':
    from naoqi import ALProxy
    settings = termios.tcgetattr(sys.stdin)
    tts = ALProxy("ALTextToSpeech", "pepper.local", 9559)
    tts.setParameter("speed", 100)
    recogProxy = ALProxy("ALSpeechRecognition", "pepper.local", 9559)
    vocabulary = ["yes", "no", "please"]
    recogProxy.setVocabulary(vocabulary, False)
    recogProxy.subscribe("Test_ASR")
    recogProxy.subscribe("WordRecognized")
    memProxy = ALProxy("ALMemory","pepper.local",9559)
    while(getKey() != '\x03'):
        value = memProxy.getData("WordRecognized")
        print(value)
    recogProxy.unsubscribe("Test_ASR")
'''
