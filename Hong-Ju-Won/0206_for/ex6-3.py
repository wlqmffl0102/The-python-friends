# 리스트 안에 for문을 포함하는 - 리스트 내포
# 리스트 내포 쓰는 예제
# 구구단의 모든 결과 담는 프로그램 구현

result = [x*y for x in range(2,10)
              for y in range(1,10)]

print(result)

