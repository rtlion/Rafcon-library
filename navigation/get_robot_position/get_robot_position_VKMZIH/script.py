import rospy
import tf
import tf2_ros
import tf2_geometry_msgs
import numpy
import pickle
import math
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

def execute(self, inputs, outputs, gvm):

    odom_timeout = inputs["odom_timeout"]
    odom_topic = inputs["odom_topic"]

    odometry_msg = None
    try:
        odometry_msg = rospy.wait_for_message(odom_topic, Odometry, odom_timeout)
    except Exception as e:
        self.logger.warn("Exception during wait for odom: \n{0}".format(e))
            
    odomPose = odometry_msg.pose.pose
    odomPoseStamped = PoseStamped(
        pose=odomPose
    )
    odomPoseStamped.header.frame_id="odom"
    
    tfListener = tf.TransformListener()
    #robot_position = tfListener.transformPose("map", odomPoseStamped)

    tf_buffer = tf2_ros.Buffer(rospy.Duration(10.0))  # tf buffer length
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    transform_odom_to_map = tf_buffer.lookup_transform(
        'map', # target frame
        odomPoseStamped.header.frame_id,  # source frame
        rospy.Time(0),  # get the tf at first available time
        rospy.Duration(1.0)  # wait for 1 second
    )
    robot_position = tf2_geometry_msgs.do_transform_pose(odomPoseStamped, transform_odom_to_map)

    outputs["robot_poseStamped"] = robot_position
    return 0
