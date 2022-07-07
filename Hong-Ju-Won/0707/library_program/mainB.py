from Book import Bbook
from Bookmanager import Bbookmanager

system = Bbookmanager()

running = True

while running == True:

    print('''도서 관리 시스템이 오신 걸 환영합니다!
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
        system.showbooks()
    
    if menu == "2":   
        # 보유 도서 리스트 보기
        title = input("제목 : ")
        system.searchbooks()

    elif menu == "3":
        # 도서 추가
        title = input("제목 : ")
        author = input("저자 : ")
        system.appendbook(Bbook(title, author))

    elif menu == "4":
        # 도서 삭제
        title = input("제목 : ")
        system.removebook(title)

    elif menu == "5":
        # 도서 수정
        title = input("제목 : ")
        title2 = input("바꿀 제목 : ")
        system.modifybook(title, title2)

    elif menu == "6":
        running = False

    else:
        print("""올바른 번호를 입력하세요!
-------------------------------------------""")