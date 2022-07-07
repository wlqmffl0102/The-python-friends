from Book import book
from Bookmanager import bookmanager

system = bookmanager()
# system 이라는 변수를 설정하여 Bookmanager.py파일에 있는 
# 클래스 bookmanager() 호출

running = True
# 운영 running 이 참일 때 while 문을 돌려보자

while running == True:

    # 도서관리 시스템 중 원하는 메뉴 입력할 수 있도록 세팅
    print('''
-------------------------------------------
도서 관리 시스템이 오신 걸 환영합니다!
원하시는 메뉴를 고르세요.

1. 보유 도서 리스트 보기
2. 도서 검색
3. 도서 추가
4. 도서 삭제
5. 도서 수정
6. 나가기
''')

    menu = input()

    if menu == "1":   
        # 보유 도서 리스트 보기
        print("보유 도서 리스트 입니다.")
        system.showbooks()
    
    if menu == "2":   
        # 도서 검색//// 이게 문제
        print("도서 검색 메뉴입니다. ")
        title = input("제목 : ")
        system.searchbooks()

    elif menu == "3":
        # 도서 추가
        print("도서 추가 메뉴입니다. ")
        title = input("제목 : ")
        author = input("저자 : ")
        system.appendbook(book(title, author))

    elif menu == "4":
        # 도서 삭제
        print("도서 삭제 메뉴입니다. ")
        title = input("제목 : ")
        system.removebook(title)

    elif menu == "5":
        # 도서 수정
        print("도서 수정 메뉴입니다. ")
        title = input("제목 : ")
        title2 = input("바꿀 제목 : ")
        system.modifybook(title, title2)

    elif menu == "6": 
        # 6번일 경우 시스템 종료
        print("시스템을 종료합니다.")
        running = False

    else:
        print("""올바른 번호를 입력하세요!
-------------------------------------------""")