

HAS_CHANGED = 0
HAS_NOT_CHANGED = 1

def execute(self, inputs, outputs, gvm):

    global HAS_CHANGED, HAS_NOT_CHANGED
    
    room_history = inputs["room_history"]
    room_history_length = len(room_history)
    
    if room_history_length <= 0:
        outputs["has_room_changed"] = False
        return HAS_NOT_CHANGED
    
    if room_history_length == 1:
        outputs["new_room"] = room_history[0]
        outputs["old_room"] = None
        outputs["has_room_changed"] = True
        return HAS_CHANGED
    
    new_room = room_history[room_history_length - 1]
    old_room = room_history[room_history_length - 2]
    outputs["new_room"] = new_room
    outputs["old_room"] = old_room
    
    if new_room == old_room:
        outputs["has_room_changed"] = False
        return HAS_NOT_CHANGED
    else:
        outputs["has_room_changed"] = True
        return HAS_CHANGED
