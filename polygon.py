class Polygon:

    # def __init__(self):
    list_of_points = []

    def __init__ (self, x, y):
        self.list_of_points.append([x,y])

    #def distance(self, x1, x2, y1, y2):
        #return ((x1-x2)**2 + (y1-y2)**2)**(0.5)

    #def perimeter(self):
        #self.perimeter = 0
        #for i in range(len(self.list_of_points)):

        #return self.perimeter

    def perimeter(self):
        list_of_points = self.list_of_points
        a = 0
        answer = 0
        while a < len(list_of_points)-1:
            answer1 = abs(((list_of_points[a][0]-list_of_points[a+1][0])**2 + (list_of_points[a][1]-list_of_points[a+1][1])**2)**(0.5))
            a += 1
            answer = answer1 + answer
        return answer

    def area(self):
        list_of_points = self.list_of_points
        list_of_points.append(list_of_points[0])
        a = 0
        answer = 0
        while a < len(list_of_points)-1:
            answer1 = list_of_points[a][0] * list_of_points[a+1][1] - list_of_points[a+1][0] * list_of_points[a][1]
            a += 1
            answer = answer1 + answer
        return abs(answer) / 2
        #def print(PrintStream out):

#empty list, add points x san dy to list, calculate area and perimeter
iiii = Polygon(2,6)
iii = Polygon(4,6)
ii = Polygon(4,4)
i = Polygon(2,4)
print(i.area())
print(i.perimeter())
