i=0
j=6

while i<7:
    print(" "*i, end='')
    while j>i:
        print("*"*(6-i), end='')
        j-=1
    print(" ")
    i+=1

