# tw 2019-06-09T23:08
import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Header
import cPickle as pickle
import os


def execute(self, inputs, outputs, gvm):
  self.logger.debug("rtl_waypoint2pose")
  uid = "x09Jun19_225504"

  repr = lambda o: object.__repr__(o)

  # sanity checks
  wp = inputs["waypoint"]
  if wp is None:
    self.logger.error("no waypoint input")
    return "aborted"

  # get the waypoints
  waypoints = gvm.get_variable(uid, per_reference=True)

  if not waypoints:
    wpp = os.path.expanduser(inputs[".wpp file"])
    self.logger.warn("no waypoints dict. loading file %r ..." % wpp)

    # sanity check
    if not os.path.isfile(wpp):
      self.logger.error("waypoint pickled file %r not such file" % wpp)
      return "preempted"

    with open(wpp, 'rb') as f: waypoints = pickle.load(f)
    self.logger.info("loaded %r pickled waypoints" % len(wpp))

    gvm.set_variable(uid, waypoints, per_reference=True)
    self.logger.info("registered waypoints %r globally" % repr(waypoints))

  else: self.logger.info("using gvm waypoints %r" % repr(waypoints))

  # check if input is in waypoints
  self.logger.info("getting pose of waypoint %r" % wp)
  pose = waypoints.get(str(int(wp)), False)
  if pose is False:
    self.logger.error("waypoint %r is not in waypoints %r" % (wp, repr(waypoints)))
    return "aborted"
  else:
    # waypoint No to pose
    out = PoseStamped(
        header=Header(frame_id=inputs["frame_id"]),
        pose=pose
    )
    self.logger.info("created new PoseStamped %r" % out)
    outputs["PoseStamped"] = out
    return "success"
