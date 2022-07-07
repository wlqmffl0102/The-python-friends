class book:
    # book 이라는 클래스 안에
    def __init__(self, title, author):
        self.title = title
        self.author = author

     #클래스 기본자 생성, 책 제목/저자 초기화

    def bookinfo(self):
        print("책 제목 : " + self.title)
        print("저자 : " + self.author)
    # 책 제목과 저자를 출력하는 함수 bookinfo

   # def searchinfo(self):
   # 검색할 정보 관련 함수 생성해서 어떻게 해보려고 했으나
   # 실패..
    #    print("책 제목 : " + self.title)
    #    print("저자 : " + self.author)

    def setTitle(self, title):
        # 책 내용 수정할 때
        # 다시 입력하기 위해
        self.title = title

    # 책 제목을 설정하는 함수

