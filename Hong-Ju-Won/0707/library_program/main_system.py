from threading import main_thread
from Book import Abook
from Book import Bbook
from Bookmanager import Abookmanager
from Bookmanager import Bbookmanager
from mainA import Abookmanager
from mainB import Bbookmanager


lib = True

while lib == True:
    print("""다음 중 서비스를 이용할 도서관을 고르시오.
[A 도서관] 의 서비스를 이용하려면 A 를 입력하시오.
[B 도서관] 의 서비스를 이용하려면 B 를 입력하시오.""")

    select = input()
    if select == "A":
        print("A 도서관 시스템입니다.")
        Abookmanager()

    elif select == "B":
        print("B 도서관 시스템입니다.")
        Bbookmanager()

    else:
        print("다시 입력해 주세요.")





    