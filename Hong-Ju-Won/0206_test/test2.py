yun = [90,65,65,70,75,90]

# 합격조건 : 평균 70이상, 과락 60
first_condition = False     # 첫번째 조건(평균 70이상)
Second_condition = False    # 두번째 조건(60이하 과락)

i=0                         # 반복문에 사용될 임시변수
avg = 0                     # 평균
sum=0                       # 점수합계
fails = []                  # 과락

while True:          # 문제1
    if yun[i] <= 60:
        continue  # 문제2
    sum = sum + yun[i]        # 문제3
    i = i+1

avg = sum/len(yun)          # 평균=총합계/리스트의 길이
if avg >= 70 :
    first_condition=True   # 문제 4-1

if len(fails) ==0:
    Second_condition=True   # 문제 4-2

i=0
if Second_condition==True and first_condition==True:                # 첫번째 조건과 두번째 조건 모두 성립하는 경우 
    print("합격입니다")
    print("평균점수 : "+str(avg))
elif Second_condition==True and first_condition==False:            # 두번째 조건만 성립하는 경우 
    print("합격조건에 미달하였습니다.\n평균점수 : "+str(avg))
elif Second_condition==False and first_condition==True:             # 첫번째 조건만 성립하는 경우 
    print("합격조건에 미달하였습니다.")
    while fails:                                                 # 문제 5-1
        print("과락점수 : "+str(fails[i]))                            # 문제 6-1
        i=i+1
elif Second_condition==False and first_condition==False:            # 모든 조건을 만족하지 못하는 경우
    print("합격조건에 미달하였습니다. 평균점수미달 및 과락")
    print("평균점수 : "+str(avg))
    while fails:                                                 # 문제 5-2
        print("과락점수 : "+str(fails[i]))                            # 문제 6-2
        i=i+1