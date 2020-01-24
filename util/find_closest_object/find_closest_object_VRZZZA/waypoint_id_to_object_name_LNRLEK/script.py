# this has hardcoded information!!!

def execute(self, inputs, outputs, gvm):

    object_waypoint_id = inputs[" waypoint_id"]
    
    
    waypoint_to_object_mapping = {
        1: "trash bin",
        2: "sideboard",
        3: "couch",
        4: "couch",
        5: "coffee table",
        6: "display cabinet",
        7: "display cabinet",
        8: "plant",
        9: "armchair",
        10: "TV",
        11: "door to the office"
    }
        
    object_name = waypoint_to_object_mapping[object_waypoint_id]
    
    self.logger.debug("waypoint to object")
    self.logger.debug("waypoint_id is {0}".format(object_waypoint_id))
    self.logger.debug("mappings are: \n{0}".format(waypoint_to_object_mapping))
    self.logger.debug("object name is {0}".format(object_name))
    
    outputs["object_name"] = object_name
    
    return 0
