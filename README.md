# 3d-auv-simulator
Automatically exported from code.google.com/p/3d-auv-simulator

project name: 3d-auv-simulator
author: Nishant Dania
email: nishantdania@gmail.com
website: nishantdania.github.io

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
# source catkin_workspace/devel/setup.bash
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
Selection Mode:
To select an object in the scene for modifications, follow the steps below:
1. Click on the Scene window to make it active and press 1 on the keyboard. This takes you to the selection mode.
Note: The default camera controls won't work in this mode.
2. Now click on any object to select it. A green box appears around it suggesting that it has been selected.
3. Press 1 on the keyboard again to go to the normal mode.

******************************
To position an object(say obj1) relative to another object(say obj2):
1. Select obj1 first by going to the selection mode.
2. Now select obj2. (Now, obj2 is currently selected and obj1 is the previously selected object)
3. Enter the required values of X,Y,Z in SetX(rel.),SetY(rel.),SetZ(rel.) respectively. 

******************************
Keyboard Operations:
Esc - Exits the application
R - resets the scene window to a blanck scene without any objects
O - Oobe mode toggle
1 - Selection mode toggle

M - World Map toggle
The following keyboard operations can be used only when the world map is active:
Z - Zoom out control for world map
X - Zoom in control
C - Default zoom
W,A,S,D - To move the world map camera

******************************
Additional Info:
Press 'o' key to go to 'oobe' mode. This allows to visualize the scene using the mouse freely. Use left mouse button to pan, right mouse button to zoom and both buttons simultaneously to tilt the view.
Pressing 'o' again takes back to normal view.

**A Water pool has been added to simulate underwater scene. Controls to animate the surface would be added in the next commit.

**Feel free to drop a mail to nishantdania@gmail.com for any doubts and suggestions.**
