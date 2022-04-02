# 함수 round
# 매개변수 select : 1 또는 2의 숫자/ 나머지 숫자는 처리X
# 매개변수 r : 원의 반지름(1 이상의 숫자)
# select = 1 ; 원의 둘레 계산해서 return
# select = 2 ; 원의 면적 계산해서 return

def round(select, r):
    # 함수 round는 매개변수 select와 매개변수 r 로 구성
    if select==1:
        # select 1일 경우 원의 둘레 계산(파이 대신 3.14 사용)
        result = (r*2)*3.14
        return result
        # return 값

    elif select==2:
        # select 2일 경우 원의 면적(넓이 계산)
        result = (r**2)*3.14
        return result
        # return 값
  

c = round(1,7)
print(c)
# 변수 c 를 생성하여 round 함수 호출(매개변수 2개)
# 해당 변수 출력하여 return 받은 값 출력