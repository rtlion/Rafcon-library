import rospy

def execute(self, inputs, outputs, gvm):
    
    challengeName = inputs['challenge'] 
    storyLine = inputs['storyLine']
    
    rospy.set_param("story/title", challengeName)
    rospy.set_param("story/storyline", storyLine)
    
    #self.logger.info("{}".format(vizbox))
    
    vizboxCounter = 0
    gvm.set_variable('vizbox_counter',vizboxCounter, per_reference=True)
    
    self.logger.info("Vizbox parameters set")
    
    return 0
