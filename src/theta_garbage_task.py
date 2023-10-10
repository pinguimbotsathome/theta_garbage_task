#!/usr/bin/env python3

import rospy
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import Twist
from theta_speech.srv import SpeechToText
from std_msgs.msg import Empty, String
import rospkg
import time

PACK_DIR = rospkg.RosPack().get_path("theta_carry_my_luggage_task")

tts_pub  = rospy.Publisher('/textToSpeech', String, queue_size=10)
face_pub = rospy.Publisher('/hri/affective_loop', String, queue_size=10)

def task_procedure(self):

    rospy.logwarn("start task")
    
    face_pub.publish('littleHappy')
    tts_pub.publish('Please open the door')
    time.sleep(4)

    #navegação ate a lixeira 1

    tts_pub.publish('Please put the garbage carefully in the green mark next to red button, PLEASE dont touch the botton')
    time.sleep(10)
    tts_pub.publish("Ok!")

    #navegação ate a lixeira 2 

    tts_pub.publish('Please put the garbage carefully in the green mark next to red button, PLEASE dont touch the botton')
    time.sleep(10)
    tts_pub.publish("Ok!")

    #navegação para fora da casa
    tts_pub.publish('Finish task')
    face_pub.publish("happy")

if __name__ == "__main__":
    rospy.init_node('Take_the_Garbage_node', anonymous=True)

    while not rospy.is_shutdown():
        pass