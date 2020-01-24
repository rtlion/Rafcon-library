
import cPickle as pickle
from matplotlib import path
from geometry_msgs.msg import PoseStamped

def execute(self, inputs, outputs, gvm):

    waypoints = pickle.loads(inputs["waypoints_pickled"])
    
    self.logger.debug("converting waypoints to xy")
    xy_points = []
    
    for waypoint_id in waypoints:
        waypoint = waypoints[waypoint_id]
        x = waypoint.position.x 
        y = waypoint.position.y
        point = (x, y)
        xy_points.append(point)
    
    outputs["path"] = path.Path(xy_points)
    self.logger.debug("path is: {0}".format(outputs["path"]))
    return 0 
