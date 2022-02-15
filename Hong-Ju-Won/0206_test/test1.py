yun = [90,60,65,70,75,40]

# 합격조건 : 평균 70이상, 과락 60
first_condition = False     # 첫번째 조건(평균 70이상)
Second_condition = False    # 두번째 조건(60이하 과락)

avg = 0                     # 평균
sum = 0                     # 점수합계
fails = []                  # 과락

for s in yun:              # 문제1
    sum = sum + s    # 문제2-1
    if s <=60:           # 문제2-2
        fails.append(s)   # 문제2-3

avg = sum/len(yun)          # 평균=총합계/리스트의 길이

if avg>=70:
    first_condition=True   # 문제 3-1

if len(fails)==0:
    Second_condition=True  # 문제 3-2

i=0
if first_condition==True and Second_condition==True:                # 첫번째 조건과 두번째 조건 모두 성립하는 경우 
    print("합격입니다")
    print("평균점수 : "+ avg )                                    # 문제 4-1
elif first_condition==False and Second_condition==True:            # 두번째 조건만 성립하는 경우 
    print("합격조건에 미달하였습니다.\n평균점수 : "+ avg )               #문제4-2
elif first_condition==True and Second_condition==False:             # 첫번째 조건만 성립하는 경우 
    print("합격조건에 미달하였습니다.")
    for f in fails:                                                      # 문제 5-1
        print("과락점수 : "+str(f))                                   # 문제 6-1
elif first_condition==False and Second_condition==False:            # 모든 조건을 만족하지 못하는 경우
    print("합격조건에 미달하였습니다. 평균점수미달 및 과락")
    print("평균점수 : "+str(avg))
    for f in fails:                                                       # 문제 5-2
        print("과락점수 : "+str(f))                                   # 문제 6-2
