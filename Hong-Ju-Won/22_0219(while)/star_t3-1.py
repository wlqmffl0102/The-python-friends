i=5
j=0

while i>0:
    print("*"*i, end='')
    while j<i:
        print(" "*(5-i), end='')
        j+=1
    print(" ")
    i-=1
