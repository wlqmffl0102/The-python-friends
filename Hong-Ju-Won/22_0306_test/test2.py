fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

f = input("좋아하는 계절은? : ")

# if f in fruit.values():
if f in fruit.keys():
    print("정답입니다.")
else:
    print("오답입니다.")
