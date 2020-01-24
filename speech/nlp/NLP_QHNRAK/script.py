import rospy
from nlp.srv import *
    
# State "NLP"
def execute(self, inputs, outputs, gvm):
    transcript = inputs['transcript']
    if not transcript:
        self.logger.warn("Got no transcript, aborting")
        return -1
    self.logger.info("Asking intention for %s" % transcript)
    nlp = rospy.ServiceProxy('nlp/general', NLP)
    intention = nlp(transcript)
    self.logger.info("The Intention is:%s" % intention)
    outputs['intention'] = intention
    
    return 0