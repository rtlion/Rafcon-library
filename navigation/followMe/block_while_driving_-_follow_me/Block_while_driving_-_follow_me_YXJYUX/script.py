
import rospy
from geometry_msgs.msg import Twist

segeln = False #

def execute(self, inputs, outputs, gvm):

    def cb_segeln(twist):
        global segeln
        # play toggle on velocity != 0
        b = ((twist.linear.x + twist.linear.y + twist.angular.z) != False) # & (not halt)
        #self.logger.info(b)
        #self.logger.info("CB Segeln b: {}".format(b))
        if b != segeln:
          segeln = b
        
        rospy.sleep(0.5)  # block callback thread to throttle

    rospy.Subscriber("/cmd_vel", Twist, cb_segeln, queue_size=1)
    
    maxWait = 5
    counter = 0

    while counter < maxWait:
        if segeln == False:
            # we don't drive -> increase counter
            counter += 1
            self.logger.info("Waiting to move... (%ds)" % counter)
        else:
            # we drive -> reset counter
            counter = 0
            self.logger.info("They see me rolling...")
        
        # wait a second
        rospy.sleep(1)
        
    self.logger.info("Didn't start moving in %ds" % counter)
    return "maxTimeWaited"