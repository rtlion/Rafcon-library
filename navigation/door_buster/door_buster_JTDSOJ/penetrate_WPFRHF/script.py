import rospy
from geometry_msgs.msg import Twist


def execute(self, inputs, outputs, gvm):
  self.logger.warn("penetrate!")

  vel = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

  t = Twist()
  t.linear.x = inputs["driveVelX"]

  # fake a publisher with 5Hz
  tt = 0
  while tt < inputs["driveHowLong"]:
    vel.publish(t)
    rospy.sleep(.2)
    tt += .2

  t = Twist()
  vel.publish(t)

  rospy.sleep(1)
  
  return "success"
