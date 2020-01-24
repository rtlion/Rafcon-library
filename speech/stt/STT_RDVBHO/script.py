import rospy
import rtl_comm.srv
from std_msgs.msg import String


def use_stt_google(self, timeout):
    ''' Listen for amount of time and return the transcript '''
    stt_google = rospy.ServiceProxy('stt_google', rtl_comm.srv.Int32)
    self.logger.info("Now listening for %d seconds" % timeout)
    resp = stt_google(timeout).message
    self.logger.info("Just heard: %s" % resp)
    return resp
    
    
def use_stt_offline(self, timeout):
    ''' Listen for amount of time and return the transcript '''
    stt_offline = rospy.ServiceProxy('stt_offline', rtl_comm.srv.Int32)
    self.logger.info("Now listening for %d seconds" % timeout)
    resp = stt_offline(timeout).message
    self.logger.info("Just heard: %s" % resp)
    return resp



def execute(self, inputs, outputs, gvm):
    
    timeout = inputs['timeout']
    if not timeout:
        self.logger.warn("Got no timeout, aborting")
        return -1
    try:
        rospy.wait_for_service('stt_google', 2.0)
        transcript = use_stt_google(self, timeout)
        
    except rospy.ROSException as e:
        self.logger.warning(e)
        self.logger.warning("Waited too long for the stt online service - trying offline serivce")
        
        try:
            rospy.wait_for_service('stt_offline', 1.0)
            transcript = use_stt_offline(self, timeout)
            
        except rospy.ROSException as e:
            self.logger.warning(e)
            self.logger.warning("Waited too long for the stt offline service - timeout!")
            return "timeout"
    
    
    vbOpPub = gvm.get_variable('vizboxOperatorText', per_reference=True)
    
    if not vbOpPub:
        self.logger.warning("Did not find a '/operator_text' publisher. Creating a new one...")
        vbOpPub = rospy.Publisher('/operator_text', String, queue_size=1)
        gvm.set_variable('vizboxOperatorText', vbOpPub, per_reference=True)
    
    else:
        self.logger.info("Using chached operator vizbox publisher: {}".format(vbOpPub))
    
    vbOpPub.publish(transcript)
    
    outputs['transcript'] = transcript
    self.logger.verbose("STT Transcript: '{}'".format(transcript))
    
            
    return 0
