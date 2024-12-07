from yourdfpy import URDF

urdf_path_left = "assets/leap_hand/leap_hand_left.urdf"
urdf_path_right = "assets/leap_hand/leap_hand_right.urdf"
robot_left = URDF.load(urdf_path_left)
robot_right = URDF.load(urdf_path_right)

print("Left Joint Names:", robot_left.joint_names)
print("Right Joint Names:", robot_right.joint_names)
