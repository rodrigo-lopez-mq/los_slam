#!/usr/bin/env python
import signal
import sys

import roslib
roslib.load_manifest('nav_kinect')
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud
from geometry_msgs.msg import Twist

import time

class sonares:
	
	def __init__(self):
	  self.pub = rospy.Publisher('/RosAria/cmd_vel', Twist)
	  self.cerca = rospy.Subscriber("/RosAria/sonar",PointCloud, self.callback)
	  self.twist = Twist()
	  self.dist=1.0
	  self.lado=0.6
	  self.lado2=0.6
	  self.lado3=0.5
	  
	  
	def callback(self,data):
		
		
		a2=data.points[1].x##izquierda
		a3=data.points[2].x
		a5=data.points[4].x##Adelante izquierda
		a4=data.points[3].x##Adelante derecha
		a6=data.points[5].x
		a7=data.points[6].x##derecha
			
		ha=a2,a3,a4,a5,a6,a7
		g=0
		#print ha
		
		if ((a4>self.dist) and (a5>self.dist)) and(a6>self.lado) and (a3>self.lado) and (a7>self.lado) and (a2>self.lado):
			self.twist.angular.z = 0.0
			self.twist.linear.x = 0.0
			g=1
		elif (((a4<self.dist) or (a5<self.dist)) and ((a7<self.dist)or(a6<self.dist))):
			self.twist.angular.z = -0.1
			self.twist.linear.x = 0.0
			time.sleep(0.1)
			g=2
		elif (((a4<self.dist) or (a5<self.dist)) and ((a2<self.dist)or(a3<self.dist))):
			self.twist.angular.z = -0.1
			self.twist.linear.x = 0.0
			time.sleep(0.1)
			g=3
		elif ((a7<self.lado)or(a6<self.lado)):
			self.twist.angular.z = 0.1
			self.twist.linear.x = 0.0
			time.sleep(0.1)
			g=4
		elif ((a2<self.lado)or(a3<self.lado)):
			self.twist.angular.z = -0.1
			self.twist.linear.x = 0.0
			time.sleep(0.1)
			g=5
		
		print g	
		##de frente a un lado
		self.pub.publish(self.twist)
			


def listener():

	rospy.init_node('sonares')
	vw = sonares()
	#rospy.init_node('sonares')
	rospy.spin()



if __name__ == '__main__':
	
	listener()
