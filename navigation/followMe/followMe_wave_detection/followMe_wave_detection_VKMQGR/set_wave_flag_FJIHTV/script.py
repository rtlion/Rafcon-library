import rospy
from std_msgs.msg import Bool

def execute(self, inputs, outputs, gvm):
    
    self.logger.info("set wave flag on true...")
    
    ####
    rospy.set_param("followMe_wave_flag", True)
    ####
    
    
    #########
    wavePub = rospy.Publisher('/followMe/wave_flag', Bool, queue_size=1)
    
    counter = 0
    while wavePub.get_num_connections() == 0 and counter < 5:
        self.logger.info("Waiting for subscriber to connect")
        rospy.sleep(1)
        counter += 1
    
    #self.logger.info(wavePub)
    #self.logger.info(wavePub.publish(Bool(True)))
    
    wavePub.publish(Bool(True))
    ############
    
    return 0
