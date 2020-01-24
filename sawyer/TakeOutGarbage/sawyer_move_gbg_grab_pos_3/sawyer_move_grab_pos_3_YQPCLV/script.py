import rospy
from itchy_hands.srv import * 

def execute(self, inputs, outputs, gvm):
    
    testMode = inputs['testMode']
    
    self.logger.info("Saywer move grab position 3!")
    
    if testMode:
        import time
        time.sleep(0.5)
        return 1 # success
    else:
    
        callArguments = ['rosservice','call','/sawyer_move', 'gbg3']
        rospy.wait_for_service('/sawyer_move')
        sawyer_grasp = rospy.ServiceProxy('sawyer_move', MoveSawyer)
        outputData = str(sawyer_grasp('pos_gbg3', 0))
        outputData = outputData[7:] # delete 'result: ' and convert to bool

        self.logger.info(outputData)
        
        if 'True' in outputData:
            # return the grab position for later use
            outputs['grabPosition'] = 3
            
            return 1 # success
            
        else:
            return 0 # fail