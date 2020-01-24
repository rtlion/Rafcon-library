import rospy
from std_msgs.msg import Bool    

def execute(self, inputs, outputs, gvm):
    
    fmPub = rospy.Publisher('/followMe/run_flag', Bool, queue_size=1)
    gvm.set_variable('fmPub',fmPub, per_reference=True)
    
    
    def humanDetectedCallback(data):
        self.logger.info("Human Decteded Callback - data: {}".format(data))
        outputs['humanInSight'] = data
        gvm.set_variable('personInSight',data,per_refernce=True)
    
    sub = rospy.Subscriber('/followme/human_selected_flag', Bool, humanDetectedCallback)
    
    self.logger.info("Created subscriber for human selected flag: {}".format(sub))
    
    return 0
