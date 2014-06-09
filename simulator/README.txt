Project Name: 3d-auv-simulator
author: Nishant Dania
Email: nishantdania@gmail.com
Website: nishantdania.github.io

******************************
Pre-requisites:
The following should be installed before running the simulator:
Panda3d 1.8.1
PyQt4
Python

******************************
Steps to run the simulator:
Download the simulator folder. Then in the terminal type the following commands:

# cd simulator
# python main.py

******************************
To add a new model:
1. Click on Browse button (or press 'Ctrl + b' for Windows). Select the .egg model file and click Open. Some sample models have been added to the assets folder. To add the panda model, just type models/panda in the model field.
2. Click on the 'Add Model' button. This would add the model to the scene.

To adjust the size and position of the model, change the respective fields like X:,Y:,Scale, etc. and click on the corresponding buttons. 

Note: The size and scale are adjusted for the latest model that was added. Adding a new model to the scene would take the control to the new model, thus not allowing us to change the previous models.
I am adding the option to choose the model from a list of added models so that the position of any model can be changed at any time.

******************************
To save the scene:
1. Click on the GUI to make it active.
2. Press 'Ctrl + S' or go to file menu and choose the 'Save' option.
3. Enter the name of the file in the dialog box, e.g. 'scene1'
4. Click Ok and the scene is saved in the directory simulator/optionManager/savedFiles as an xml file.

******************************
To load a previously saved scene:
1. Click on the GUI to make it active.
2. Press 'Ctrl + L' or go to file menu and choose the 'Load' option.
3. Search for the file in the dialog box and click the 'Open' button. 

******************************
Additional options:
Click on the Panda window.
Press 'o' key to go to 'oobe' mode. This allows to visualize the scene using the mouse freely. Use left mouse button to pan, right mouse button to zoom and both buttons simultaneously to tilt the view.
Pressing 'o' again takes back to normal view.

Press ESCAPE key to exit the application.

TODO:
Add a save option to save the current state of the simulator which can be loaded later on.  

**Feel free to drop a mail to nishantdania@gmail.com for any doubts and suggestions.**


