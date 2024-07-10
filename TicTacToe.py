import os
import random


while(True):
    # *****Global Variable*****
    completed_formate_line = []
    remain_inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    winnum = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for_one_time = True


    # *****Functions*****
    def isDraw():
        if remain_inputs == []:
            os.system('cls')
            print(formate)
            print("*****DRAW*****")
            return True
        return False
    def didAnyoneWin(user_or_computer_inputes):
        for item in winnum:
            if item[0] in user_or_computer_inputes and item[1] in user_or_computer_inputes and item[2] in user_or_computer_inputes:
                return True
        return False     
    def computerInputSelector(user_inputes, computer_inputes):
        check, prevent_num = isWinningHowToPrevent(computer_inputes)
        if check:
            return prevent_num

        check, prevent_num = isWinningHowToPrevent(user_inputes)
        if check:
                return prevent_num
        return random.choice(remain_inputs)
    def isWinningHowToPrevent(user_or_computer_inputes):
        for item in winnum:
            if item in completed_formate_line:
                continue
            if (item[0] in user_or_computer_inputes and item[1] in user_or_computer_inputes) or (item[0] in user_or_computer_inputes and item[2] in user_or_computer_inputes) or (item[1] in user_or_computer_inputes and item[2] in user_or_computer_inputes):
                completed_formate_line.append(item)
                num_not_in_list = whichNumIsNotInList(user_or_computer_inputes, item)
                if num_not_in_list != False:
                    return True, num_not_in_list 
        return False, 0
    def whichNumIsNotInList(user_or_computer_inputes, list):
        for i in list:
            if i not in user_or_computer_inputes:
                if i in remain_inputs:
                    return i
                else:
                    return False


    # *****Some importent variable*****
    user_inputes = []
    computer_inputes = []
    formate = (''' 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9''')


    # *****Mode Of Game*****
    while(True):
        try: 
            os.system('cls')
            print('''1. Easy
2. Medium
3. Impossible''')
            game_mode = int(input("Please Enter Game Mode: "))
            if game_mode not in [1, 2, 3]:
                continue
            print('''1. You
2. Computer''')
            first_player = int(input("Who will play first: "))
            if first_player not in [1, 2]:
                continue
            user_input = 0
            break
        except:
            continue


    # *****Main*****

    while(True):
        os.system('cls')
        print(formate)


        # *****User:
        if first_player == 1:
            try: 
                user_input = int(input("Enter youer choice: "))
                remain_inputs.remove(user_input)
            except:
                continue
            user_inputes.append(user_input)
            formate = formate.replace(str(user_input), "O")
            if didAnyoneWin(user_inputes):
                formate = formate.replace(str(user_input), "O")
                os.system('cls')
                print(formate)
                print("*****You Win*****")
                break
            if isDraw():
                break
        first_player = 1

        # *****Computer:
        if game_mode == 1:
            computer_input = random.choice(remain_inputs)
        if game_mode == 2:
            computer_input = computerInputSelector(user_inputes, computer_inputes)  
        if game_mode == 3:
            if for_one_time:
                if user_input in [1, 3, 7, 9]:
                    for_one_time = None
                    computer_input = 5
                if user_input in [2, 4, 5, 6, 8]:
                    for_one_time = None
                    computer_input = random.choice([1, 3, 7, 9])
            if for_one_time != None:
                computer_input = computerInputSelector(user_inputes, computer_inputes)
            for_one_time = False
        remain_inputs.remove(computer_input)
        computer_inputes.append(computer_input)
        formate = formate.replace(str(computer_input), "X")
        if didAnyoneWin(computer_inputes):
            formate = formate.replace(str(computer_input), "X")
            os.system('cls')
            print(formate)
            print("*****Computer Win*****")
            break
        if isDraw():
            break  
    input()