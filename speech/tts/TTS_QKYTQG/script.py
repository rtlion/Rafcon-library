import rospy
import rtl_comm.srv
from std_msgs.msg import String

import os
import yaml
import sys
import socket

with open(os.path.expanduser("~/.config/rafcon/config.yaml")  , 'r') as stream:
    yamlData = yaml.safe_load(stream)
    rafconLibPath = yamlData['LIBRARY_PATHS']['rtl_rafcon_lib']
    sys.path.insert(1, rafconLibPath)
    
from externalScripts import p_brain

# State "Speak"
def execute(self, inputs, outputs, gvm):
    
    
    # --- p brain ---
    hasEmofaniConnection = False
    emofaniClient = gvm.get_variable('emofaniClient', per_reference=True)
    
    if not emofaniClient:
        self.logger.warning("Did not find a emofani client... creating a new one!")
        
        sourceIp = inputs['sourceIP']
        
        #sourceIp = socket.gethostbyname(socket.gethostname())
        #self.logger.info("My ip: {}".format(sourceIp))
        sourcePort = inputs['sourcePort']
        targetIp = inputs['targetIP']
        targetPort = inputs['targetPort']
        
        try:
            emofaniClient = p_brain.emofani(sourceIp, sourcePort, targetIp, targetPort)
            hasEmofaniConnection = True
        except Exception as e:
            self.logger.warning("Emofani Error: {error}".format(error = e))
            hasEmofaniConnection = False
        
        gvm.set_variable('emofaniClient', emofaniClient, per_reference=True)
    else:
        self.logger.info("Using chached emofani client: {}".format(emofaniClient))
        hasEmofaniConnection = True
    ###############

    text = str(inputs['text'])
    if not text:
        self.logger.warn("Got no text to speak, aborting")
        return -1
    tts = rospy.ServiceProxy('tts/speak', rtl_comm.srv.String)
    self.logger.info("Now saying: %s" % text)
    
    if hasEmofaniConnection:
        emofaniClient.speaking(True) # start emofani
    resp = tts(text).message
    #self.logger.info("Got response: %s" % text)
    
    if hasEmofaniConnection:
        emofaniClient.speaking(False) # stop it    
    
    
    # --- vizbox ---
    vbPub = gvm.get_variable('vizboxRobotText', per_reference=True)
    
    if not vbPub:
        self.logger.warning("Did not find a '/robot_text' publisher. Creating a new one...")
        vbPub = rospy.Publisher('/robot_text', String, queue_size=1)
        gvm.set_variable('vizboxRobotText', vbPub, per_reference=True)
    
    else:
        self.logger.info("Using chached vizbox publisher: {}".format(vbPub))
    vbPub.publish(text)
    ###################
    
    return 0