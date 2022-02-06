# 튜플 사용한 for문

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
    print(first)
    print(last)
    print(first*last)
    print(" ")

# a 리스트의 요소의 값이 튜플
# 각각의 요소가 자동으로 (first, last) 변수에 대입
# 대입된 상태로 원하는 값 출력