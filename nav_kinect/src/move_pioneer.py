#!/usr/bin/env python
import roslib; roslib.load_manifest('nav_kinect')
import rospy
from std_msgs.msg import String

from geometry_msgs.msg import Twist

global mitad
global mmax
global mmin
global num

def callback(data):
    vel_pub = rospy.Publisher('/RosAria/cmd_vel', Twist)
    #rospy.loginfo("I heard %s",data.data)
    a =int(data.data[1]+data.data[2]+data.data[3])
    b =int(data.data[6]+data.data[7]+data.data[8])
    a1 =int(data.data[11]+data.data[12]+data.data[13])
    b1 =int(data.data[16]+data.data[17]+data.data[18])
   # print a,b,a1,b1
    
    mitad=320
    mmax=600
    mmin=100
    num=0
    
    twist = Twist()

    if b1==999 and a1==999:
   
      if b > mitad and b<mmax:
        listener.nu=1
        num=num+1
  
      elif b < mitad and b>mmin:
        listener.nu=2
        num=num+1
      
      else:
        num=0
        listener.nu=0
    else:
      if b > mitad and b<mmax and b1> mitad and b1<mmax :
        listener.nu=1
  
      elif b < mitad and b>mmin and b1< mitad and b1>mmin:
        listener.nu=2

      elif (b< mitad and b>mmin and b1< mitad and b1>mmin)or(b> mitad and b<mmax and b1<mitad and b1>mmin):
        listener.nu=2
        for i in range(1000):
          num=num
        listener.nu=2  
        num=num+1      

      else:
        num=0
        listener.nu=0

    #if num>6:
    #    twist.linear.x = 0.0
    #    twist.angular.z = -0.1
		
    if listener.nu ==0:
	twist.linear.x = 0.1
	twist.angular.z = 0.0
    if listener.nu ==1:
	twist.linear.x = 0.0
	twist.angular.z = 0.1
    if listener.nu ==2:
        twist.linear.x = 0.0
        twist.angular.z = -0.1

    print listener.nu
        
    vel_pub.publish(twist)
    
    

def listener():
    rospy.init_node('mandar')
    nu=0
    num=0
    rospy.Subscriber("puntos", String,callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
