import rospy
from itchy_hands.srv import * 

def execute(self, inputs, outputs, gvm):
    
    testMode = inputs['testMode']
    
    self.logger.info("Saywer trying to move to table...")
    
    if testMode:
        import time
        time.sleep(0.5)
        
        from random import randint
        if randint(0,5) >= 1:
            self.logger.info("Successfully moved to table!")
            return "success"
            
        else:
            self.logger.info("Failed to move to the table!")
            return "fail"
        
    else:
        rospy.wait_for_service('/sawyer_move', 2.0)
        sawyer_grasp = rospy.ServiceProxy('sawyer_move', MoveSawyer)
        outputData = str(sawyer_grasp('pos_table_1', 0))
        outputData = outputData[7:] # delete 'result: ' and convert to bool

        self.logger.info(outputData)
        
        if 'True' in outputData:
            
            self.logger.info("Successfully moved to table!")
            return "success"
            
        else:
            self.logger.info("Failed to move to the table!")
            return "fail"
