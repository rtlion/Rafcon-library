import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped,Twist

def execute(self, inputs, outputs, gvm):
    p = PoseWithCovarianceStamped()
    p.header.frame_id = inputs["pose"].header.frame_id
    p.pose.pose = inputs["pose"].pose
    p.pose.covariance = [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.07]
    self.logger.info("send PoseWithCovarianceStamped\n%r" % p)

    message_pub = rospy.Publisher("/initialpose", PoseWithCovarianceStamped, queue_size=1)
    message_pub.publish(p)


    vel = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    t=Twist()
    t.linear.x= 0.2
    t.linear.y= 0.1
    t.angular.z= 0.1

    vel.publish(t)
    rospy.sleep(2)
    t=Twist()
    vel.publish(t)

    o = PoseStamped()
    o.header.frame_id=inputs["frame_robot"]
    o.pose.position.x=inputs["distance"]
    o.pose.position.y=inputs["distance"]
    o.pose.position.z=0

    o.pose.orientation.x=0
    o.pose.orientation.y=0
    o.pose.orientation.z= 0.259
    o.pose.orientation.w= 0.966

    self.logger.info("setting some movement to localize\n%r" % o)
    outputs["relative pose"] = o

    return "success"