"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	August 16, 2014

"""

#########################################################################

from subprocess import *
from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import *
import os
import cv
import cv2
import numpy as np

class RosManager(object):
	def __init__(self):
		self.init_roscore_path = os.path.dirname(os.path.realpath(__file__)) + "/init_roscore.sh"
		call(self.init_roscore_path, shell=True)
		# taskMgr.add(self.ImagePublisher, 'ImagePublisher')

        cv2.namedWindow("1", 0)
        

		
	def ImagePublisher(self):

		tex = Texture()
		width = 1
		height = 1
		imageBuffer = base.win.makeTextureBuffer('Image Buffer',width,height,tex,True)
		cam=Camera('BaseCam')
		cam.setLens(base.camLens.makeCopy())
		cam.getLens().setAspectRatio(width/height)
		pCam=NodePath(cam)
		blank_image = np.zeros((height,width,3), np.uint8)

		mycamera = base.makeCamera(imageBuffer,useCamera=pCam)
		myscene = base.render
		mycamera.node().setScene(myscene)
		base.graphicsEngine.renderFrame()
		tex = imageBuffer.getTexture()
		imageBuffer.setActive(False)
		# tex.write("ImageBuffer"+".jpg")
		# img  = cv2.imread(tex.getRamImage(),0)
		# cv2.imshow("1",img)
		# cv2.waitKey(2)
		# print blank_image

		# count =0 
		# for x in xrange(0,height):
		# 	for y in xrange(0,width):
		# 		for z in xrange(0,3):
		# 			blank_image[x][y][z] = (tex.getRamImage())[count]
		# 			count+=1

		# for item in tex.getRamImage():
		# 	print item
		# print (tex.getRamImage())[3]

		base.graphicsEngine.removeWindow(imageBuffer)
		return blank_image
		# return task.cont