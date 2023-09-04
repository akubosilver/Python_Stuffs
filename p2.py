st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0]=='s':
        print(word)

mylist = [x for x in range(11) if x%2==0]
print(mylist)

my_list = [x for x in range(1,50) if x%3==0]
print(my_list)

for word in st:
    if len(word)%2==0:
        print("even!")

for i in range(1,100):
    if (i%3==0 and i%5==0):
        print("FizzBuzz")
    elif (i%3==0):
        print("Fizz")
    elif (i%5==0):
        print("Buzz")
    else:
        print(i)

stt = 'Create a list of the first letters of every word in this string'
an_list = [word[0] for word in stt.split()]
print(an_list)