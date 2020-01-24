
from geometry_msgs.msg import PoseStamped
import cPickle as pickle

def execute(self, inputs, outputs, gvm):
    self.logger.debug("converting database human position to PoseStamped")
    human = inputs["human"]
    
    human_x = float(human['x'])
    human_y = float(human['y'])
    
    person_poseStamped = PoseStamped()
    person_poseStamped.header.frame_id = map
    person_poseStamped.pose.position.x = human_x
    person_poseStamped.pose.position.y = human_y
    self.logger.debug("human position is x={0}, y={1}".format(human_x, human_y))
    
    outputs["person_poseStamped_pickled"] = pickle.dumps(person_poseStamped)
    return 0
