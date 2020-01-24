# tw 2019-06-09T23:08
import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Header
import cPickle as pickle
import os


def execute(self, inputs, outputs, gvm):

    self.logger.info("Creating waypoint to pose...")
    
    waypointPickled = inputs['waypointPickled']
    pose = pickle.loads(waypointPickled)

    # waypoint No to pose
    out = PoseStamped(
        header=Header(frame_id='map'),
        pose=pose
    )
    #self.logger.info("created new PoseStamped %r" % out)
    outputs["poseStamped"] = out
    return "success"

