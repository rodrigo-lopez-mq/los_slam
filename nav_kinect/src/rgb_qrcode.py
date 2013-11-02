#!/usr/bin/env python
import roslib
roslib.load_manifest('nav_kinect')
import sys
import rospy
import cv
import Image
import StringIO
import zbar
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


#import Image

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("image_topic_2",Image)

    cv.NamedWindow("Image window", 1)
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/rgb/image_color",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv(data, "rgb8")
    except CvBridgeError, e:
      print e

    (cols,rows) = cv.GetSize(cv_image)
   

    gris = cv.CreateImage(cv.GetSize(cv_image),cv.IPL_DEPTH_8U,1);
    cv.CvtColor(cv_image, gris, cv.CV_RGB2GRAY);
    scanner = zbar.ImageScanner()
    scanner.parse_config('enable')

    raw=gris.tostring()
    
    image = zbar.Image(cols,rows, 'Y800', raw)

    scanner.scan(image)
    
    for symbol in image:
      print symbol.data

    cv.ShowImage("Image window", cv_image)
    
    cv.WaitKey(3)


def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  
  rospy.spin()
 

if __name__ == '__main__':
    main(sys.argv)
