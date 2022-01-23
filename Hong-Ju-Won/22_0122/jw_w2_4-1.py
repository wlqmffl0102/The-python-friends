# K 와 L 이 각각 국,영,수 시험성적을 입력 받아 평균을 구하고
# 어느 쪽이 시험을 더 잘 봤는지 출력(cal_avg)

k_kor = int(input("K의 국어 점수 : "))
k_eng = int(input("K의 영어 점수 : "))
k_math = int(input("K의 수학 점수 : "))
# K의 국영수 점수 입력 받기

k_avg = k_kor+k_eng+k_math /3
# K의 국영수 성적 평균 구하기

l_kor = int(input("L의 국어 점수 : "))
l_eng = int(input("L의 영어 점수 : "))
l_math = int(input("L의 수학 점수 : "))
# L의 국영수 점수 입력 받기 

l_avg = l_kor+l_eng+l_math /3
# L의 국영수 성적 평균 구하기

if k_avg>l_avg:
    print("K의 시험 성적이 더 우수합니다.")
elif l_avg<k_avg:
    print("L의 시험 성적이 더 우수합니다.")
# 평균이 더 높은 사람의 시험 성적이 더 우수하다고 출력하기

