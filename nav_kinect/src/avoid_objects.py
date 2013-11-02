#!/usr/bin/env python
import roslib
roslib.load_manifest('nav_kinect')
import sys
import rospy
import cv
import time
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

from geometry_msgs.msg import Twist

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("puntos",String)
    #self.vel_pub = rospy.Publisher('/RosAria/cmd_vel', Twist)
    cv.NamedWindow("Image window", 1)
    self.bridge = CvBridge()
    self.depth_sub = rospy.Subscriber("camera/depth/image",Image,self.callbackDepth)
    #self.twist = Twist()
    
    
    

  def callbackDepth(self,data):
    
    try:
      cv_depth = self.bridge.imgmsg_to_cv(data, "32FC3")
      w,h=cv.GetSize(cv_depth)
      print w,h
    except CvBridgeError, e:
      print e
    a=999;b=999;a1=999;a2=999;a3=999;b1=999;b2=0;b3=0
    low=1.0
    c=0;
    for i in range(200,381,5):
      for w in range(170,491,5):
        if (cv_depth[i,w][0]<low)and c==0:
			 
				a=i;b=w;c+=1
        if (cv_depth[i,w][0]<low)and c==1 and ((b+200)<w or (b-200)>w):  #and ((a+100)<i or (a-100)>i):
			 
				a1=i;b1=w;c+=1
   #     if (cv_depth[i,w][0]<low)and c==2 and ((b+200)<w or (b-200)>w)  and ((a+100)<i or (a-100)>i) and ((b1+200)<w or (b1-200)>w)  and ((a1+100)<i or (a1-100)>i):
			 
	#			a2=i;b2=w;c+=1
        #if (cv_depth[i,w][0]<low)and c==3 and(w+30)>b and (i+30)>a and (w+30)>b and (i+30)>a and(w+30)>b2 and (i+30)>a2:
        #  a3=i;b3=w;c+=1
   # for i in range(1,480,10):
   #   for w in range(1,632,10):
   #     if (cv_depth[i,w][0]<low)and c==1 and ((b+30)<w or (b-30)>w)  and ((a+30)<i or (a-30)>i):
   #       a1=i;b1=w;c+=1

          #low=cv_depth[i,w][0]
    
    if b!=999 and a!=999:
      cv.Circle(cv_depth, (b,a), 10, cv.CV_RGB(0, 255, 0),10)
    if b1!=999 and a1!=999:
      cv.Circle(cv_depth, (b1,a1), 10, cv.CV_RGB(15, 0, 100),10)
   # if b2!=0 and a2!=0:
   #   cv.Circle(cv_depth, (b2,a2), 10, cv.CV_RGB(0, 55, 255),10)
   # if b3!=0 and a3!=0:
   #   cv.Circle(cv_depth, (b3,a3), 10, cv.CV_RGB(0, 255, 0),10)
    

    cv.ShowImage("Image window", cv_depth)
    if b1<100:
      b1=100
    if a1<100:
      a1=100
    if b<100:
      b=100
    if a<100:
      a=100
    #cv.WaitKey(3)
    punto=a,b,a1,b1
    self.image_pub.publish(str(punto))

def main(args):
  
  
  ic = image_converter()
  rospy.init_node('imagen')
  
  rospy.spin()
  

if __name__ == '__main__':
    main(sys.argv)


