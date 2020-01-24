import rospy
from rtl_comm.srv import *
from geometry_msgs.msg import Point

def execute(self, inputs, outputs, gvm):
    
    dataDict = inputs['dataDict']
    objLabel = dataDict['label']
    
    self.logger.info("Trying to move to the {}".format(objLabel))
    
    x = dataDict['x']
    y = dataDict['y']
    width = dataDict['w']
    height = dataDict['h']
    
    
    '''
    # --- challenge mode !!!
    # set parameter
    paramDict = {'x': x, 'y': y, 'w': width, 'h': height} 
    rospy.set_param('boundingBox', paramDict)
    
    # call service
    rospy.wait_for_service('/', 10)
    closestObj = rospy.ServiceProxy('', getClosestObj)
    # -----
    '''
    
    # --- TEST MODE ----
    rospy.wait_for_service('/sawyer_move', 4.0)
    sawyer_grasp = rospy.ServiceProxy('sawyer_move', MoveSawyer)
    outputData = str(sawyer_grasp('dummyObjGrasp', 0))
    outputData = outputData[7:] # delete 'result: ' and convert to bool
    # --------------------------
    
    
    self.logger.info(outputData)
        
    if 'True' in outputData:
        self.logger.info("Succceded going to the object '{}'! Ready for grasping!".format(objLabel))
        return "success"
    else:
        self.logger.info("Failed going to the object '{}'!".format(objLabel))
        return "fail"

