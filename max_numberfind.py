

def maximum(a, b):
    if a >= b:
        print("Maximum Number is = ")
        print(a) #we can also use "return a" instead of print(a)

    else:
        print("Maximum Number is = ")
        print(b) #we can also use "return b" instead of print(b)


number_1 = int(input("Enter First Number: "))
number_2 = int(input("Enter Second Number: "))

print(maximum(number_1, number_2))
