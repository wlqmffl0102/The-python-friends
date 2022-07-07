from book import Abook
from Bookinfo import Abookinfo

info = Abookinfo()

system = True

while system == True:
    lib = input("""A 도서관/ B 도서관/ C 도서관 중
원하는 도서관을 선택해서 A, B, C 중 하나를 입력하시오.""")
   
    if lib =='A':
        menu = int(input("""---------------------------------------------------
도서 관리 시스템 입니다. 
해당 메뉴 중 원하는 번호를 선택해서 입력하시오.

1. 보유 도서 리스트 보기
2. 도서 검색
3. 도서 추가
4. 도서 삭제
---------------------------------------------------"""))
        if menu == 1: # 보유 도서 리스트 보기
            Abookinfo.viewbook()

        elif menu == 3: #도서 추가
            title = input("도서명을 입력하시오 : ")
            bookcode = input("도서 코드를 입력하시오 : ")
            author = input("저자를 입력하시오 : ")
            genre = input("도서 장르를 입력하시오 : ")
            Abookinfo.addbook(Abook(title, bookcode, author, genre))
        
        elif menu == 4: #도서 삭제
            title = input("도서명을 입력하시오 : ")
            Abookinfo.delbook(title)

        

