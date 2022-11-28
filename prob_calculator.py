import copy
import random
# Consider using the modules imported above.

# take a variable number of arguments that specify the number of balls of each color that are in the hat
class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    # take an argument indicating the number of balls to draw from the hat
    def draw(self, num):
        if num >= len(self.contents):
            return self.contents

        balls = []
        for i in range(num):
            ball = random.choice(self.contents)
            balls.append(ball)
            self.contents.remove(ball)
        return balls

# return a prbability of getting a specific number of balls of a specific color
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        flag = True
        for key, value in expected_balls.items():
            if balls.count(key) < value:
                flag = False
                break
        if flag:
            success += 1
    return success / num_experiments