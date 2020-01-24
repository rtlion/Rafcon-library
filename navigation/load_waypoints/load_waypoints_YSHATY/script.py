import pickle

def execute(self, inputs, outputs, gvm):
    path_to_file = inputs["path_to_file"]
    file = open(path_to_file)
    pickled_waypoints = file.read()
    outputs["pickled_waypoints"] = pickled_waypoints
    return 0
