#문제1
#사용자로 부터 시험점수를 입력받아 90~100점은 A, 80~89점은 B,
#70~79점은 C, 60~69점은 D, 나머지 점수는 F를 출력하시오.
#이때 0 이하, 100이상의 숫자는 "Error" 출력하기

score = int(input("시험 점수를 입력해 주세요. : "))

if score<=0:
    print("Error")
elif score>100:
    print("Error")
#밑에 else 구문으로 따로 빼보았으나 실행 시 F로 뜨는 관계로 맨 앞으로 빼서
#0 이하나 100 초과의 숫자는 "Error" 가 출력되도록 구문 작성
elif score>=90:
    print("A")
#90점 이상은 A가 나오도록 작성
elif score>=80:
    print("B")
#80점 이상은 B가 나오도록 작성
elif score>=70:
    print("C")
#70점 이상은 C가 나오도록 작성
elif score>=60:
    print("D")
#60점 이상은 D가 나오도록 작성
elif score<60:
    print("F")
#60점 미만은 F가 나오도록 작성


