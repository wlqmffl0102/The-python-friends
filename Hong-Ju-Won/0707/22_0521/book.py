
class Abook:
    def __init__(self, title, bookcode, author, genre):
        self.title = title
        self.bookcode = bookcode
        self.author = author
        self.genre = genre

    def bookinfo(self):
        print("도서명 : " + self.title)
        print("도서 코드 : " + self.bookcode)
        print("저자 : " + self.author)
        print("도서 장르 : " + self.genre)

    def newbook(self, title):
        self.title = title
       