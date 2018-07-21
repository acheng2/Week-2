a = "computational thinking"
b = "duke university"
c = "python code"

docking = b[0] + a[1] + a[0] + a[18:] #cost = 7
thin_king = a[14:18] + a[13] + a[18:] #cost = 5
computer_code = a[:6] + b[9:11] + c[6:] #cost = 5
ratatatat = b[10] + a[6:8] * 3 #cost = 4
duke_is_cool = b[0:5] + b[7] + b[11] + c[6:9] + a[1] + a[12] #cost = 11
diversity_nation = b[0] + b[7:] + b[4] + c[5] + a[6:11] #cost = 9
money_honey = a[2] + c[4:6] + b[3] + c[1] + c[6] + c[3] + c[4:6] + b[3] + c[1] #cost = 17
print(docking)
print(thin_king)
print(computer_code)
print(ratatatat)
print(duke_is_cool)
print(money_honey)

#B is incorrect
#D
#SKIP

def all_same (value1, value2, value3):
    Tf = False
    value1 = 1
    value2 = 1
    value3 = 1
    if value1 == value2 == value3:
        Tf = True
    print(Tf)

def all_same (value1, value2, value3):
    if value1 == value2 == value3:
        return True
    return False

#for any word that does not have an A in it, that word is added to the previous word that has no A.
#The program prints out all the words that dont have A

def acronym(phrase):
    """
    return a string that is an acronym
    of the string parameter phrase
    """
    phraseList = phrase.split()
    answer = ""
    for word in phraseList:
        x = word[0]
        answer = answer + x
    print(answer)

acronym ()
