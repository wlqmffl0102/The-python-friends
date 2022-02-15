# 가위바위보 게임
# 1. 게임 선택 화면 (1. 게임 시작, 2. 게임 종료)
# 2. 게임 시작을 눌렀을 경우 
# -------- 게임 시작 ---------
# 1) 사용자로 부터 1(가위) 2(바위) 3(보) 의 입력 받음
# 2) 3판 중 더 많이 이긴 쪽 우승, 게임 끝
# 3) 3판째 까지 무승부이면 계속해서 게임이 연장
# 4) 4판 이후부터 1회라도 더 많이 이기면 그쪽이 우승, 게임 끝


# 1(가위) 2(바위) 3(보) 중 하나를 선택하세요
# 2-1 1~3 이외의 숫자가 나오면 다시 선택
# 2-2 1~3의 숫자가 선택되면 컴퓨터가 랜덤으로 1~3의 숫자를(난수로) 생성
# 2-2 사용자 vs 컴퓨터

# 결과값 저장(사용자, 컴퓨터)

#3. 게임의 승패가 갈리면 다시 게임을 할지 종료 할지 선택

import random
Game = True
start_or_end = False
game_count = 0
game_start = True


while Game:
    print("1. 게임 시작")
    print("2. 게임 종료")
    print("-------------")
    start = int(input("1 또는 2 선택 : "))
    if start<0 or start>2:
        print("1 또는 2로 선택해주세요.")
        continue
    elif start==1:
        start_or_end = True
        user_result = 0
        computer_result = 0

        while start_or_end:
            print("""
---------------------- 게임 시작 ------------------------
1) 사용자로 부터 1(가위) 2(바위) 3(보) 의 입력 받음
2) 3판 중 더 많이 이긴 쪽 우승, 게임 끝
3) 3판째 까지 무승부이면 계속해서 게임이 연장
4) 4판 이후부터 1회라도 더 많이 이기면 그쪽이 우승, 게임 끝
---------------------------------------------------------               
                """)
            while game_start:
                game_count += 1
                print("\n"+str(game_count) + "번째 판")
                
                user_selection = int(input("1(가위) or 2(바위) or 3(보) 중 하나를 선택해 주세요. : "))
                computer_selection = random.randrange(1,4)
                if user_selection == 1:
                    if computer_selection == 1:
                        pass
                        print(str(game_count)+"번째 판 비겼습니다.")
                    
                    elif computer_selection == 2:
                        computer_result += 1
                        print("\n유저 : " + str(user_result) + "점")
                        print("컴퓨터 : " + str(computer_result) + "점")
                        print("\n"+str(game_count)+"번째 판 졌습니다.")
                       
                    elif computer_selection == 3:
                        user_result += 1
                        print("\n유저 : " + str(user_result) + "점")
                        print("컴퓨터 : " + str(computer_result) + "점")
                        print("\n"+str(game_count)+"번째 판 이겼습니다.")
                       
                elif user_selection == 2:
                    if computer_selection == 1:
                        user_result += 1
                        print("\n유저 : " + str(user_result) + "점")
                        print("컴퓨터 : " + str(computer_result) + "점")
                        print("\n"+str(game_count)+"번째 판 이겼습니다.")
                        
                    elif computer_selection == 2:
                        pass
                        print(str(game_count)+"번째 판 비겼습니다.")
                        
                    elif computer_selection == 3:
                        computer_result += 1
                        print("\n유저 : " + str(user_result) + "점")
                        print("컴퓨터 : " + str(computer_result) + "점")
                        print("\n"+str(game_count)+"번째 판 졌습니다.")
                        
                elif user_selection == 3:
                    if computer_selection == 1:
                        computer_result += 1
                        print("\n유저 : " + str(user_result) + "점")
                        print("컴퓨터 : " + str(computer_result) + "점")
                        print("\n"+str(game_count)+"번째 판 졌습니다.")
                        
                    elif computer_selection == 2:
                        user_result += 1
                        print("\n유저 : " + str(user_result) + "점")
                        print("컴퓨터 : " + str(computer_result) + "점")
                        print("\n"+str(game_count)+"번째 판 이겼습니다.")
                        
                    elif computer_selection == 3:
                        pass
                        print(str(game_count)+"번째 판 비겼습니다.")
                        
                if game_count >= 3:
                    if user_result == computer_result:
                        continue
                    else:
                        if user_result>computer_result:
                            print("\n이겼습니다.")
                        elif user_result<computer_result:
                            print("\n졌습니다.")
                        print("----------------------")
                        print("다시 하시겠습니까? 1. 게임 재시작 2. 게임 종료")
                        a = int(input("1. 게임 재시작, 2. 게임 종료 : "))
                        if a==1:
                            user_selection = 0
                            computer_selection = 0
                            user_result = 0
                            computer_result = 0
                            game_count = 0
                            continue
                        elif a==2:
                            print("\n게임을 종료합니다.")
                            start_or_end = False
                            Game = True
                            game_start = False
                          
                            
                        
    elif start==2:
        print("\n게임을 종료합니다.")
        break


