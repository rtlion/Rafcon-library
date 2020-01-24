import rospy
from itchy_hands.srv import * 

def execute(self, inputs, outputs, gvm):
    
    testMode = inputs['testMode']
    
    self.logger.info("Saywer grasp - check if object in gripper!")
    
    if testMode:
        import time
        time.sleep(0.5)
        
        from random import randint
        if randint(0,1) >= 1:
            return 1 # success
        else:
            return 0 # fail
        
    else:            
    
     
        try:
            rospy.wait_for_service('/sawyer_grasp', 5.0)
        except rospy.ROSException as e:
            self.logger.warning(e)
            return "timeout"
        
        sawyer_grasp = rospy.ServiceProxy('sawyer_grasp', Grasp)
        outputData = str(sawyer_grasp('success', 0))
        outputData = outputData[7:] # delete 'result: ' and convert to bool

        self.logger.info(outputData)
        
        if 'True' in outputData:
            self.logger.info("!Object in Gripper!") 
            return "success"
        else:
            self.logger.info("Fail! Object not in Gripper!")
            return "fail"
