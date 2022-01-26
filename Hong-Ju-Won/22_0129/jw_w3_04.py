# K와 L 이 국,영,수 시험 성적으로 내기
# K와 L 의 시험 성적 입력 받아 평균 구하고 비교 하기

k_kor = int(input("K의 국어 점수을 입력해 주세요. : "))
k_eng = int(input("K의 영어 점수을 입력해 주세요. : "))
k_math = int(input("K의 수학 점수를 입력해 주세요. : "))
# K의 국,영,수 점수 입력 받기

l_kor = int(input("L의 국어 점수을 입력해 주세요. : "))
l_eng = int(input("L의 영어 점수을 입력해 주세요. : "))
l_math = int(input("L의 수학 점수를 입력해 주세요. : "))
# L의 국,영,수 점수 입력 받기

k_avg = (k_kor + k_eng + k_math)/3
l_avg = (l_kor + l_eng + l_math)/3
# K와 L의 점수 평균 각각 구하기

if k_avg>l_avg:
    print("K의 성적이 더 좋습니다.")
    # K의 평균이 L의 평균보다 더 높을 경우 K의 성적이 더 좋다고 출력
elif k_avg<l_avg:
    print("L의 성적이 더 좋습니다.")
    # L의 평균이 K의 평균보다 더 높을 경우 K의 성적이 더 좋다고 출력
elif k_avg==l_avg:
    print("K와 L의 성적이 동점입니다.")
    # K의 평균과 L의 평균이 같을 경우 동점 출력

