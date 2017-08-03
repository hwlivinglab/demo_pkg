#!/usr/bin/env python
# Title : pepper_example.py

import time
from naoqi import ALProxy

if __name__ == '__main__':
    from naoqi import ALProxy

    an_tag = ALProxy("ALAnimatedSpeech", "pepper.local", 9559)

    an_tag.say("^startTag(body language)Hi, this is using my Animated Speech API.")
