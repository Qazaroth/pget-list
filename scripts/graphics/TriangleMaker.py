#prints a triangle of size n

n=int(input("Size:"))
for height in range(n):
    for width in range(height + 1):     #no. of dots in that line
        print("*",  end="")     #prints dots, side by side
    print("")   #changes to a new line
