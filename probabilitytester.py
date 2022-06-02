import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self, remove):
        if remove < len(self.contents):
            self.removed_balls = []
            for i in range(remove):
                ran_num = random.randint(0, (len(self.contents) - 1))
                self.removed_balls.append(self.contents[ran_num])
                del self.contents[ran_num]
            return self.removed_balls
        else:
            return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_received = hat_copy.draw(num_balls_drawn)
        for color in colors_received:
            if color in expected_copy:
                expected_copy[color] -= 1
            
        if all (x <= 0  for x in expected_copy.values()):
            count += 1
    
    return count / num_experiments


