import rospy
from itchy_hands.srv import * 

def execute(self, inputs, outputs, gvm):
    
    testMode = inputs['testMode']
    
    self.logger.info("Saywer move to home after picking up garbage!")
    
    if testMode:
        import time
        time.sleep(0.5)
        return 1 # success
        
    else:
        callArguments = ['rosservice','call','/sawyer_move', 'pos_gbghome']
        rospy.wait_for_service('/sawyer_move', 3.0)
        sawyer_grasp = rospy.ServiceProxy('sawyer_move', MoveSawyer)
        outputData = str(sawyer_grasp('pos_home', 0))
        outputData = outputData[7:] # delete 'result: ' and convert to bool

        self.logger.info(outputData)
        
        if 'True' in outputData:
            return 1 # success
        else:
            return 0 # fail
