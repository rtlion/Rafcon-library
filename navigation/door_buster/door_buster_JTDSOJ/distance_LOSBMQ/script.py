import rospy
from sensor_msgs.msg import LaserScan
import numpy


def execute(self, inputs, outputs, gvm):

  OpenDist = inputs["minDistAsOpen"]
  side = inputs["cardinal"]

  pan = inputs["scanPanInDeg"]  # +-grad !not *2 here
  door_dist = OpenDist + 0.4  # plus dist base_link to front most

  def callback(data):
    r = numpy.array(data.ranges)
    # x2 stuff because LaserScan has 721 increments ~= 0.5 deg resolution
    back = numpy.concatenate((r[:0 + pan], r[360 * 2 - pan:]))
    right = r[90 * 2 - pan:90 * 2 + pan]
    front = r[180 * 2 - pan:180 * 2 + pan]
    left = r[270 * 2 - pan:270 * 2 + pan]

    dists = dict(
        back=back[numpy.nonzero(back)].mean(),
        right=right[numpy.nonzero(right)].mean(),
        front=front[numpy.nonzero(front)].mean(),
        left=left[numpy.nonzero(left)].mean(),
    )

    rospy.logdebug_throttle(1, "distances\n%r" % dists)

    if dists[side] > door_dist:
      self.logger.info("open detected! dist to %r: %.3r m" % (side, dists[side]))
      self.cob.unregister()
      self.res = "open"
      return
    else:
      #self.res = "closed"
      self.logger.debug("dist to %r: %.3r m" % (side, dists[side]))
      pass

  self.cob = rospy.topics.Subscriber(
      "/cob_scan_unifier/scan_unified",
      LaserScan,
      callback,
      queue_size=1
  )
  rospy.wait_for_message
  self.logger.info("starting dist check loop")
  self.res = None

  while self.res is None: rospy.sleep(1)

  return self.res
