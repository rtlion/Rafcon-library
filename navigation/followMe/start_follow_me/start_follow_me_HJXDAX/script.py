import rospy
from std_msgs.msg import Bool

def execute(self, inputs, outputs, gvm):
    
    self.logger.info("Starting follow me...")
    
    # declare wave flag
    rospy.set_param("followMe_wave_flag", False)
    
    fmPub = rospy.Publisher('/followMe/run_flag', Bool, queue_size=1)
    
    counter = 0
    while fmPub.get_num_connections() == 0 and counter < 10:
        self.logger.info("Waiting for subscriber to connect")
        rospy.sleep(1)
        counter += 1
    
    #self.logger.info(fmPub)
    #self.logger.info(fmPub.publish(Bool(True)))
    
    self.logger.info("Set follow me flag on true")
    fmPub.publish(Bool(True))
    
    return 0
