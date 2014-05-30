"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	May 28, 2014

"""

#########################################################################


from pandaManager import PandaScene
from guiManager import Gui
from Queue import Queue
from eventManager import EventManager
from guiManager import GuiThread

def main():
	q = Queue(1)
	pandaScene = PandaScene()
	em = EventManager(pandaScene)
	gui = GuiThread(q,em)
	gui.start()
	pandaScene.run()


if __name__=='__main__':
	main()
