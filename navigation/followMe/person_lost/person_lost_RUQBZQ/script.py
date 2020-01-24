import rospy
from std_msgs.msg import Bool

personInSight = None

def execute(self, inputs, outputs, gvm):
    global personInSight
    
    #personInSight = inputs['personInSight']
    #self.logger.info("-----------------------------------------------")
    #self.logger.info("Person in sight value: {}".format(personInSight))
    #self.logger.info("-----------------------------------------------")
    
       
    def humanDetectedCallback(data):
        self.logger.info("Human Decteded Callback - data: {}".format(data.data))
        self.logger.info("callback data: {}".format(data))
        global personInSight
        personInSight = data.data
    
    sub = rospy.Subscriber('/followMe/human_selected_flag', Bool, humanDetectedCallback, queue_size=1)
    
    counter = 0
    
    while personInSight == None and counter < 50: #5 sec
        counter += 1
        rospy.sleep(0.1)
        #self.logger.info("Waiting for data")
    
    if personInSight:
        self.logger.info("Person still in sight!")
	return "personInSight"
        
    if personInSight is False:
        self.logger.info("Person not in sight anymore")
        return "personLost"

    else:
        self.logger.info("Unknown person in sight value! It is: {}".format(personInSight))
        return "personLost"
    
        
        
    """
    #rospy.sleep(10) # Slep
    import time
    time.sleep(10)
    
    
    personInSight = None
    
    #if rospy.has_param('follows'):
        #self.logger.info("Set follows param")
    personInSight = rospy.get_param('follows')
    """ 
    

