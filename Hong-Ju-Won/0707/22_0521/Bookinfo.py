# A 도서관 설정
from book import Abook
class Abookinfo:
    def __init__(self):
        self.booklist = []
    
    def viewbook(self, Abook):
        for Abook in self.booklist:
            Abook.bookinfo()
    
    def addbook(self, Abook):
        self.booklist.append(Abook)

    def delbook(self, title):
        select = None

        for Abook in self.booklist:
            if Abook.title == title:
                select = Abook

        if select != None:
            self.booklist.remove(select)
            
