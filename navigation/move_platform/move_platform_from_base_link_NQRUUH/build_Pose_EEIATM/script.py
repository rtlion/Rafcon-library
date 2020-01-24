import rospy
from geometry_msgs.msg import PoseStamped

def execute(self, inputs, outputs, gvm):
    
    baseFrame = inputs['base_frame']
    
    # position expects value in meters -> divide by 100
    moveAmountCM = inputs['moveAmountCM'] / 100.0
    direction = inputs['direction']
    
    # bag pose frame
    poseStamped = PoseStamped()
    poseStamped.header.stamp = rospy.Time.now()
    poseStamped.header.frame_id = baseFrame
    
    if direction == 'forward':
        self.logger.info("Moving plattform {}cm forward".format(moveAmountCM))
        poseStamped.pose.position.x = moveAmountCM
        poseStamped.pose.position.y = 0    
    
    elif direction == 'backward':
        self.logger.info("Moving plattform {}cm backward".format(moveAmountCM))
        moveAmountCM = -1 * moveAmountCM
        poseStamped.pose.position.x = moveAmountCM     
        poseStamped.pose.position.y = 0
        
    elif direction == 'left':
        self.logger.info("Moving plattform {}cm left".format(moveAmountCM))
        poseStamped.pose.position.x = 0        
        poseStamped.pose.position.y = moveAmountCM
        
    elif direction == 'right':
        self.logger.info("Moving plattform {}cm right".format(moveAmountCM))
        moveAmountCM = -1 * moveAmountCM
        poseStamped.pose.position.x = 0        
        poseStamped.pose.position.y = moveAmountCM
    
    else:
        self.logger.info("The entered direction '{}' is invalid!\nUse 'forward', 'backward', 'left' or 'right'!".format(direction))
        return 'invalidParams'
    
    
    poseStamped.pose.position.z = 0

    # orientation
    poseStamped.pose.orientation.x = 0
    poseStamped.pose.orientation.y = 0
    poseStamped.pose.orientation.z = 0
    poseStamped.pose.orientation.w = 1
    
    outputs['poseStamped'] = poseStamped
    
    return 'success'
