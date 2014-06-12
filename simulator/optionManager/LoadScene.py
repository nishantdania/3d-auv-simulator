"""

project:        3d-auv-simulator
author:         nishant dania
email:          nishantdania@gmail.com
modified on:    June 8, 2014

"""

#########################################################################


from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

class LoadScene(object):
	def __init__(self, filename, sceneGraphManager):
		self.filename = filename
		self.sgm = sceneGraphManager
		self.loadScene()
		
	def loadScene(self):
		self.tree = ElementTree.ElementTree(file=self.filename)
		root = self.tree.getroot()
		for elem in root:
			for child_elem in elem:
				if child_elem.tag == 'filename':
					filename = child_elem.attrib['value']
					self.sgm.addModelNode(filename)

				if child_elem.tag == 'position':
					x = child_elem.attrib['x']
					self.sgm.setNodeX(x)
					y = child_elem.attrib['y']
					self.sgm.setNodeY(y)
					z = child_elem.attrib['z']
					self.sgm.setNodeZ(z)

				if child_elem.tag == 'orientation':
					h = child_elem.attrib['h']
					self.sgm.setNodeH(h)
					p = child_elem.attrib['p']
					self.sgm.setNodeP(p)
					r = child_elem.attrib['r']
					self.sgm.setNodeR(r)

				if child_elem.tag == 'scale':
					scale = child_elem.attrib['value']
					self.sgm.setNodeScale(scale)