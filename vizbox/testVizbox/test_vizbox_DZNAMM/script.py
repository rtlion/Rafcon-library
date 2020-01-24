import rospy

def execute(self, inputs, outputs, gvm):
    self.logger.debug("Hello world")
    
    self._title = rospy.get_param("story/title", "Challenge")
    self._storyline = rospy.get_param("story/storyline", ["Start"])
    
    self.logger.info("Challenge: {}\nStoryline: {}".format(self._title, self._storyline))
        
    return 0
