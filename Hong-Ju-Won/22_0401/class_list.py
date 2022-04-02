
a = ["윤아", "제시카", "유리"]
b = ["태연", "티파니", "서현"]
c = ["효연", "수영", "써니"]


def class_list(choice, *args):
    print("""-------------------------------------
1. A클래스, B클래스, C 클래스 선택해 내용 출력
2. A클래스, B클래스, C 클래스 선택해 내용 추가
3. 종료
-------------------------------------""")
# 프로그램 시작 시 메뉴 중 선택할 수 있도록 함수 실행하면 제일 먼저 메뉴 출력
    choice = input("출력, 추가, 종료 중 하나를 선택하여 입력하세요. : ")
    # 사용자로 부터 어떤 선택을 할지 입력 받기(입력 받은 후 동작)
    if choice == "출력":
         # 사용자가 "출력" 을 입력하면 a/b/c의 리스트 각각 출력
        if choice in a:
            print(a)
        elif choice in b:
            print(b)
        elif choice in c:
            print(c)
    
    elif choice == "추가":
        k2 = input("a, b, c 중 하나를 선택하여 입력하세요. : ")
        # 사용자가 "추가" 를 입력하면 a/b/c의 리스트 중 사용자가 선택한 리스트에 사용자가 입력한 이름 추가
        if k2 in a:
            a.append(args)
        elif k2 in b:
            b.append(args)
        elif k2 in c:
            c.append(args)

    elif choice == "종료":
        print("종료하겠습니다.")



c = class_list("추가", "크리스탈")
print(c)
