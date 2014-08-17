# """

# project:		3d-auv-simulator
# author:			nishant dania
# email: 			nishantdania@gmail.com
# modified on:	August 16, 2014

# """

# #########################################################################

xterm -hold -e roscore &
xterm -e rosrun ros_image image_listener.py &
# bash -c "rosrun ros_image image_listener.py" &
exit 0