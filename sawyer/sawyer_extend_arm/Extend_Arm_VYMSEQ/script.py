import rospy
from itchy_hands.srv import * 

def execute(self, inputs, outputs, gvm):
    
    testMode = inputs['testMode']
    
    self.logger.info("Trying to move arm to looking position")
    
    if testMode:
        import time
        time.sleep(0.5)
        
        from random import randint
        if randint(0,5) >= 1:
            self.logger.info("Successfully moved to position")
            return "success"
            
        else:
            self.logger.info("Failed to move to position")
            return "fail"
        
    else:
        rospy.wait_for_service('/sawyer_move')
        sawyer_grasp = rospy.ServiceProxy('sawyer_move', MoveSawyer)
        outputData = str(sawyer_grasp('pos_extendHook', 0))
        outputData = outputData[7:] # delete 'result: ' and convert to bool

        self.logger.info(outputData)
        
        if 'True' in outputData:
            
            self.logger.info("Succesfully opened shelf door!")
            return "success"
            
        else:
            self.logger.info("Failed to open shelf door!")
            return "fail"
