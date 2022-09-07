# 本程序为jetbrains academy的任务 主题为last pencil
# 参考链接：https://hyperskill.org/projects/258
# 个人邀请码：https://hyperskill.org/join/6ac34c25f
import random

PENCIL = '|'
string_1 = 'How many pencils would you like to use:'
string_2 = 'Who will be the first (John, Jack):'
players = ['John', 'Jack']
string_3 = "'s turn:"
pencils = 0


# 获取用户输入
def get_pencils():
    global pencils
    while True:
        try:
            pencils = int(input())
        except ValueError:
            print('The number of pencils should be numeric')
            continue
        else:
            if pencils == 0:
                print('The number of pencils should be positive')
                continue
            else:
                break


# 游戏规则
def gameplay():
    global pencils
    global players
    global PENCIL
    while True:
        player = str(input())
        if player != players[0] and player != players[1]:
            print("Choose between 'John' and 'Jack'")
            continue
        else:
            break
    if player == players[0]:
        count = 0
        bot = -1
    else:
        count = 1
        bot = 1
    while pencils > 0:
        print(PENCIL * pencils)
        if count % 2 == 0:
            print(players[0] + string_3)
        else:
            print(players[1] + string_3)
        while True:
            # bot算法
            if bot == 1:
                if pencils % 4 == 0:
                    value = 3
                if pencils % 4 == 3:
                    value = 2
                if pencils % 4 == 2:
                    value = 1
                if pencils % 4 == 1:
                    value = 1
                print(value)
                break
            # 用户算法
            else:
                try:
                    value = int(input())
                except ValueError:
                    print("Possible values: '1', '2' or '3'")
                    continue
                else:
                    if value > 3 or value < 1:
                        print("Possible values: '1', '2' or '3'")
                        continue
                    elif pencils - value < 0:
                        print('Too many pencils were taken')
                        continue
                    else:
                        break
        bot *= -1
        pencils -= value
        if pencils == 0:
            winner = players[(count + 1) % 2]
        count += 1

    print(f"{winner}" + ' won!')


print(string_1)
get_pencils()
random.seed(pencils)
print(string_2)
gameplay()
