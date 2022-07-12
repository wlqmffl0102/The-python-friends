from Book import book
from Bookmanager import bookmanager

system_a = bookmanager()
system_b = bookmanager()
# system 이라는 변수를 설정하여 Bookmanager.py파일에 있는 
# 클래스 bookmanager() 호출

running = True
# 전체 프로그램 while문 돌릴 때 사용
# 총 도서 관리 프로그램 메뉴 

while running == True:

    # 도서관리 시스템 중 원하는 메뉴 입력할 수 있도록 세팅
    print('''
-----------------------------------------------------------

도서 관리 시스템이 오신 걸 환영합니다!
사용하실 도서관 시스템을 선택하시오.[A/B/종료 중 입력해 주세요.]

* A 도서관
* B 도서관
* 종료

-----------------------------------------------------------
''')

    select = input()

    if select == "A":
    # A를 입력했을 경우 
    # A 도서관 관리 시스템으로 이동해 각 메뉴 수행 

        proA = True
        # A 도서 관리 시스템 전용 while문

        while proA == True:
            print('''
-------------------------------------------------
[A 도서관 관리 시스템]
A 도서관의 도서 관리 시스템이 오신 걸 환영합니다!
원하시는 메뉴를 고르세요.

1. 보유 도서 리스트 보기
2. 도서 검색
3. 도서 추가
4. 도서 삭제
5. 도서 수정
6. 나가기
-------------------------------------------------
''')

            menu = input()

            if menu == "1":   
            # 보유 도서 리스트 보기
                print("보유 도서 리스트 입니다.")
                system_a.showbooks()
    
            if menu == "2":   
            # 도서 검색//// 이게 문제
                print("도서 검색 메뉴입니다. ")
                title = input("제목 : ")
                system_a.searchbooks()

            elif menu == "3":
            # 도서 추가
                print("도서 추가 메뉴입니다. ")
                title = input("제목 : ")
                author = input("저자 : ")
                system_a.appendbook(book(title, author))

            elif menu == "4":
            # 도서 삭제
                print("도서 삭제 메뉴입니다. ")
                title = input("제목 : ")
                system_a.removebook(title)

            elif menu == "5":
            # 도서 수정
                print("도서 수정 메뉴입니다. ")
                title = input("제목 : ")
                title2 = input("바꿀 제목 : ")
                system_a.modifybook(title, title2)

            elif menu == "6": 
            # 6번일 경우 A 도서 관리 시스템 종료
            # 종료 후 전체 메뉴로 돌아오도록 설정
                print("A 도서관의 도서 관리 시스템을 종료합니다.")
                proA = False

            else:
                print("""올바른 번호를 입력하세요!
-------------------------------------------------
""")


    elif select == "B":
    # B를 입력했을 경우 
    # B 도서관 관리 시스템으로 이동해 각 메뉴 수행 

        proB = True
        # B 도서 관리 시스템 전용 while문

        while proB == True:
            print('''
-------------------------------------------------
[B 도서관 관리 시스템]
B 도서관의 도서 관리 시스템이 오신 걸 환영합니다!
원하시는 메뉴를 고르세요.

1. 보유 도서 리스트 보기
2. 도서 검색
3. 도서 추가
4. 도서 삭제
5. 도서 수정
6. 나가기
-------------------------------------------------
''')

            menu = input()

            if menu == "1":   
            # 보유 도서 리스트 보기
                print("보유 도서 리스트 입니다.")
                system_b.showbooks()
    
            if menu == "2":   
            # 도서 검색//// 이게 문제
                print("도서 검색 메뉴입니다. ")
                title = input("제목 : ")
                system_b.searchbooks()

            elif menu == "3":
            # 도서 추가
                print("도서 추가 메뉴입니다. ")
                title = input("제목 : ")
                author = input("저자 : ")
                system_b.appendbook(book(title, author))

            elif menu == "4":
            # 도서 삭제
                print("도서 삭제 메뉴입니다. ")
                title = input("제목 : ")
                system_b.removebook(title)

            elif menu == "5":
            # 도서 수정
                print("도서 수정 메뉴입니다. ")
                title = input("제목 : ")
                title2 = input("바꿀 제목 : ")
                system_b.modifybook(title, title2)

            elif menu == "6": 
            # 6번일 경우 시스템 종료
            # 종료 후 전체 메뉴로 돌아오도록 설정
                print("B 도서관의 도서 관리 시스템을 종료합니다.")
                proB = False

            else:
                print("""올바른 번호를 입력하세요!
-------------------------------------------""")

    
    elif select == "종료":
        # A/B 도서관 선택하라는 창 종료
        # 종료라는 단어를 입력하면 종료
        print("전체 시스템을 종료합니다.")
        running = False

    else:
        print("잘못 입력하였습니다. 다시 입력해 주세요.")
        # 전체 도서 시스템 메뉴 예외 처리) 
        # A/B/종료 이 외의 단어 입력 시 다시 입력해 달라는 문구 출력