import rospy
from itchy_hands.srv import * 

def execute(self, inputs, outputs, gvm):
    
    testMode = inputs['testMode']
    
    self.logger.info("Saywer rotate!")
    
    if testMode:
        import time
        time.sleep(0.5)
        return 1 # success
        
    else:
        zRotation = inputs['zRotation']
        
        self.logger.info("Rotate sawyer to z: {z}".format(z=zRotation))
    
        rospy.wait_for_service('/sawyer_move', 5.0)
        sawyer_grasp = rospy.ServiceProxy('sawyer_move', MoveSawyer)
        outputData = str(sawyer_grasp('rotateZ', zRotation))
        outputData = outputData[7:] # delete 'result: ' and convert to bool

        self.logger.info(outputData)
        
        if 'True' in outputData:
            return 1 # success
        else:
            return 0 # fail
