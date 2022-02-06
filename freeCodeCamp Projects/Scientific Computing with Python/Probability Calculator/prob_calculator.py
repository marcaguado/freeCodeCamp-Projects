import copy
import random
# Consider using the modules imported above.
class Hat:
    def __init__(self, **kwargs):
        self.temp = kwargs
        self.contents = []
        for i in self.temp:
            for k in range(0, self.temp.get(i)):
                self.contents.append(i)
    def draw(self, numBalls):
        if numBalls >= len(self.contents):
            drawnBalls = self.contents
            self.contents = []
            return drawnBalls
        else:
            drawnBalls = []
            for m in range(0, numBalls):
                selectedChoice = random.choice(self.contents)
                drawnBalls.append(selectedChoice)
                self.contents.remove(selectedChoice)
            return drawnBalls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for k in range(0, num_experiments):
        currentHat = copy.deepcopy(hat)
        drawnBalls = currentHat.draw(num_balls_drawn)
        rasd = False
        for i in expected_balls:
            if expected_balls.get(i) <= drawnBalls.count(i):
                rasd = True
            else:
                rasd = False
                break
        if rasd:
            successes += 1
    probability = float(successes / num_experiments)
    return probability