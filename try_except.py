try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Please input the appropriate data type")
finally:
    print("I always Run")

x = 5
y = 0
try:
    z = x/y
    print(z)
except ZeroDivisionError:
    print("You should do the division with another value not Zero")
finally:
    print("All Done")

def ask():
    while True:
        try:
            accept = int(input("Input an Integer"))
        except:
            print("Enter an integer")
            continue
        else:
            break
        finally:
            print("All Done")
ask()