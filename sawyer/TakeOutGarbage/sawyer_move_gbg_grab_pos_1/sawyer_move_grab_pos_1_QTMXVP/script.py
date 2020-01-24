import rospy
from itchy_hands.srv import * 

def execute(self, inputs, outputs, gvm):
    
    testMode = inputs['testMode']
    
    self.logger.info("Saywer move to grab position 1!")
    
    if testMode:
        import time
        time.sleep(0.5)
        
        from random import randint
        if randint(0,5) >= 1:
            self.logger.info("Successfully went to grasping position 1!")
            return 1 # success
            
        else:
            self.logger.info("Failed to go to grasping position 1!")
            return 0 # fail
        
    else:
        
        rospy.wait_for_service('/sawyer_move')
        sawyer_grasp = rospy.ServiceProxy('sawyer_move', MoveSawyer)
        outputData = str(sawyer_grasp('pos_gbg1', 0))
        outputData = outputData[7:] # delete 'result: ' and convert to bool

        self.logger.info(outputData)
        
        if 'True' in outputData:
            
            # return the grab position for later use
            outputs['grabPosition'] = 1
            
            self.logger.info("Successfully went to grasping position 1!")
            return 1 # success
            
        else:
            self.logger.info("Failed to go to grasping position 1!")
            return 0 # fail
