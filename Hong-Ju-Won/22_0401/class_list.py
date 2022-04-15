a = ["윤아", "제시카", "유리"]
b = ["태연", "티파니", "서현"]
c = ["효연", "수영", "써니"]


def class_list():
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
        select = input("a, b, c 중에 하나를 입력하세요. : ")
        if select == "a":
            print(a)
        elif select == "b":
            print(b)
        elif select == "c":
            print(c)
        else:
            
    
    elif choice == "추가":
        k2 = input("a, b, c 중 하나를 선택하여 입력하세요. : ")
        # 사용자가 "추가" 를 입력하면 a/b/c의 리스트 중 사용자가 선택한 리스트에 사용자가 입력한 이름 추가
        add_names = int(input("몇 개 추가하실지 써 주세요 : "))
       
        if k2 == "a":
            for i in range(add_names):
                names = input("이름을 입력해 주세요. : ")
                a.append(names)
            

        elif k2 == "b":
            for i in range(add_names):
                names = input("이름을 입력해 주세요. : ")
                b.append(names)
          
        
        elif k2 == "c":
            for i in range(add_names):
                names = input("이름을 입력해 주세요. : ")
                c.append(names)
        class_list()
        

    elif choice == "종료":
        print("종료하겠습니다.")
        exit
        # 종료할 때 종료 문구 뜨도록 해봄


#c = class_list(choice, names)
# '크리스탈' 이라는 이름이 리스트에 추가되서 나오도록 출력
#print(c)

class_list()
# 더 생각해야 할 것) a/b/c 중 어느 리스트에 이름 추가하도록 하는 부분