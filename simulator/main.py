"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	June 8, 2014

"""

#########################################################################


from pandaManager import PandaScene
from pandaManager import SceneGraphManager
from guiManager import Gui
from Queue import Queue
from eventManager import EventManager
from guiManager import GuiThread

def main():
	q = Queue(1)
	pandaScene = PandaScene()
	sceneGraphManager = SceneGraphManager(pandaScene)
	eventManager = EventManager(sceneGraphManager)
	gui = GuiThread(q,eventManager)
	gui.start()
	pandaScene.run()


if __name__=='__main__':
	main()
