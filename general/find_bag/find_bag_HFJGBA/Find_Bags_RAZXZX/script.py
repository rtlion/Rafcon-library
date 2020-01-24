import rospy
from rtl_comm.srv import *

def execute(self, inputs, outputs, gvm):
    self.logger.info("STATUS: Finding Bag Positions")
    
    rospy.loginfo ("Getting object pose")
    rospy.wait_for_service('/enableCapture', 10)
    enabler = rospy.ServiceProxy('/enableCapture', enableCapture)
    enabler(True) # enable Capture
    rospy.sleep(3)
    

    self.logger.info("Getting obj Pose")
    rospy.wait_for_service('getObjPose',10)
    try:
        gripPoint = rospy.ServiceProxy('getObjPose', getObjPose)
        resp = gripPoint(0)   # Argument is dummy, to get pose of 1st object detected
        rospy.wait_for_service('enableCapture',10)
        enabler(False)
        pose = resp.objPose
        self.logger.info("Pose: {}".format(pose))
        
        outputs['bag_position'] = pose
        
        return "success"
        
    except rospy.ServiceException, e:
        rospy.loginfo("Service call failed: %s"%e)
        self.logger.info("Service call failed: {}".format(e))
        rospy.wait_for_service('enableCapture',5)
        enabler(False)
        return "fail"
    