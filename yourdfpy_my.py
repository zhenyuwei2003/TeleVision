from yourdfpy import URDF

urdf_path_left = "assets/leap_hand/leap_hand_left.urdf"
urdf_path_right = "assets/leap_hand/leap_hand_right.urdf"
# urdf_path_left = "assets/inspire_hand/inspire_hand_left.urdf"
# urdf_path_right = "assets/inspire_hand/inspire_hand_right.urdf"
robot_left = URDF.load(urdf_path_left)
robot_right = URDF.load(urdf_path_right)

print("Left Joint Names:", [j.name for j in robot_left.robot.joints if j.type != 'fixed'])
print("Right Joint Names:", [j.name for j in robot_right.robot.joints if j.type != 'fixed'])
