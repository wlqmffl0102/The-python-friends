i=5
j=0

while i>0:
    # i 는 5 ~ 1까지 1씩 감소
    # j 는 0 ~ 5 까지 1씩 증가 = 5 - i
    print("*"*i, end='')
    while j<i:
        print(" "*(5-i), end='')
        j+=1
    print(" ")
    i-=1
