#!/usr/bin/env python  
import roslib
roslib.load_manifest('egoat_2dnav')
import rospy

import tf
import geometry_msgs 

def handle_egoat_pose(msg, egoat1):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     egoat1,
                     "world")

if __name__ == '__main__':
    rospy.init_node('egoat_tf_broadcaster')
    egoat1 = rospy.get_param('~egoat')
    rospy.Subscriber('/%s/pose' % egoat1,
                     geometry_msgs.Pose, #!should be the name of the dep that has pose msgs, from up there
                     handle_egoat_pose,
                     egoat1)
    rospy.spin()
