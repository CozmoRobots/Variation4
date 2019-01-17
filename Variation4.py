import cozmo;

# Variation 4 group
# mudathirmahgoub
# heardwulf



def move(robot: cozmo.robot.Robot, x, y):
    pass

def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("variation 4").wait_for_completed()
    move(robot, 100, 100);

if __name__ == "__main__":
    cozmo.run_program(cozmo_program)
