# coding: utf-8

class People(object):
    """并查集"""
    def __init__(self, name):
        self.name = name
        self.rel = None

    def update(self, another):
        sr = self.root()
        ar = another.root()

        if sr is ar:
            return

        if sr.name > ar.name:
            sr.rel = ar
        else:
            ar.rel = sr
        
    def check(self, another):
        return (self.root() is another.root())

    def root(self):
        p = self
        while p.rel is not None:
            p = p.rel

        return p

    def __repr__(self):
        return "<People %d>"%self.name


total = 100000
peoples = [None]+[People(i) for i in range(1, total+1)]
datas = []

with file("hotspot_2.txt") as f:
    for line in f:
        d1, d2 = tuple([peoples[int(x)] for x in line.split()])
        d1.update(d2)


a = set()
for p in peoples[1:]:
    a.add(p.root().name)
    
print len(a)
