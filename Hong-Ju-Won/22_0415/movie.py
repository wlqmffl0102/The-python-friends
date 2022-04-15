
user_list = ["abcd"]
# 회원가입된 사용자 id를 저장하는 리스트
movie_info = {'abcd':'쿵푸팬더'}
# 아이디와 예매한 영화를 저장하는 딕셔너리

def movie():
    print("""-------------------------------------
1.  회원 가입
2.  영화 예매
3.  예매 확인
4.  예매 취소
5.  회원 탈퇴
6.  종료
-------------------------------------""")
# 처음 함수를 출력하면 나오는 화면, 메뉴 출력

    choice = input("1 ~ 6 중 원하는 서비스 하나를 선택하여 한글로 입력하세요. : ")
    # 1~6 서비스 중 원하는 것을 한글로 입력 받기
    
    if choice == "회원 가입":
        # 1. 원하는 것이 회원 가입일 경우
        while True:
            check = input("회원 가입할 사용자 id를 입력해 주세요. :")

            if check not in user_list:
                user_list.append(check)
                # 사용자로부터 입력받은 id가 리스트에 없는 경우 추가
                print("회원 가입을 완료 하였습니다.")
                break
                     
            else:    
                # 사용자로부터 입력받은 id가 리스트에 있는 경우 이미 가입된 회원이라는 문구 출력
                print("이미 회원 가입된 id 입니다.")
                continue


    elif choice == "영화 예매":
        # 2. 원하는 것이 영화 예매일 경우
        while True:
            check = input("사용자 id를 입력해 주세요. :")
            if check in user_list:
                # 입력 받은 id가 리스트에 있을 경우
                print("""--------------------------
<상영 영화 정보>
반지의 제왕
해리포터
쿵푸팬더
--------------------------""")

                # 회원 가입된 id에 한해서 영화 예매 진행
                usermovie = input("예매할 영화를 입력해 주세요 : ")
                movie_info[check] = usermovie
                # 입력받은 아이디와 영화 이름 movie_info 딕셔너리에 추가
                break
            
            else:
                # 리스트에 입력받은 id가 없을 경우 회원가입 문구 출력
                print("회원 가입되지 않은 id 입니다.")
                continue

    elif choice == "예매 확인":
        #3. 원하는 것이 예매 확인일 경우
        while True:
            check = input("사용자 id를 입력해 주세요. :")
            if check in user_list:
                # 입력 받은 사용자 id가 리스트에 있을 경우 
                if check in movie_info.keys():
                    # 예매를 한 경우 예매 정보 출력
                    print("%s님은 %s를 예매하셨습니다." % (check,movie_info[check]))
                    break
                else:
                    # 사용자 id는 리스트에 있지만 예매를 하지 않은 경우
                    print("예매를 하지 않으셨습니다.")
                    break
            else:
                # 리스트에 입력받은 id가 없을 경우 회원가입 문구 출력
                print("회원 가입되지 않은 id 입니다.")
                continue
    
    elif choice == "예매 취소":
        # 4. 원하는 것이 예매 취소일 경우
        while True:
            check = input("사용자 id를 입력해 주세요. :")
            if check in user_list:
                # 입력 받은 사용자 id가 리스트에 있을 경우
                print("%s님은 %s를 예매하셨습니다." % (check,movie_info[check]))
                cancel = input("예매한 영화를 취소하시겠습니까?(yes/no) : ")
                # 예매 정보 한 번 출력해서 보여 준 후 취소 여부 묻기/ yes 또는 no 로 대답 입력받기
                if cancel == "yes":
                    # 사용자로 부터 yes(취소) 한다고 입력 받은 경우
                    del movie_info[check]
                    # movie_info 딕셔너리에서 해당 정보 삭제
                    print("예매 취소를 완료하였습니다.")
                    break
                else:
                    # 사용자로 부터 no(취소 안함)이라고 입력 받은 경우  
                    print("예매 취소에 실패했습니다.")
                    break
            else:
                # 리스트에 입력받은 id가 없을 경우 회원가입 문구 출력
                print("회원 가입되지 않은 id 입니다.")
                continue
    
    elif choice == "회원 탈퇴":
        # 5. 원하는 것이 회원 탈퇴일 경우
         while True:
            check = input("사용자 id를 입력해 주세요. :")
            if check in user_list:
                # 입력 받은 사용자 id가 리스트에 있을 경우
                cancel = input("회원을 탈퇴 하시겠습니까?(yes/no) : ")
                # 회원 탈퇴 여부 한번 더 물어보기
                if cancel == "yes":
                    # 사용자로 부터 yes(탈퇴) 입력 받았을 경우
                    del movie_info[check]
                    user_list.remove(check)
                    # 회원 탈퇴 이므로 사용자 id 리스트와 영화정보 딕셔너리에서 모두 해당 사용자 정보 삭제
                    print("회원 탈퇴를 완료하였습니다.")
                    # 탈퇴 완료 문구 출력
                    break
                else:
                    # 사용자로 부터 no(탈퇴 안함) 입력 받았을 경우
                    print("회원 탈퇴에 실패하였습니다.")
                    # 탈퇴 실패 문구 출력
                    #(실수로 눌렀을 경우 해당)
                    break
            else:
                # 리스트에 입력받은 id가 없을 경우 회원가입 문구 출력
                print("회원 가입되지 않은 id 입니다.")
                continue
    
    elif choice == "종료":
        # 원하는 것이 종료일 경우
        print("종료하겠습니다.")
        exit


movie()







