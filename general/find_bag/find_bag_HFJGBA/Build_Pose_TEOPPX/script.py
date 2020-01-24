import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose
from std_msgs.msg import Header

def execute(self, inputs, outputs, gvm):
  
  point_direction = inputs['point direction']
  bag_position = inputs['bag_position']
  frameCam = inputs['cam frame']
  target_frame = inputs['robot frame']
  bufferZone = inputs['teb buffer zone']

  listener = gvm.get_variable("tf_listener", per_reference=True)  # this from `init_ros_node`
  
  thatBag = bag_position
  
  # bag pose frame
  pBag = PoseStamped(pose=thatBag)
  pBag.header.frame_id = frameCam

  # bag pose in base_link
  pose_msg = listener.transformPose(target_frame, pBag)
  pose_msg.pose.position.x -= bufferZone
  pose_msg.pose.position.y -= bufferZone
  pose_msg.pose.position.z = 0
  
  # ggf. noch verbessern - (laut thomas)
  pose_msg.pose.orientation.x = 0
  pose_msg.pose.orientation.y = 0
  pose_msg.pose.orientation.z = 0
  pose_msg.pose.orientation.w = 1
  
  
  """
  pose_msg = PoseStamped(
      header=Header(frame_id=target_frame),
      pose= Pose(
          position=g.Point(x=.5, y=.5, z=0),
          orientation=g.Quaternion(x=0, y=0, z=0, w=1)
          ))
          
  pose_
  """
  
  outputs["bag_pose"] = pose_msg
  
  self.logger.info("Bag Pose: {}".format(pose_msg))
  
  return "success"
