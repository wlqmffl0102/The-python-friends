# < for문과 range 함수 >
# 총 5명의 학생이 시험을 봄
# 시험 점수가 60점 이상인 사람 합격 -> 축하메시지
# 나머지 사람 -> 아무 메시지도 전하지 X 프로그램

a = int(input("1번 학생의 시험 점수 : "))
b = int(input("2번 학생의 시험 점수 : "))
c = int(input("3번 학생의 시험 점수 : "))
d = int(input("4번 학생의 시험 점수 : "))
e = int(input("5번 학생의 시험 점수 : "))

score = [a, b, c, d, e]

for s in range(len(score)):
    # len 함수 : 리스트 안의 요소 개수를 돌려주는 함수
    # len(score)=5 가 된다. 5개 이므로
    if score[s] < 60:
        # len(score) 즉 리스트 안의 5개의 수를 s 에 대입해서
        # s가 60보다 값이 작을 때
        continue
        # for 문으로 돌아간다
    print("%d번 학생 축하합니다. 합격입니다. " %(s+1))
    # 값이 60보다 클 때 출력