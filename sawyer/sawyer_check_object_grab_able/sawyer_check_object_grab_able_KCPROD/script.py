import rospy
from itchy_hands.srv import * 

def execute(self, inputs, outputs, gvm):
    
    testMode = inputs['testMode']
    dataDict = inputs['dataDict']
    
    try:
        x = dataDict['x']
        y = dataDict['y']
        width = dataDict['w']
        height = dataDict['h']
        
        objectName = dataDict['label']
        
    except KeyError as e:
        self.logger.info("Key Error in dataDict! Can not find {} in dict!".format(e))
        return -1
    
    if dataDict is None:
        self.logger.info("Error!!! - Data Dict is None! Aborting...")
        return -1
    
    self.logger.info("Sawyer - Check if object '{}' is grabable....".format(objectName))
    
    if testMode:
        import time
        time.sleep(0.5)
        
        from random import randint
        if randint(0,5) >= 1:
            self.logger.info("Object is grabable!")
            return "success"
            
        else:
            self.logger.info("Object is not grabable!")
            return "fail"
        
    else:
        rospy.wait_for_service('/sawyer_move')
        sawyer_grasp = rospy.ServiceProxy('sawyer_send', MoveSawyer)
        
        outputData = str(sawyer_grasp('boundingBox', x, y, width, height))
        outputData = outputData[7:] # delete 'result: ' and convert to bool

        self.logger.info(outputData)
        
        if 'True' in outputData:
            
            self.logger.info("Object is grabable!")
            return "success"
            
        else:
            self.logger.info("Object is not grabable!")
            return "fail"
