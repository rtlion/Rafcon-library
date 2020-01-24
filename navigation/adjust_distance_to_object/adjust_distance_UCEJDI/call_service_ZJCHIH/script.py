import rospy
from rtl_comm.srv import * 

def execute(self, inputs, outputs, gvm):
    
    try:
        rospy.wait_for_service('/to_the_plank', 5.0)
    except rospy.ROSException as e:
        self.logger.warning(e)
        return "timeout"
    
    wallDistance = rospy.ServiceProxy('to_the_plank', ReturnFloat64)
    
    # compare with parameter / solver
    compareValue = wallDistance.data
    
    # oder anders herum?
    #movePlattformInCM = compareValue - value
    movePlattformInCM = compareValue - rospy.get_param('/neobotix/soll_distance', 95.0)    
    
    # decide if we should move or not move
    if abs(movePlattformInCM) <= 5:
        return "dontMove"
        
    if abs(movePlattformInCM) > 25:
        # if the distance is very big, try to move to the waypoint again
        return "moveBaseAgain"
    
    
    # decide the direction
    if movePlattformInCM >= 0:
        direction = "forward"
    else:
        direction = "backward"  
      
    outputs['movePlattformInCM'] =  movePlattformInCM
    outputs['direction'] = direction
    
    return "success"