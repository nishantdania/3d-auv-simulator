#!/usr/bin/python
import roslib
roslib.load_manifest('ros_image')
import sys
import rospy
import cv
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import sys

sys.setrecursionlimit(10000)

class test_vision_node:

    def __init__(self):

        rospy.init_node('test_vision_node')

        """ Give the OpenCV display window a name. """
        self.cv_window_name = "OpenCV Image"

        """ Create the window and make it re-sizeable (second parameter = 0) """
        cv2.namedWindow(self.cv_window_name, 0)
        
        self.ShowImage()

        """ Create the cv_bridge object """
        self.bridge = CvBridge()

        print "ros image node initialised"

        """ Subscribe to the raw camera image topic """
        # self.image_sub = rospy.Subscriber("/bumblebee/bottomCam", Image, self.callback)

    # def callback(self, data):
    #     try:
    #         """ Convert the raw image to OpenCV format """
    #         cv_image = self.bridge.imgmsg_to_cv(data, "bgr8")
    #     except CvBridgeError, e:
    #       print e
  
    #     img1 = numpy.asarray(cv_image[:,:])
    #     ret,img = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
    #     """ Refresh the image on the screen """
    #     cv2.imshow(self.cv_window_name, img)
    #     cv2.waitKey(3000)

    def ShowImage(self):
        try:
            img = cv2.imread("catkin_workspace/src/ros_image/scripts/ImageBuffer.jpg",0)
            cv2.imshow(self.cv_window_name, img)
            cv2.waitKey(150)
        except Exception, e:
            pass
        self.ShowImage()

def main(args):
    vn = test_vision_node()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down vison node."
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)