"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	June 8, 2014

"""

#########################################################################

from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import os

class SaveScene(object):
	def __init__(self, filename, modelList):
		self.filename = os.path.dirname(os.path.realpath(__file__)) + '/savedFiles/' + filename +'.xml'
		self.modelList = modelList

	def saveModels(self):
		models = Element('models')

		for modelItem in self.modelList:
			model = SubElement(models, 'model')
			filename = SubElement(model,'filename',value=modelItem.getFilename())
			position = SubElement(model,'position',
				x=str(modelItem.getX()),
				y=str(modelItem.getY()),
				z=str(modelItem.getZ()))
			orientation = SubElement(model,'orientation',
				h=str(modelItem.getH()),
				p=str(modelItem.getP()),
				r=str(modelItem.getR()))
			scale = SubElement(model,'scale',value=str(modelItem.getScale()))
		
		tree = ElementTree.ElementTree(models)
		tree.write(self.filename,
			xml_declaration=True,encoding='utf-8',
			method="xml")
		print "File Saved"
	