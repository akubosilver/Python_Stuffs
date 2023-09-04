def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    if len(code) == 1:
        print(True)
    else:
        print(False)

spy_game([1,2,4,0,0,7,5])

def count_primes(num):
    arr = []
    
    for i in range(2,num+1):
        for j in range(2, i):
            if (i%j) == 0:
                break
        else:
            arr.append(i)
    print(arr)
    print(len(arr))

count_primes(100)

mylist = [1,2,3,4,5]
new_list = list(map(lambda num:num**2, mylist))
print(new_list)
even = list(filter(lambda num:num%2==0, mylist))
print(even)

new_list = [1,2,3,4,5,5,6,6,7]
#using for loop for sum()
def my_sum(my_list):
    result = 0
    for i in my_list:
        result += i
    print(result)
#using list comprehension for sum() 
def an_sum(my_list):
    total = 0
    [total := total + x for x in my_list]
    print(total)

my_sum(new_list)
print(sum(new_list)) #original sum()
an_sum(new_list)