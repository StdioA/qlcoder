# coding: utf-8

class LifeGame(object):
    def __init__(self, points=None):
        if points is None:
            points = set()
        self.points = points
        self.total = len(points)
        self.next = set()
        self.cur_time = 0

    def check(self, point):
        ts = 0
        x, y = point
        
        if point in self.points:    # 这个点有生命体
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    else:
                        ts += int((x+i, y+j) in self.points)
            if 2 <= ts <= 3:
                self.next.add(point)
        else:                       # 没有生命体
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    else:
                        ts += int((x+i, y+j) in self.points)
            if ts == 3:
                self.next.add(point)

    def next_period(self):
        self.cur_time += 1
        self.next = set()
        self.checked = set()
        for x, y in self.points:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (x+i, y+j) not in self.checked:
                        self.checked.add((x+i, y+j))
                        self.check((x+i, y+j))
        self.points = self.next
        return self.points, self.cur_time

    def __iter__(self):
        while True:
            yield self.next_period()


ps = set([(0, 1), (0, 2), (1, 0), (1, 1), (2, 1)])
game = LifeGame(ps)
max_pop = len(ps)
max_time = 1

for i in range(10000):
    pop, time = game.next_period()
    if len(pop) > max_pop:
        max_pop = len(pop)
        max_time = time

print max_pop, max_time
# 319 821
        
