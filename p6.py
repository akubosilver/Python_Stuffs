#HOME WORK
def vol(rad):
    pi = 3.14
    volume = 4/3 * pi * rad ** 3
    print(volume)

vol(2)

def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f"{num} is in the range between {low} and {high}")
    else:
        print(f"{num} is not in the range between {low} and {high}")

ran_check(7,2,7)

def up_low(s):
    low = 0
    up = 0
    for letter in s:
        if letter.isupper():
            up += 1
        elif letter.islower():
            low += 1
        else:
            pass
    print(f"Number of lowercases is {low} and uppercases is {up}")

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

def unique_list(lst):
    new = list(set(lst))
    print(new)

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

def multiply(numbers):
    product = 1
    [product := product * x for x in numbers]
    print(product)

multiply([1,2,3,-4])

def pallindrome(s):
    s = s.replace(' ', '')
    if s == s[::-1]:
        print(True)
    else:
        print(False)

pallindrome('helleh')

import string
def ispangram(s):
    count = 0
    s = s.lower()
    word = string.ascii_lowercase
    for letter in word:
        if letter in s:
            count += 1
        else:
            break
    if count == 26:
        print(True)
    else:
        print(False)

ispangram("The quick brown fox jumps over the lazy dog")