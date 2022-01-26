# 네 정수(1~100) A,B,C,D 입력 받아서
# 가장 큰 정수를 출력하는 프로그램

a = int(input("A : "))
b = int(input("B : "))
c = int(input("C : "))
d = int(input("D : "))
# 네 정수 A,B,C,D 입력 받기

max = a
# 가장 큰 값 임의의 변수 max로 선언

if b>max:
    max=b
    # 최대값인 a 보다 b가 더 클 때, 최대값 max는 b로 바뀜(최댓값 출력해야 하기 때문)
    if c>max:
        max=c
        # 최댓값 보다 c 가 더 클 때, max는 c 로 바뀜
    if d>max:
        max=d
        # 최댓값 보다 d 가 더 클 때, max는 d 로 바뀜
elif c>max:
    c=max
    # 최대값인 a 보다 c가 더 클 때, 최대값 max는 c로 바뀜
    if b>max:
        max=b
        # 최댓값 보다 b 가 더 클 때, max는 b 로 바뀜
    if d>max:
        max=d
        # 최댓값 보다 d 가 더 클 때, max는 d 로 바뀜
elif d>max:
    d=max
    # 최대값인 a 보다 d가 더 클 때, 최대값 max는 d로 바뀜
    if b>max:
        max=b
        # 최댓값 보다 b 가 더 클 때, max는 b 로 바뀜
    if c>max:
        max=c
        # 최댓값 보다 c 가 더 클 때, max는 c 로 바뀜

print(max)