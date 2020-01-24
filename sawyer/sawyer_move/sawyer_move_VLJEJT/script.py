import rospy
from itchy_hands.srv import * 

def execute(self, inputs, outputs, gvm):
    
    infoStr = inputs['infoText']
    callParam = inputs['callParam']
    
    self.logger.info("{info} --- call param: {callP}".format(info = infoStr, callP = callParam))
    
    try:
        rospy.wait_for_service('/sawyer_move', 10.0)
    except rospy.ROSException as e:
        self.logger.warning(e)
        return "timeout"
    
    sawyer_grasp = rospy.ServiceProxy('sawyer_move', MoveSawyer)
    outputData = str(sawyer_grasp(callParam, 0))
    outputData = outputData[7:] # delete 'result: ' and convert to bool

    self.logger.info("Output data: {}".format(outputData))
    
    if 'True' in outputData:
        return 'success'
    else:
        return 'fail'