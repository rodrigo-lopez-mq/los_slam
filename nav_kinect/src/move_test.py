#!/usr/bin/env python
import roslib; roslib.load_manifest('nav_kinect')
import rospy

from geometry_msgs.msg import Twist

def mover():
    pub = rospy.Publisher('/RosAria/cmd_vel', Twist)
    rospy.init_node('robot_mover')

    twist = Twist()
    twist.linear.x = 0.1; 

    pub.publish(twist)
    rospy.sleep(1)



    twist.angular.z = -0.5
    pub.publish(twist)
    rospy.sleep(1);
    
    #rospy.spin()
    twist.linear.x = 0; 
    twist.angular.z = 0
    pub.publish(twist)
    

if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException: pass
