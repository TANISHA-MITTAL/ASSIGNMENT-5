import math
side_1 = float(input("Enter the length of side a"))
side_2 = float(input("Enter the length of side b"))
side_3 = float(input("Enter the length of side c"))

def valid_triangle():
    if side_1+side_2>=side_3 and side_1+side_3>=side_2 and side_3+side_2>=side_1:
        return True
    else:
        return False

if valid_triangle():
    print("Triangle is Valid")
else:
    print("Triangle is invalid")

s = (side_1+side_2+side_3)/2
area = math.sqrt(s*(s-side_1)*(s-side_2)*(s-side_3))

print("the area of the triangle is", area)