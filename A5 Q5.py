T = 65
for i in range(0,5):
    for j in range(0,i+1):
        alphabet = chr(T)
        print(alphabet, end="")
        T += 1
    print()