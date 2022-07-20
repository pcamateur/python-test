'''七分排序法，将一个列表找出最大值和最小值，平均分成七份，然后分别命名为：mini ml big mc small mr maxi ,分别对七个容器再次进行排序操作'''

from random import randint



mini_list, ml_list, big_list, mc_list, small_list, mr_list, maxi_list = [], [], [], [], [], [], []


def seven_division(lists):
    
    mini = min(lists)
    maxi = max(lists)

    divisions = (maxi - mini) // 7



    # mini_G = range(mini, mini + divisions)
    # ml_G = range(mini + divisions + 1, mini + divisions * 2)
    # big_G = range(mini + divisions * 2 + 1, mini + divisions * 3)
    # mc_G = range(mini + divisions * 3 + 1, mini + divisions * 4)
    # small_G = range(mini + divisions * 4 + 1, mini + divisions * 5)
    # mr_G = range(mini + divisions * 5 + 1, mini + divisions * 6)
    # maxi_G = range(mini + divisions * 6 + 1, mini + divisions * 7 + 1)

    

    for datas_list in lists:
        
        if datas_list >= mini and datas_list < (mini + divisions + 1):
            mini_list.append(datas_list)

        elif datas_list >= (mini + divisions + 1) and datas_list < (mini + divisions * 2 + 1):
            ml_list.append(datas_list)

        elif datas_list >= (mini + divisions * 2 + 1) and datas_list < (mini + divisions * 3 + 1):
            big_list.append(datas_list)

        elif datas_list >= (mini + divisions * 3 + 1) and datas_list < (mini + divisions * 4 + 1):
            mc_list.append(datas_list)

        elif datas_list >= (mini + divisions * 4 + 1) and datas_list < (mini + divisions * 5 + 1):
            small_list.append(datas_list)

        elif datas_list >= (mini + divisions * 5 + 1) and datas_list < (mini + divisions * 6 + 1):
            mr_list.append(datas_list)

        else:
            maxi_list.append(datas_list)




lis = [ok for ok in range(1500)]

seven_division(lis)

print(mini_list)
print(ml_list)
print(big_list)
print(mc_list)
print(small_list)
print(mr_list)
print(maxi_list)

print(len(mini_list))
print(len(ml_list))
print(len(big_list))
print(len(mc_list))
print(len(small_list))
print(len(mr_list))
print(len(maxi_list))