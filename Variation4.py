import cozmo;

# Variation 4 group
# mudathirmahgoub
# heardwulf
# benstoffer

def move(robot: cozmo.robot.Robot, x, y):
    # get the current position and rotation
    current_x, current_y, current_z = robot.pose.position. x,   robot.pose.position.y, robot.pose.position.z
    angle_z = robot.pose.rotation.angle_z

    waypoint_1 = cozmo.util.pose_z_angle(x, y, 0, angle_z)
    robot.go_to_pose(waypoint_1, True).wait_for_completed()


def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("variation 4").wait_for_completed()
    move(robot, 300, -300);

if __name__ == "__main__":
    cozmo.run_program(cozmo_program)
