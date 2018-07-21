def Find(list1, search):
    count = 0
    while count < len(list1):
        if list1[count] == search:
            print(count + 1)
            return
        count = count + 1
    if count == len(list1):
        print(-1)
        count = count + 1
Find(list(range(1, 100000)), 10000)
