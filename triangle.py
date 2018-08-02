import polygon as poly

class triangle(polygon):
    def __init__(self):
        poly.polygon.__init__(self,3)

    def findArea(self):
        a,b,c = self.sides