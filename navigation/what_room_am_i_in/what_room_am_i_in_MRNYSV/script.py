
import rospy
import matplotlib.path as path

SUCCESS = 0
UNKNOWN = 1

def execute(self, inputs, outputs, gvm):

    global UNKNOWN, SUCCESS

    room_name_to_border_paths_dict = inputs["room_names_to_border_paths_dict"]
    robot_position_xy = inputs["robot_position_xy_vector"]
    
    self.logger.verbose("attempting to identify current room")
    self.logger.verbose("robot position is: {0}".format(robot_position_xy))

    found_room_name = None
    for room_name in room_name_to_border_paths_dict:
        border_path = room_name_to_border_paths_dict[room_name]
        is_inside = border_path.contains_points(robot_position_xy)

        if is_inside:
            found_room_name = room_name
            break

    if found_room_name is None:
        self.logger.warn("could not identify current room")
        return UNKNOWN

    outputs["room_name"] = found_room_name
    self.logger.verbose("I am currently in the {0}".format(found_room_name))
    return SUCCESS
