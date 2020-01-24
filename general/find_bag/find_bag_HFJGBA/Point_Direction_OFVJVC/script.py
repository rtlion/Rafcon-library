import rospy
import std_msgs.msg
import cPickle as pickle

#from . import WhichBag
#from ros import WhichBag

import sys
import os
import yaml

with open(os.path.expanduser("~/.config/rafcon/config.yaml")  , 'r') as stream:
    yamlData = yaml.safe_load(stream)
    rafconLibPath = yamlData['LIBRARY_PATHS']['rtl_rafcon_lib']
    sys.path.insert(1, rafconLibPath)
    
from externalScripts import WhichBag

sys.path.insert(1, os.path.expanduser("~/libs/tf-pose-estimation"))
from tf_pose.estimator import TfPoseEstimator

# 4. Pointing to bag (mit OpenPose)

def execute(self, inputs, outputs, gvm):
    
    self.logger.info("Start - getting point direction")
    rospy.sleep(0.8) # wait a bit
    
    try:
        humans = rospy.wait_for_message(
            inputs["humans topic"],
            std_msgs.msg.String,
            timeout=inputs["wait_for_message_timeout"]
        )
    except rospy.ROSException as timeout:
        self.logger.info("Timeout")
        return "timeout"

    self.logger.info("Affter rospy wait")

    # call arm find function
    hums = pickle.loads(humans.data)
        
    
    fett = WhichBag.biggestPeron(hums)
    
    self.logger.info("Calling choose bag")
    
    somewhere = WhichBag.chooseBag(fett.body_parts)
    self.logger.info("STATUS: Decide Bag %r" % somewhere)
    outputs["pointingDirection"] = somewhere
    
    return "success"
