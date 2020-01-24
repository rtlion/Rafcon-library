import rospy
from threading import Timer
from geometry_msgs.msg import Twist



def execute(self, inputs, outputs, gvm):
    
    self.logger.info("Starting timer")
    
    self.robotIsDriving = False
    self.timerRunning = False
    
    # create a Timer
    t = Timer(10, timeout)
    
    def cb_driving(self, twist):
    
        # play toggle on velocity != 0
        self.robotIsDriving = (twist.linear.x + twist.linear.y) != 0
        
        rospy.loginfo(self.robotIsDriving)
        self.logger.info(self.robotIsDriving)
    
        if self.timerRunning:
            if self.robotIsDriving:
                # cancel the timer
                t.cancel()
            else:
                # robot not driving - do nothing
                pass
    
        else:
            # timer not running
            if not self.robotIsDriving:
                # robot is not driving -> start timer
                t.start()
            
            
    # create subscriber
    sub = rospy.Subscriber("/cmd_vel", Twist, cb_driving, queue_size=1)
    
    
    waitAmount = inputs['waitAmount'] # in seconds
    
    def timeout():
        self.logger.info("Timer finished")
        sub.unregister()
        return "success"
        
    t = Timer(waitAmount, timeout)
    t.start()
    
    #while(True):
    #    pass
