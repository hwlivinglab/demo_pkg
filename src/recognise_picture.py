#!/usr/bin/env python
import os
import sys
import time
import naoqi
from naoqi import *
# A global counter of the number of loops
count = 10
newModule = 0

PC_IP = "192.168.1.62"  # Replace this with your computer's IP address
NAO_IP = "pepper.local" # Replace this with your NAOqi's IP address

# The name of the event generated by ALVisionRecognition
event_name = "PictureDetected"

# The name of our local python module
#module_name = "banana"

class myModule(ALModule):
  def endProgram():
    print("end")

  def dataChanged(self, strVarName, value, strMessage):
    """callback when data change"""

    print "datachanged", strVarName, " ", value, " ", strMessage
    global count
    count = count - 1
    tts.say("Ibuprofen")
    #tts.say("Ibuprofen should be taken with a meal")
    tabletProxy.showImage("http://198.18.0.1/apps/dragone-51a938/Dragone.jpg")
    time.sleep(5)
    tabletProxy.hideImage()
    return

# Create a local broker, connected to the remote naoqi
broker = ALBroker("pythonBroker", PC_IP, 9999, NAO_IP, 9559)

# Create a python module
#pythonModule = myModule(module_name)
try:
  global newModule
  newModule = myModule("newModule")
  # Create a proxy to ALMemory
  tts = ALProxy("ALTextToSpeech", "pepper.local", 9559)
  memoryProxy = ALProxy("ALMemory", "pepper.local", 9559)
  tabletProxy = ALProxy("ALTabletService", "pepper.local", 9559)
  # Subscribe to the event, saying where we want to be called back
  memoryProxy.subscribeToEvent(event_name, "newModule", "dataChanged")

  # Let the picture recognition run
  while count > 0:
    time.sleep(5)
    print("running picture recognition")
    print(count)
    if (count == 9):
        print("exit")
        break

  # Unsubscribe
  memoryProxy.unsubscribeToEvent(event_name,"newModule")

except RuntimeError, e:
  print e
  exit(1)

print 'end'
