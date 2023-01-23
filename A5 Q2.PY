lower_range = int(input("Enter the lower range"))
upper_range = int(input("Enter the upper range"))
number = int(input("enter the divisor"))
for i in range(lower_range,upper_range+1):
    if i%number == 0:
        print(i)
