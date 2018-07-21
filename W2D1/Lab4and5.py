#s.lower
#s
#8,5,4,2,1
#0

count = 0
lego_list = ["red", "blue", "red"]
while count < 50:
    if lego_list[len(lego_list) - 1] == "red":
        lego_list.append("blue")
    if lego_list[len(lego_list) - 1] == "blue":
        lego_list.append("red")
    count = count + 1
print(lego_list)

#the program is trying to open athletes.txt aka name. filename = "C:\\Users\\train916\\Desktop\\DukeTIP 2018\\Week 2\\W2D1\\athletes.txt"
#string
#it prints THE DATA IS: and then the file athletes.txt\
#
