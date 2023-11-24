class ToyRobot:
    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None
        self.isOnTable = False

    def place(self, x, y, facing):
        if 0 <= x < 5 and 0 <= y < 5:
            self.x = x
            self.y = y
            self.facing = facing
            self.isOnTable = True

    def move(self):
        if not self.isOnTable:
            return
        if self.facing == "NORTH" and self.y < 4:
            self.y += 1
        elif self.facing == "SOUTH" and self.y > 0:
            self.y -= 1
        elif self.facing == "EAST" and self.x < 4:
            self.x += 1
        elif self.facing == "WEST" and self.x > 0:
            self.x -= 1

    def rotate(self, direction):
        if not self.isOnTable:
            return
        directions = ["NORTH", "EAST", "SOUTH", "WEST"]
        idx = directions.index(self.facing)
        if direction == "LEFT":
            self.facing = directions[(idx - 1) % 4]
        elif direction == "RIGHT":
            self.facing = directions[(idx + 1) % 4]

    def report(self):
        if self.isOnTable:
            return f"{self.x},{self.y},{self.facing}"
        return "Robot is not on the table"

def process_command(robot, command):
    parts = command.split()
    cmd = parts[0]

    if cmd == "PLACE" and len(parts) == 2:
        x, y, facing = parts[1].split(',')
        robot.place(int(x), int(y), facing)
    elif cmd == "MOVE":
        robot.move()
    elif cmd == "LEFT" or cmd == "RIGHT":
        robot.rotate(cmd)
    elif cmd == "REPORT":
        return robot.report()

def main():
    robot = ToyRobot()
    while True:
        command = input("Enter command: ")
        if command == "EXIT":
            break
        output = process_command(robot, command)
        if output:
            print(output)

if __name__ == "__main__":
    main()
