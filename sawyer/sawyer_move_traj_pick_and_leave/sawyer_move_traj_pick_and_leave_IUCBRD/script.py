import rospy
from itchy_hands.srv import * 

def execute(self, inputs, outputs, gvm):
    
    testMode = inputs['testMode']
    
    self.logger.info("Saywer move (traj) pick and leave!")
    
    if testMode:
        import time
        time.sleep(0.5)
        return 1 # success
        
    else:
        callArguments = ['rosservice','call','/sawyer_move', 'traj_gbgpicknleave']
        rospy.wait_for_service('/sawyer_move')
        sawyer_grasp = rospy.ServiceProxy('sawyer_move', MoveSawyer)
        outputData = str(sawyer_grasp('traj_gbgpicknleave', 0))
        outputData = outputData[7:] # delete 'result: ' and convert to bool

        self.logger.info(outputData)
        
        if 'True' in outputData:
            return 1 # success
        else:
            return 0 # fail
