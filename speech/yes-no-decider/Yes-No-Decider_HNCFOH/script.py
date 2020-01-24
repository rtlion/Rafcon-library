import rospy
import rtl_comm.srv


def execute(self, inputs, outputs, gvm):
    transcript = inputs['transcript']
    self.logger.info("Is '%s' Yes or no" % transcript)
    yesno = rospy.ServiceProxy('nlp/yesno', rtl_comm.srv.String)
    
    try:
        answer = yesno(transcript).message
    except rospy.ServiceException as e:
        self.logger.warning(e)
        return -1
        
    self.logger.info("It is: {}".format(answer))
    
    if answer == "yes":
        return 0
        
    elif answer == "no":
        return 1
        
    else:
        return -1
