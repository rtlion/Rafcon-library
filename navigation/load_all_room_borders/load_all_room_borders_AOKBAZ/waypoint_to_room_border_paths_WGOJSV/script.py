import cPickle as pickle
import matplotlib.path as path

def execute(self, inputs, outputs, gvm):
    waypoints = pickle.loads(inputs["waypoints_pickled"])
    waypoints_xy = {}
    
    ids_bedroom = [2, 3, 6, 9, 5]
    ids_kitchen = [9, 6, 8, 7]
    ids_office = [1, 2, 5, 4]
    ids_livingroom = [4, 5, 9, 8, 10]
    
    for waypoint_id in waypoints:
        waypoint_pose = waypoints[waypoint_id]
        x = waypoint_pose.x
        y = waypoint_pose.y
        xy_vector = (x, y)
        waypoints_xy[waypoint_id] = xy_vector
    
    bedroom_path = []
    for id in ids_bedroom:
        bedroom_path.append(waypoints_xy[id])
        
    kitchen_path = []
    for id in ids_kitchen:
        kitchen_path.append(waypoints_xy[id])
    
    office_path = []
    for id in ids_office:
        office_path.append(waypoints_xy[id])
    
    livingroom_path = []
    for id in ids_livingroom:
        livingroom_path.append(waypoints_xy[id])
    
    outputs["bedroom_path"] = bedroom_path
    outputs["kitchen_path"] = kitchen_path
    outputs["office_path"] = office_path
    outputs["livingroom_path"] = livingroom_path
    
    return 0
