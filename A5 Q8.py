"""
print("Please Enter 10 Numbers\n")
for i in range(1, 11):
    num = int(input("Number %d = " %i))
    Sum = num + Sum

avg = Sum / 10

print("The Sum of 10 Numbers     = ", Sum)
print("The Average of 10 Numbers = ", avg)
"""

list = []
n = 10
print("Enter the 10 numbers")
for i in range(0,n):
    elements = float(input())

    list.append(elements)

print(list)

num = 0
num1 = 0
num2 = 0
num3 = 0
print("The positive numbers are as follows:")
while(num< len(list)):
    if list[num] >= 0:
        print(list[num], end = "\n")
    num += 1
print("The negative numbers are as follows:")
while(num1< len(list)):
    if list[num1] < 0:
        print(list[num1], end = "\n" )
    num1 += 1
print("The Odd numbers are as follows:")
while(num2< len(list)):
    if list[num2] % 2 == 1:
        print(list[num2], end = "\n")
    num2 += 1
print("The even numbers are as follows:")
while(num3< len(list)):
    if list[num3] % 2 == 0:
        print(list[num3], end = "\n")
    num3 += 1
print("The number of time a number has occured")


def countX(list, x):
    count = 0
    for ele in list:
        if (ele == x):
            count = count + 1
    return count
for x in list:
    print('{} has occurred {} times'.format(x,
                                        countX(list, x)))