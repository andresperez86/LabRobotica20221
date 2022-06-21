#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
import numpy as np

if __name__ == "__main__":
	rospy.init_node("sendJointsNode")
	pub = rospy.Publisher("joint_states", JointState, queue_size=1000)
	# Joint names
	jnames = ("right_j0", "head_pan", "right_j1", "right_j2", "right_j3", "right_j4", "right_j5", "right_j6")

	# Desired Joint Configuration (in radians)
	.. Your code here ...

	# Object (message) whose type is JointState
	jstate = JointState()
	# Set values to the message
	jstate.header.stamp = rospy.Time.now()
	jstate.name = jnames
	jstate.position = jvaluesInicial
	# Loop rate (in Hz)
	rate = rospy.Rate(100)
	# Continuous execution loop

	while (not rospy.is_shutdown()): #and i<=300:
		# Current time (needed as an indicator for ROS)
		jstate.header.stamp = rospy.Time.now()
		jvalues =  list(np.array(jvaluesInicial)+np.array(paso)*i)
		jstate.position = jvalues
		# Publish message
		pub.publish(jstate)
		# Wait for the next iteration
		rate.sleep()
	

