# 사용자로 부터 시험 점수 입력 받아
# 90~100 : A, 80~89 : B, 70~79 : C, 60~69 : D, 나머지 : F
# 단 0 이하, 100 초과 입력하면 "Error"

s = int(input("시험 점수를 입력하시오 : "))
# 사용자로 부터 시험 점수 입력 받기

if s<=0:
    print("Error")
    # Error 조건 중 하나인 0 이하일 때 가정을 맨 밑으로 보내면 실행 안되서, 맨 위로 넣어줌
elif s>100:
    print("Error")
    # Error 조건 중 100 초과일 경우 설정
elif s>=90 and s<=100:
    print("A")
    # A : 90~100 경우 설정
elif s>=80 and s<90:
    print("B")
    # B : 80~89 경우 설정
elif s>=70 and s<80:
    print("C")
    # C : 70~79 경우 설정
elif s>=60 and s<70:
    print("D")
    # D : 60~69 경우 설정
elif s<60:
    print("F")
    # 60 미만일 경우 설정
