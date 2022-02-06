# 총 5명의 학생이 시험을 봄
# 시험 점수가 60점이 넘으면 합격, 그렇지 않으면 불합격
# 합격인지 불합격인지 결과 출력 프로그램

a = int(input("1번 학생의 시험 점수 : "))
b = int(input("2번 학생의 시험 점수 : "))
c = int(input("3번 학생의 시험 점수 : "))
d = int(input("4번 학생의 시험 점수 : "))
e = int(input("5번 학생의 시험 점수 : "))

score = [a, b, c, d, e]
n = 0
for s in score:
    n = n+1
    if s >= 60:
        print("%d번 학생은 합격입니다. "%n)
    else:
        print("%d번 학생은 불합격입니다. "%n)