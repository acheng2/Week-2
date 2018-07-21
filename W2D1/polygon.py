ix = input("How many points do you want?")

i = Polygon()

while ix > 0:
    x = input("Pick an X")
    y = input("Pick a Y")
    i.addPoint(x, y)
    ix = ix - 1

class Polygon:

    def __init__(self):
        self.list_of_points = []

    def addPoint(self, x, y):
        self.list_of_points.append([x,y])

    def distance(self, x1, x2, y1, y2):
        return ((x1-x2)**2 + (y1-y2)**2)**(0.5)

    def perimeter():
        self.perimeter = 0
        for i in range(len(1, self.list_of_points)):

        return self.perimeter

    def area1(self):

        list_of_points.append(list_of_points[0])
        a = 0
        while a < 2*len(list_of_points):
            answer1 = list_of_points[a][0] * list_of_points[a+1][1] - list_of_points[a+1][0] * list_of_points[a][1]
            a = a + 2
            answer = answer1 + answer
            print(answer)
        #def print(PrintStream out):

print(list_of_points)
