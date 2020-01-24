# tw 2019-06-09T21:40
import rospy
import actionlib  # Brings in the SimpleActionClient
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped

def execute(self, inputs, outputs, gvm):
  self.logger.debug("rtl_move_base")
  uid = "x08Jun19_004438"

  # sanity checks
  if not type(inputs["PoseStamped"]) is PoseStamped:
    self.logger.error("PoseStamped is wrong type or None")
    return "aborted"

  client = gvm.get_variable(uid, per_reference=True)

  if not client:
    self.logger.warn("no SimpleActionClient found. registering new one ...")

    # Creates the SimpleActionClient, passing the type of the action
    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)

    
    # Waits until the action server has started up and started listening for goals.
    if not client.wait_for_server(
        timeout=rospy.Duration(inputs["timeout_wait_for_server"])
    ):
      self.logger.error("Action server not available!")
      return "preempted"
    else:
        gvm.set_variable(uid, client, per_reference=True)
        self.logger.info("new client %r Connected to move base server" % client)

  else: 
    self.logger.info("using SimpleActionClient %r" % client)

  # Creates a goal to send to the action server.
  goal = MoveBaseGoal(inputs["PoseStamped"])
  self.logger.info("sending goal %r" % goal)

  # Sends the goal to the action server.
  client.send_goal(goal)


  # TODO Add stuck detection
  
  # Waits for the server to finish performing the action.
  finished_within_time = client.wait_for_result(
      timeout=rospy.Duration(inputs["timeout_wait_for_result"])
  )

  # If we don't get there in time, abort the goal
  if not finished_within_time:
    client.cancel_goal()
    rospy.sleep(0.5)
    self.logger.warn("Timed out achieving goal")

  # Prints out the result of executing the action
  result = client.get_state()
  self.logger.info("result is %r" % result)
  return self.get_semantic_data(["move_base result", str(int(result))])
