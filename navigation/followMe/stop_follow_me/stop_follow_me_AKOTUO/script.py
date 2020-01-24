import rospy
from std_msgs.msg import Bool

def execute(self, inputs, outputs, gvm):
    
    self.logger.info("Stopping follow me...")
    
    #fmPub = inputs['followMePublisher']
    fmPub = rospy.Publisher('/followMe/run_flag', Bool, queue_size=1)
    
    counter = 0
    while fmPub.get_num_connections() == 0 and counter < 5:
        self.logger.info("Waiting for subscriber to connect")
        rospy.sleep(1)
        counter += 1
    
    self.logger.info(fmPub)
    
    #fmPub = gvm.get_variable('fmPub', per_reference=True)
    fmPub.publish(Bool(False))
    
    return 0