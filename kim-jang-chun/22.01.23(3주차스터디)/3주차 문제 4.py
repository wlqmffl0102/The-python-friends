KIM1 = int(input("KIM 국어 성적 입력"))
KIM2 = int(input("KIM 수학 성적 입력"))
KIM3 = int(input("KIM 영어 성적 입력"))

LEE1 = int(input("LEE 국어 성적 입력"))
LEE2 = int(input("LEE 수학 성적 입력"))
LEE3 = int(input("LEE 영어 성적 입력"))

KIM_AVG = (KIM1 + KIM2 + KIM3) / 3
LEE_AVG = (LEE1 + LEE2 + LEE3) / 3

if KIM_AVG > LEE_AVG:
    print("KIM WIN")
elif KIM_AVG < LEE_AVG:
    print("LEE WIN")
elif KIM_AVG == LEE_AVG:
    print("무승부")


#윤지혜 코멘트 : 주석없음
