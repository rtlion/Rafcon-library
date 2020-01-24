import rospy

def execute(self, inputs, outputs, gvm):
    
    start_time = inputs["start_time"]
    timeout = inputs["timeout"]

    if start_time == -1:
        start_time = rospy.Time.now()
    
    
    now = rospy.Time.now.secs
    
    time_has_wrapped_around = (now < start_time)
    is_timed_out = (now - start_time >= timeout)
    
    if time_has_wrapped_around or is_timed_out:
        return 1

    self.logger.debug("waiting 1 sec")
    rospy.sleep(1.0)

    outputs["start_time"] = start_time

    return 0
