class Abook: 
    # A 도서관 시스템에 사용될 Abook 클래스
    def __init__(self, title, author):
        self.title = title
        self.author = author

     #클래스 기본자 생성, 책 제목/저자 초기화

    def bookinfo(self):
        print("책 제목 : " + self.title)
        print("저자 : " + self.author)
    # 책 제목과 저자를 출력하는 함수 bookinfo

    def setTitle(self, title):
        self.title = title
    # 책 제목을 설정하는 함수


class Bbook:
    # A 도서관 시스템에 사용될 Bbook 클래스
    def __init__(self, title, author):
        self.title = title
        self.author = author

     #클래스 기본자 생성, 책 제목/저자 초기화

    def bookinfo(self):
        print("책 제목 : " + self.title)
        print("저자 : " + self.author)
    # 책 제목과 저자를 출력하는 함수 bookinfo

    def setTitle(self, title):
        self.title = title

    # 책 제목을 설정하는 함수
