#네 정수(1~100)A,B,C,D 입력 받아서 두번째로 큰 정수 출력 프로그램

# int(input("정수 A,B,C,D를 각각 입력해 주세요."))

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
d = int(input("D = "))
#정수 입력 받는 구문 작성

if a<b:
    if a>c:
        if a>d:
            print(a)
#입력 받은 a값이 b보다 작은데 c,d 보다 크면 두번째로 큰 값이므로 a를 출력
elif a>b:
    if b>c:
        if b>d:
            print(b)
#입력 받은 b값이 a보다 작은데 c,d 보다 크면 두번째로 큰 값이므로 b를 출력
elif b>c:
    if c>a:
        if c>d:
            print(c)
#입력 받은 c값이 b보다 작은데 a,d 보다 크면 두번째로 큰 값이므로 c를 출력
elif d<c:
    if d>a:
        if d>b:
            print(d)
#입력 받은 d값이 c보다 작은데 a,b 보다 크면 두번째로 큰 값이므로 d를 출력