import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self,**kwargs):
        self.contents = list()
        self.draws = list()
        for item in kwargs:
            value = kwargs[item]
            while value > 0:
                self.contents.append(item)
                value -= 1

    def draw(self,quantity):
        if quantity >= len(self.contents):
            return self.contents
        while quantity > 0 and quantity < len(self.contents):
            ball = random.choice(self.contents)
            index = self.contents.index(ball)
            self.draws.append(ball)
            self.contents.pop(index)
            quantity -= 1
        return self.draws
            
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    occurences = 0
    n = num_experiments
    keys = list(expected_balls.keys())
    values = list(expected_balls.values())
    convert = list()
    index = 0
    for item in values:
        while item > 0:
            convert.append(keys[index])
            item -= 1
        index += 1
    
    while num_experiments > 0:
        duplicate = copy.deepcopy(hat)
        kv = copy.deepcopy(convert)
        draws = duplicate.draw(num_balls_drawn)
        num_experiments -= 1
        if len(kv) > len(draws): continue
        counter = 0
        for item in kv:
            if item in draws:
                counter += 1
                draws.remove(item)
        if counter == len(kv):
            occurences += 1
            
    return occurences / n
