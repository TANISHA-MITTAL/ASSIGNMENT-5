def reverseString(a):
    str = ""
    for i in a:
        str = i + str
    return str

a = "this string will be reversed"

print(a)
print(reverseString(a))