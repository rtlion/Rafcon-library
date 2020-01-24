import rospy
from std_msgs.msg import UInt32

def execute(self, inputs, outputs, gvm):
    
    vixboxCounter = gvm.get_variable('vizbox_counter', per_reference=True)
    
    pub = gvm.get_variable('challengeStepPub', per_reference=True)
    
    if not pub:
        #self.logger.warning("Did not find a '/challenge_step' publisher. Creating a new one...")
        pub = rospy.Publisher('/challenge_step', UInt32, queue_size=1)
        gvm.set_variable('challengeStepPub', pub, per_reference=True)
    
    pub.publish(vixboxCounter)

    return 0