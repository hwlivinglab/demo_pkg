#!/usr/bin/env python
# Title : speech_test.py
# Author : Clarissa Cremona
# Date : 13/06/2017
# Version : 1.0

import time
from naoqi import ALProxy

if __name__ == '__main__':
    from naoqi import ALProxy
    tabletProxy = ALProxy("ALTabletService", "pepper.local", 9559)
    tabletProxy.showImage("http://198.18.0.1/apps/dragone-51a938/Dragone.jpg")
    #tabletProxy.showImage("http://198.18.0.1/img/help_charger.png")
    time.sleep(5)
    tabletProxy.hideImage()
