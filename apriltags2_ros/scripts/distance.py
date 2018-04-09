#!/usr/bin/env python
import roslib
import rospy
import tf
from std_msgs.msg import Float32

if __name__ == "__main__":
	rospy.init_node("agv_apriltags_distance")
	listener = tf.TransformListener()

	distance_pub = rospy.Publisher('distance', Float32, queue_size=1)
	rate = rospy.Rate(10.0)

	while not rospy.is_shutdown():
		try:
			trans, rot = listener.lookupTransform("/camera_link", "agv_dis", rospy.Time(0))
			
		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			continue
		dis = float(trans[2])
		distance_pub.publish(dis)

		rate.sleep()
