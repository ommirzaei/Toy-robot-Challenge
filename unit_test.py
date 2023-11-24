import unittest
from toy_robot import ToyRobot

class TestToyRobot(unittest.TestCase):

    def test_initial_placement_and_report(self):
        robot = ToyRobot()
        robot.place(0, 0, "NORTH")
        self.assertEqual(robot.report(), "0,0,NORTH")

    def test_movement(self):
        robot = ToyRobot()
        robot.place(1, 1, "NORTH")
        robot.move()
        self.assertEqual(robot.report(), "1,2,NORTH")

    def test_boundary_condition(self):
        robot = ToyRobot()
        robot.place(0, 0, "SOUTH")
        robot.move()  # Should be ignored as it would make the robot fall
        self.assertEqual(robot.report(), "0,0,SOUTH")

    def test_invalid_placement(self):
        robot = ToyRobot()
        robot.place(-1, -1, "NORTH")  # Invalid place
        self.assertEqual(robot.report(), "Robot is not on the table")

    def test_edge_movement(self):
        robot = ToyRobot()
        robot.place(4, 4, "NORTH")
        robot.move()  # Should be ignored
        self.assertEqual(robot.report(), "4,4,NORTH")

    def test_rotation(self):
        robot = ToyRobot()
        robot.place(0, 0, "NORTH")
        robot.rotate("LEFT")
        self.assertEqual(robot.report(), "0,0,WEST")

    def test_ignore_before_valid_place(self):
        robot = ToyRobot()
        robot.move()
        robot.rotate("LEFT")
        robot.place(1, 1, "NORTH")
        self.assertEqual(robot.report(), "1,1,NORTH")

    def test_sequential_commands(self):
        robot = ToyRobot()
        robot.place(1, 2, "EAST")
        robot.move()
        robot.move()
        robot.rotate("LEFT")
        robot.move()
        self.assertEqual(robot.report(), "3,3,NORTH")

if __name__ == '__main__':
    unittest.main()
