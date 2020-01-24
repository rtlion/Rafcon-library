import rospy
from itchy_hands.srv import * 

def execute(self, inputs, outputs, gvm):
    
    testMode = inputs['testMode']
    
    self.logger.info("Saywer grasp - Trying to go to the object...")
    
    if testMode:
        import time
        time.sleep(0.5)
        
        from random import randint
        if randint(0,20) == 4:
            self.logger.info("Succceded going to the object! Ready for grasping!")
            return 1 # success
        else:
            self.logger.info("Failed going to the object!")
            return 0 # fail
        
        
    else:
        
        try:
            #rospy.wait_for_service('/sawyer_grasp', 5.0)
            rospy.wait_for_service('/sawyer_move', 5.0)
        except rospy.ROSException as e:
            self.logger.warning(e)
            return "timeout"
        
        #sawyer_grasp = rospy.ServiceProxy('sawyer_grasp', Grasp)
        sawyer_grasp = rospy.ServiceProxy('sawyer_move', Grasp)
        #outputData = str(sawyer_grasp('gotoObj', 0))
        outputData = str(sawyer_grasp('pos_collect_gbg', 0))        
        outputData = outputData[7:] # delete 'result: ' and convert to bool

        self.logger.info(outputData)
        
        if 'True' in outputData:
            self.logger.info("Succceded going to the object! Ready for grasping!")
            return "success"
        else:
            self.logger.info("Failed going to the object!")
            return "fail"
