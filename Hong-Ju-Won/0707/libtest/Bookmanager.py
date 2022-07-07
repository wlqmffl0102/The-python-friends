from Book import book

class bookmanager:
    
    def __init__(self):
        self.booklist = []
        # 책에 대한 정보가 들어갈 책 리스트 초기화
        # 책 리스트 생성

    def showbooks(self):
        # 도서 목록 보기/ 북 리스트에 있는 책의 제목과 저자 출력
        for book in self.booklist:
            book.bookinfo()
            # booklist에 있는 책 제목, 저자 정보 출력

    def searchbooks(self, title):
        # 도서 검색하는 함수
        # booklist 안에 있는 책 제목이 내가 찾으려는 책 제목과 같다면
        # bookinfo 함수 실행시켜서 그 책에 관한 정보 출력 하는게 목표...
        for book in self.booklist:
            if book.bookinfo(title) == title:
                book.bookinfo()

            else:
                print("해당 도서는 도서관에 없습니다.")

    def appendbook(self, book):
        # 책 추가하는 append 라는 함수
        self.booklist.append(book)
        # 위에 초기화한 booklist에 책 추가 한다는 내용
        # 책 제목, 저자가 들어있는 book 클래스 실행

    def removebook(self, title):
        # 도서 삭제 하는 함수
        target = None
        # target이 없으면
        for book in self.booklist:
            # 책이 booklist에 존재하지 않을 경우
            if book.title == title:
                target = book  #target은 삭제 대상이 아니다.

        if target != None: # 찾는 책이 없지 않다면 삭제해준다. target을
            self.booklist.remove(target)

        """for book in self.booklist():
                book.title == title
                title = input("해당 도서를 삭제하시겠습니까? [yes/no] : ")
                if title == "yes":
                    print("해당 도서를 삭제합니다.")
                    self.booklist.remove(title)

                elif title == "no":
                    print("해당 도서를 삭제 하지 않습니다.")
            """
            # 해당 방법도 사용해 보았으나 실패

    def modifybook(self, title, title2):
        # 도서 수정하는 함수
        target = None #target이 없다면
        for book in self.booklist:
            if book.title == title:
                target = book
                
        if target != None:  # 수정해줄 target이 없지 않다면 책 제목을 재설정 해준다.
            target.setTitle(title2) # 변수 title을 title2 로 재설정

    # removebook 와 modifybook 은 인터넷 검색으로 찾아봤습니다.
    # remove 및 구성방식이 헷갈려서 찾아보다가 도서 수정 부분도 있길래 가져와 봤습니다.