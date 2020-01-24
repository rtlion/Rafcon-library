
from geometry_msgs.msg import PoseStamped
import tf
import cPickle as pickle
import math

def euclidean_distance_between(pose1, pose2):
    delta_x = pose1.position.x - pose2.position.x
    delta_y = pose1.position.y - pose2.position.y
    # delta_z is always 0
    return math.sqrt(delta_x ** 2 + delta_y ** 2)
    
transform = tf.TransformListener()
def transform_to_map(poseStamped):
    if poseStamped.header.frame_id == "map":
        return poseStamped
    else:
        global transform 
        return transform.transformPose("map", poseStamped)

def execute(self, inputs, outputs, gvm):
    
    center_poseStamped = pickle.loads(inputs["center_poseStamped_pickled"])
    waypoints = pickle.loads(inputs["waypoints_pickled"]) 
    
    self.logger.info("calculating nearest neighbor")
    self.logger.debug("center pose: \n{0}".format(center_poseStamped))
    self.logger.debug("neighbors: \n{0}".format(waypoints))
    
    # transform center pose to map if it isn't already
    center_pose_map = None
    if center_poseStamped.header.frame_id == "map":
        center_pose_map = center_poseStamped
    else:
        center_pose_map = transform_to_map(center_poseStamped)
    
    # calculate all euclidean distances -> minimum is nearest neighbor
    nearest_waypoint_id = -1
    nearest_waypoint_distance = -1
    
    for waypoint_id in waypoints:
        waypoint_pose = waypoints[waypoint_id]
    
        # calculate distance
        distance = euclidean_distance_between(center_pose_map.pose, waypoint_pose)
        
        is_initial_state = nearest_waypoint_id == -1
        if is_initial_state:
            nearest_waypoint_id = waypoint_id
            nearest_waypoint_distance = distance
            continue
        
        is_closer = (distance < nearest_waypoint_distance)
        if is_closer:
            nearest_waypoint_id = waypoint_id
            nearest_waypoint_distance = distance
            
    nearest_waypoint = waypoints[nearest_waypoint_id]
    
    self.logger.info("nearest waypoint id is {0}".format(nearest_waypoint_id))
    self.logger.debug("nearest waypoint is \n{0}".format(nearest_waypoint))
    
    outputs["nearest_waypoint_id"] = nearest_waypoint_id
    outputs["nearest_waypoint_distance"] = nearest_waypoint_distance
    outputs["nearest_waypoint_pose"] = nearest_waypoint
        

    self.logger.debug("Hello world")
    return 0
