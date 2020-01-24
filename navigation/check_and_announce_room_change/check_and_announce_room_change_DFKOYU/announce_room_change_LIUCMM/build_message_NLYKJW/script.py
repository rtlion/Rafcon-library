
def execute(self, inputs, outputs, gvm):
    
    old_room = inputs["old_room"]
    new_room = inputs["new_room"]
    enter_room_template = inputs["enter_room_template"]
    leave_room_template = inputs["leave_room_template"]
    
    message = ""
    
    if old_room is None:
        message = leave_room_template.format(old_room)
    
    message += new_room.format(new_room)
    
    outputs["message"] = message
    return 0
