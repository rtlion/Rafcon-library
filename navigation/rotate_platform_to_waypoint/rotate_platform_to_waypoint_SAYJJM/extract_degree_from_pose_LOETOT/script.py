import rospy
import tf
import tf2_ros
import tf2_geometry_msgs
import numpy
import pickle
import math

from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Header
from nav_msgs.msg import Odometry

def unit_vector(vector):
  return vector / numpy.linalg.norm(vector)

def angle_between(v1, v2):
  v1_u = unit_vector(v1)
  v2_u = unit_vector(v2)
  return numpy.arccos(numpy.clip(numpy.dot(v1_u, v2_u), -1.0, 1.0))

def execute(self, inputs, outputs, gvm):
    
    self.logger.info("Extracting degree from pose...")
    
    facePoseStamped = inputs['poseStamped']
    
    odomTopic = '/odometry'
    
    # try to get the odemtry pose
    odometryMsg = None
    try:
        odometryMsg = rospy.wait_for_message(odomTopic, Odometry, 3.0)
    except Exception as e:
        self.logger.warning(e)
        
        odomAltTopic = '/odom'
        try:
            odometryMsg = rospy.wait_for_message(odomAltTopic, Odometry, 3.0)
        except Exception as e:
            # should not happen ever!!!
            self.logger.error(e)
            return -1
            
    odomPose = odometryMsg.pose.pose
    odomPoseStamped = PoseStamped(
        header=Header(frame_id="odom"),
        pose=odomPose
    )
    
    tfListener = tf.TransformListener()
    # transform relative to map
    
    #self.logger.info("Odom Pose Stamped: {}".format(odomPoseStamped))
    #self.logger.info("Face Pose Stamped: {}".format(facePoseStamped))
    
    
    #currentPoseStamped = tfListener.transformPose("base_link", odomPoseStamped)

    # transform to map frame 
    tf_buffer = tf2_ros.Buffer(rospy.Duration(10.0))  # tf buffer length
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    transform_odom_to_base_link = tf_buffer.lookup_transform(
        'base_link', # target frame
        odomPoseStamped.header.frame_id,  # source frame
        rospy.Time(0),  # get the tf at first available time
        rospy.Duration(1.0)  # wait for 1 second
    )
    currentPoseStamped = tf2_geometry_msgs.do_transform_pose(odomPoseStamped, transform_odom_to_base_link)
    
    #self.logger.info("Current Pose: {}".format(currentPoseStamped))


    # transform facepose
    #facePoseStamped_base_link = tfListener.transformPose("base_link", facePoseStamped)
    tf_buffer = tf2_ros.Buffer(rospy.Duration(10.0))  # tf buffer length
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    transform_facePose_to_base_link = tf_buffer.lookup_transform(
        'base_link', # target frame
        facePoseStamped.header.frame_id,  # source frame
        rospy.Time(0),  # get the tf at first available time
        rospy.Duration(1.0)  # wait for 1 second
    )
    facePoseStamped_base_link = tf2_geometry_msgs.do_transform_pose(facePoseStamped, transform_facePose_to_base_link)
    
    
    x = facePoseStamped_base_link.pose.position.x - currentPoseStamped.pose.position.x
    y = facePoseStamped_base_link.pose.position.y - currentPoseStamped.pose.position.y
    
    # radian angle
    angle = angle_between((x,y), (1,0))
    
    # convert to degree
    angleDegrees = math.degrees(angle)
    outputs['degree'] = int(angleDegrees)
    
    if y < 0:
        outputs['direction'] = 'left'
    else:
        outputs['direction'] = 'right'


    return 0