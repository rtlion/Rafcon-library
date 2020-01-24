
MAX_HISTORY_LENGTH = 20

def execute(self, inputs, outputs, gvm):

    global HISTORY_LENGTH 
    
    room_history = inputs["room_history"]
    room_name = inputs["room_name"]
    
    if room_history is None:
        room_history = []
    
    room_history.append(room_name)
    
    # remove old history if necessary
    room_history_length = len(room_history)
    if room_history_length > MAX_HISTORY_LENGTH:
        number_of_elements_to_remove = room_history_length - MAX_HISTORY_LENGTH
        room_history = room_history[number_of_elements_to_remove : ]
    
    outputs["room_history"] = room_history
    return 0
