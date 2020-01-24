
def execute(self, inputs, outputs, gvm):
    
    poseStamped = inputs["poseStamped"]
    
    x = poseStamped.pose.position.x
    y = poseStamped.pose.position.y
    xy_vector = (x, y)

    outputs["xy_vector"] = xy_vector
    return 0
