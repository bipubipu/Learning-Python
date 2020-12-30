import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
            self.contents += [key] * value

    def draw(self, n):
        if n >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            random.shuffle(self.contents)
            drawn_balls = self.contents[:n]
            self.contents = self.contents[n:]
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    for i in range(num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        # Before the next experiment, need to put drawn balls back
        hat.contents += drawn_balls
        for key, value in expected_balls.items():
            if drawn_balls.count(key) < value:
                flag = False
                break
            flag = True
        if flag:
            num_success += 1
    return num_success / num_experiments
