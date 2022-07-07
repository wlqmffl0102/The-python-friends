from Book import Abook
from Book import Bbook

class Abookmanager:
    
    def __init__(self):
        self.booklist = []
        # 책에 대한 정보가 들어갈 책 리스트 초기화
        # 책 리스트 생성

    def appendbook(self, book):
        # 책 추가하는 append 라는 함수
        self.booklist.append(book)
        # 위에 초기화한 booklist에 책 추가 한다는 내용
        # 책 제목, 저자가 들어있는 book 클래스 실행

    def showbooks(self):
        # 도서 목록 보기/ 북 리스트에 있는 책의 제목과 저자 출력
        for book in self.booklist:
            book.bookinfo()
            # booklist에 있는 책 제목, 저자 정보 출력
            # 이 부분이 뭔가 이상함

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

    def modifybook(self, title, title2):
        # 도서 수정하는 함수
        target = None #target이 없다면
        for book in self.booklist:
            if book.title == title:
                target = book

        if target != None:  # 수정해줄 target이 없지 않다면 책 제목을 재설정 해준다.
            target.setTitle(title2)

class Bbookmanager:
    
    def __init__(self):
        self.booklist = []
        # 책에 대한 정보가 들어갈 책 리스트 초기화
        # 책 리스트 생성

    def appendbook(self, book):
        # 책 추가하는 append 라는 함수
        self.booklist.append(book)
        # 위에 초기화한 booklist에 책 추가 한다는 내용
        # 책 제목, 저자가 들어있는 book 클래스 실행

    def showbooks(self):
        # 도서 목록 보기/ 북 리스트에 있는 책의 제목과 저자 출력
        for book in self.booklist:
            book.bookinfo()
            # booklist에 있는 책 제목, 저자 정보 출력
            # 이 부분이 뭔가 이상함

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

    def modifybook(self, title, title2):
        # 도서 수정하는 함수
        target = None #target이 없다면
        for book in self.booklist:
            if book.title == title:
                target = book

        if target != None:  # 수정해줄 target이 없지 않다면 책 제목을 재설정 해준다.
            target.setTitle(title2)