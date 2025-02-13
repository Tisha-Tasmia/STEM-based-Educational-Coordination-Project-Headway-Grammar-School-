//Simulating a moving robot

import time

class Robot:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move_forward(self):
        self.position += 1
        print(f"{self.name} moved to position {self.position}")

robot = Robot("STEMBot")
for _ in range(5):
    robot.move_forward()
    time.sleep(1)
