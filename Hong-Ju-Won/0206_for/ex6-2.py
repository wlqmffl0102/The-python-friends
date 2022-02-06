# 리스트 안에 for문을 포함하는 - 리스트 내포
# 리스트 내포 쓰는 예제

a = [1,2,3,4]

result = [n*3 for n in a if n%2==0]
# if 조건 생략 가능
# [ 표현식 for 항목 in 반복 가능 객체 if 조건문 ]
# a 리스트에 3을 곱한 값 중에 짝수인 값을 result 리스트 안에 담음

print(result)

# a의 값을 n에 대입
# n*3을 계산해서 -> result 리스트안의 값에 추가
# result 값 출력
