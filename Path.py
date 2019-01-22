#Jaykang Heo
#mudathirmahgoub
import cozmo

# Cozmo robot turns right
def turn_right(robot):
    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
    return
# Cozmo robot turns left
def turn_left(robot):
    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()

# Cozmo robot moves the ditance designated
def move_straight(robot: cozmo.robot.Robot, unit):
    robot.drive_straight(cozmo.util.distance_mm(unit), cozmo.util.speed_mmps(150)).wait_for_completed()

"""
Arguments:
wayPoints: list of points 

"""

# Iterated through a list of tuples and arrive at the end of the roads
def move(robot: cozmo.robot.Robot, way_points):
    previous_x , previous_y = way_points[0]
    print(previous_x)
    print(previous_y)
    for i in range(len(way_points)):
        if i == 0 :
            continue
        (x,y) = way_points[i]
        if i % 2 == 1:
            move_straight(robot, x - previous_x )
        else:
            turn_left(robot)
            move_straight(robot, y - previous_y )
            turn_right(robot)
        previous_x , previous_y = (x, y)

# Define distances inside the roads with tuples inside a list
def cozmo_program(robot: cozmo.robot.Robot):
    way_points = [(0, 0), (540, 0),
                  (540, 600),
                  (1580, 550),
                  (1580, 1200)]

    move(robot, way_points)

# Initiate the program
if __name__ == "__main__":
    cozmo.run_program(cozmo_program)
