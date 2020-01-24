
import cPickle as pickle

def execute(self, inputs, outputs, gvm):
    
    bedroom_path = inputs["bedroom_path"]
    kitchen_path = inputs["kitchen_path"]
    office_path = inputs["office_path"]
    livingroom_path = inputs["livingroom_path"]
    
    room_names_to_room_borders_dict = {
        "bedroom" : bedroom_path,
        "kitchen" : kitchen_path,
        "office" : office_path,
        "living room" : livingroom_path
    }
    
    outputs["room_names_to_room_borders_dict"] = room_names_to_room_borders_dict
    
    self.logger.info("loaded room_names_to_room_borders_dict")
    self.logger.verbose("room_names_to_room_borders_dict: \n{0}".format(room_names_to_room_borders_dict))
    
    return 0
