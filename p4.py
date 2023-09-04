def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)

def animal_crackers(word_list):
    my_list = word_list.lower().split()
    count = 0
    for items in my_list:
        count += 1
    if count == 2:
        if my_list[0][0] == my_list[1][0]:
             print(True)
        else:
             print(False)
    else:
        pass
    
#def other_side_of_seven(num):

def old_macdonald(name):
    name = name[0].upper() + name[1:3] + name[3].upper() + name[5:]
    print(name)

old_macdonald('macdonald')

def master_yoda(text):
    new = text.split()
    rev = new[::-1]
    print(" ".join(rev))

master_yoda('I am home')

def almost_there(n):
    if n in range(90,111) or n in range(200,211):
        return True
    else:
        return False
    
almost_there(212)

def blackjack(a,b,c):
    answer = a + b + c
    if answer <= 21:
        print(answer)
    elif (answer > 21 and 11 in [a,b,c]):
        print(answer - 10)
    else:
        print("BUST")

blackjack(9,9,11)

def summer_69(arr):
    result = 0
    for i in arr:
        if i in range(6,10):
            pass
        else:
            result += i
    print(result)

summer_69([2,1,6,9,11])

def paper_doll(text):
    new = ''
    for i in text:
        new += (i * 3)
    print(new)

paper_doll('Mississippi')