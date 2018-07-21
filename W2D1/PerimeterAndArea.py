class Polygon:

    list_of_points = []

    def __init__ (self, x, y):
        self.list_of_points.append([x,y])

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

ix = int(input("How many points do you want?"))

while ix > 0:
    x = int(input("Pick an X"))
    y =int(input("Pick a Y"))
    i = Polygon(x, y)
    ix = ix - 1

print(i.area())
print(i.perimeter())
