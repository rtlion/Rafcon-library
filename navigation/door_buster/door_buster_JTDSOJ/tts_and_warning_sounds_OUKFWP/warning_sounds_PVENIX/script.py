import rospy
from std_msgs.msg import String


def execute(self, inputs, outputs, gvm):
  self.logger.debug("warn the guy in the door")
  sound = rospy.Publisher("/sampler/play", String, queue_size=1)
  sound.publish(String("alert"))
  rospy.sleep(10) # tts wait
  sound.publish(String("impossible"))
  rospy.sleep(8)
  sound.publish(String("inception"))
  #rospy.sleep(5)
  # sound.publish(String("yeah"))
  # sound.publish(String("ready"))
  # sound.publish(String("halleluja"))
  return 0