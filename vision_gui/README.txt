Was originally a ROS node to be run with command: rosrun gui vision_gui_node

Has front and bottom camera input image and filter image

image topics:
/front_camera/camera/image_raw
/bot_camera/camera/image_raw

Flare_Vision: Vision filter chain for the flare (CAD file in the respective folder)
Controller.msg: Required ROS message service for sendMovement function found in flare_vision.py for locomotion of robot
