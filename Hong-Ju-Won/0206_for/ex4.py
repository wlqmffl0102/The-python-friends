# < for 문과 continue >
# 총 5명의 학생이 시험을 봄
# 시험 점수가 60점 이상인 사람 합격 -> 축하메시지
# 나머지 사람 -> 아무 메시지도 전하지 X 프로그램

a = int(input("1번 학생의 시험 점수 : "))
b = int(input("2번 학생의 시험 점수 : "))
c = int(input("3번 학생의 시험 점수 : "))
d = int(input("4번 학생의 시험 점수 : "))
e = int(input("5번 학생의 시험 점수 : "))

score = [a, b, c, d, e]
n = 0
for s in score:
    n = n+1
    if s < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " %n)

# 60점 이하인 학생 -> s < 60 이 참이 되어 continue 문 수행
# 즉 출력으로 넘어가지 않고 다시 for문의 처음으로 돌아가게 됨