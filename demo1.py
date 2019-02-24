import random

# 输出标题
print("*" * 50)
print("\t" * 2 + "石头剪子布V1.0")
print("\t\t\tpowered by bboysoul")
print("*" * 50)

# 判断谁输谁赢


def judg():
    if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print("你赢了")
    elif computer == player:
        print("平局")
    else:
        print("你输了")
# 判断用户输入，当a=1的时候说明用户输入的内容违规


def pt_player():
    a = 0
    if player == 0:
        print("你输入的是剪刀")
    elif player == 1:
        print("你输入的是石头")
    elif player == 2:
        print("你输入的是布")
    else:
        print("你输入的数值有误,请重新输入")
        a = 1
    return a

# 判断电脑输入


def pt_computer():
    if computer == 0:
        print("电脑输入的是剪刀")
    elif computer == 1:
        print("电脑输入的是石头")
    else:
        print("电脑输入的是布")


# 程序开始执行
while True:
    # 异常处理，不能输入字母
    try:
        player = int(input("请输入 0剪刀 1石头 2布："))
        computer = random.randint(0, 2)
        a = pt_player()
        if a == 1:
            continue
        else:
            pass
        pt_computer()
        judg()
    except ValueError:
        print("请不要输入其他符号")
