# 리스트 안에 for문을 포함하는 - 리스트 내포
# 리스트 내포 쓰는 예제
# 구구단의 모든 결과 담는 프로그램 구현

result = [x*y for x in range(2,10)
              for y in range(1,10)]

print(result)

# result 리스트 안에
# 2~9 까지 세로 x
# 1~9 까제 가로 y
# [x2*y1, x2*y2, x2*y3, .... x2*y9, ...
# ... x9*y1, x9*y2, x9*y3, .... x9*y9]

