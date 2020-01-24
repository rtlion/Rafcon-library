import rospy
from sensor_msgs.msg import LaserScan
import numpy


def execute(self, inputs, outputs, gvm):

  OpenDist = inputs["minDistAsOpen"]

  pan = 5 * 2
  pan = inputs["scanPanInDeg"]  # +-grad
  door_dist = OpenDist + 0.4  # plus dist base_link to front most

  def callback(data):
    r = numpy.array(data.ranges)
    hinten = numpy.concatenate((r[:0 + pan], r[360 * 2 - pan:]))
    rechts = r[90 * 2 - pan:90 * 2 + pan]
    vorne = r[180 * 2 - pan:180 * 2 + pan]
    links = r[270 * 2 - pan:270 * 2 + pan]

    ma = rechts[numpy.nonzero(rechts)]
    dists = dict(
        hinten=hinten[numpy.nonzero(hinten)].mean(),
        rechts=rechts[numpy.nonzero(rechts)].mean(),
        vorne=vorne[numpy.nonzero(vorne)].mean(),
        links=links[numpy.nonzero(links)].mean(),
    )

    self.logger.debug("distances\n", dists)

    if not vorne > door_dist: return "closed"
    # else

    vel = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    t = Twist()
    t.linear.x = 0.2
    t.linear.y = 0.1
    t.angular.z = 0.1

    vel.publish(t)
    rospy.sleep(2)
    t = Twist()
    vel.publish(t)

    rospy.sleep(.2)

  rospy.init_node("sfddssfd")
  sub = rospy.Subscriber("/cob_scan_unifier/scan_unified", LaserScan, callback, queue_size=1)

  while 1:
    rospy.sleep(.5)
    pass

    sub = rospy.Subscriber("/cob_scan_unifier/scan_unified", LaserScan, callback, queue_size=1)

    self.logger.debug("Hello world")
    return 0
