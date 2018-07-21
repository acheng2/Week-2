'''
Created on July 17, 2018

@author; Angela Cheng
'''

def process(name):
    # name is a file, returns a list of strings
    #    from the file
    f = open(name)
    answer = []
    for line in f:
        line = line.strip()
        line = line.split(":")
        answer.append(line)
    return answer

if __name__ == '__main__':
    filename = "C:\\Users\\train916\\Desktop\\DukeTIP 2018\\Week 2\\W2D1\\athletes.txt"
    data = process(filename)
    print("THE DATA IS:")
    #for item in data:
        #print(item)

def AverageHeight():
    answer2 = 0
    count = 0
    answer1 = 0
    while count < 39:
        answer = data[count][4]
        answer1 = int(answer) + answer1
        count = count + 1
        answer2 = answer1 / 39
    print(answer2)

def  heightRange(height1, height2):
    #height1 >= height2
    count = 0
    while count < 39:
        answer = int(data[count][4])
        count = count + 1
        if height1 >= answer >= height2:
            print(answer)

def groupFunction(gender, sport):
    #put answer in quotes
    count = 0
    while count < 39:
        answer = str(data[count][2])
        answer1 = str(data[count][0])
        answer2 = str(data[count][3])
        count = count + 1
        if answer == gender and answer2 == sport:
            print(answer1 + " " + str(data[count][1]))
AverageHeight()
heightRange(78,72)
groupFunction("men", "soccer")
