# 리스트 안에 for문을 포함하는 - 리스트 내포
# 리스트 내포 쓰는 예제

a = [1,2,3,4]

result = [n*3 for n in a]
# append 함수 없이 a 리스트의 각 항목에 3을 곱한 결과를 result 리스트에 담음

print(result)

# a의 값을 n에 대입
# n*3을 계산해서 -> result 리스트안의 값에 추가
# result 값 출력
