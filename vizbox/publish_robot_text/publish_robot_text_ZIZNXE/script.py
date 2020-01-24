import rospy
from std_msgs.msg import String

def execute(self, inputs, outputs, gvm):
    
    text = inputs['robotText']
    pub = rospy.Publisher('/robot_text', String, queue_size=1)
    pub.publish(text)
    
    return 0
