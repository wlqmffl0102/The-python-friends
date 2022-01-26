# 네 정수(1~100) A,B,C,D 입력 받아서
# 두 번째로 큰 정수를 출력하는 프로그램

a = int(input("A : "))
b = int(input("B : "))
c = int(input("C : "))
d = int(input("D : "))
# 네 정수 A,B,C,D 입력 받기

max = a
# 가장 큰 값 임의의 변수 max로 선언

if b>max:
    max=b
    if c<max:
        max=c
    elif d<max:
        max=d
elif c>max:
    max=c
    if b<max:
        max=b
    elif d<max:
        max=d
elif d>max:
    max=d
    if b<max:
        max=b
    elif c<max:
        max=c

print(max)
