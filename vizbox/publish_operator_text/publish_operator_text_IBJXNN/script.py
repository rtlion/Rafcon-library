import rospy
from std_msgs.msg import String

def execute(self, inputs, outputs, gvm):
    
    text = inputs['operatorText']
    pub = rospy.Publisher('/operator_text', String, queue_size=1)
    pub.publish(text)
    
    return 0
