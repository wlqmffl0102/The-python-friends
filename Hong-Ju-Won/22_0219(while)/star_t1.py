i=2
j=1

while i<7:
    # j가 i 보다 작을 때 5번 돌아서 출력값 나와야 하므로 범위 7보다 작음
    # i와 j 모두 출력값 5번씩 나와야 됨
    while j<i:
        # i와 j 모두 while 문 안이 1씩 증가
        print("*"*j, end='')
        j+=1
    print("")
    i+=1

# i 는 세로 증가 수, 왼쪽 밑으로 1, 2, 3, 4, 5 순으로 증가
# j 는 가로 증가 수, 오른쪽으로 1, 2, 3, 4 ,5 순으로 증가


