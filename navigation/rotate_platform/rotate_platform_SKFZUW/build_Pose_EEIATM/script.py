import rospy
from geometry_msgs.msg import PoseStamped
import tf
import tf2_ros
import tf2_geometry_msgs
import math

def execute(self, inputs, outputs, gvm):
    
    baseFrame = inputs['base_frame']
    
    # position expects value in meters -> divide by 100
    degree = inputs['degree']
    radians = math.radians(degree)
    direction = inputs['direction']
    
    # bag pose frame
    poseStamped = PoseStamped()
    poseStamped.header.stamp = rospy.Time.now()
    poseStamped.header.frame_id = baseFrame

        
    if direction == 'left':
        # roll | pitch | yaw
        self.logger.info("Rotating the plattform to the left with {} degree's".format(degree))
        quaternion = tf.transformations.quaternion_from_euler(0, 0, radians)
        
    elif direction == 'right':
        # roll | pitch | yaw
        self.logger.info("Rotating the plattform to the right with {} degree's".format(degree))
        radians = -1 * radians
        quaternion = tf.transformations.quaternion_from_euler(0, 0, radians)
    
    else:
        self.logger.info("The entered direction '{}' is invalid!\nUse 'left' or 'right'!".format(direction))
        return 'invalidParams'
    
    poseStamped.pose.position.x = 0        
    poseStamped.pose.position.y = 0
    poseStamped.pose.position.z = 0

    # roll | pitch | yaw
    #quaternion = tf.transformations.quaternion_from_euler(0, 0, degree)

    poseStamped.pose.orientation.x = quaternion[0]
    poseStamped.pose.orientation.y = quaternion[1]
    poseStamped.pose.orientation.z = quaternion[2]
    poseStamped.pose.orientation.w = quaternion[3]

    #self.logger.info("{}".format(poseStamped))
    
    # transform to map frame 
    self.logger.info("Transforming pose relative to map")
    tf_buffer = tf2_ros.Buffer(rospy.Duration(1200.0))  # tf buffer length
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    transform_base_to_map = tf_buffer.lookup_transform(
        'map', # target frame
        baseFrame,  # source frame
        rospy.Time(0),  # get the tf at first available time
        rospy.Duration(1.0)  # wait for 1 second
    )

    mapPose = tf2_geometry_msgs.do_transform_pose(poseStamped, transform_base_to_map)
    self.logger.info("Finished transform")


    
    degreeAbs = abs(degree % 360)
    # 3 sec + ( 1 sek for each 15 degree)
    maxWaitForResult = int(round(3 + min(degreeAbs, 360 - degreeAbs) * 12/180))
    self.logger.info("Max wait time: {}".format(maxWaitForResult))
    
    
    
    outputs['poseStamped'] = mapPose
    outputs['maxTimeWait'] = maxWaitForResult
    
    return 'success'
