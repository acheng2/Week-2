#import time
#tic = time.time()
def Factorial ():
    n = input("what do you want to factorial?")
    n = int(n)
    answer1 = 1
    while n > 0:
        answer1 = answer1 * (n)
        n = n - 1
    print(answer1)
Factorial()
#toc = time.time()
#print((toc - tic)/60000)
