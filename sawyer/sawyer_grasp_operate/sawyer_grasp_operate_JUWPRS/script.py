import rospy
from itchy_hands.srv import * 

def execute(self, inputs, outputs, gvm):
    
    # can be between 0 and 9
    # 0 -> close
    # 9 -> fully open
    degree = inputs['degree']
    
    testMode = inputs['testMode']
    
    self.logger.info("Operate gripper!")
    
    if testMode:
        import time
        time.sleep(0.5)
        return 1 # success
        
    else:
    
        if degree < 0:
            degree = 0
            self.logger.info("Degree was lower than 0, will be set to 0. (0 is min)")
        
        if degree > 9:
            degree = 9
            self.logger.info("Degree was higher than 9, will be set to 9. (9 is max)")
        
        self.logger.info("Gripper open/close to: {}".format(degree))
        
        
        try:
            rospy.wait_for_service('/sawyer_grasp', 5.0)
        except rospy.ROSException as e:
            self.logger.warning(e)
            return "timeout"
               
        sawyer_grasp = rospy.ServiceProxy('sawyer_grasp', Grasp)
        outputData = str(sawyer_grasp('operate', degree))
        outputData = outputData[7:] # delete 'result: ' and convert to bool

        self.logger.info(outputData)
        
        rospy.sleep(2)
        
        if 'True' in outputData:
            self.logger.info("Success")
            return 1
            
        else:
            self.logger.info("Fail")
            return 0 # fail
