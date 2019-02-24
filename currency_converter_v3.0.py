"""
Currency Converter 小象学院 梁斌老师 Python基础入门课 课件
Version : v3.0
Date: Feb 22 2019
Student: pcamateur
2.0 new:根据输入判断是人民币还是美元，进行相应的换算计算
3.0 new:程序可以一直运行，直到用户选择退出
"""

# 汇率
USD_VS_RMB = 6.77

# 带单位的货币的输入
currency_str_value = input('请输入带单位的货币金额(退出程序请输入Q)： ')

# 循环次数初始赋值
i = 0

while currency_str_value != 'Q':

    # 根据循环次数记数赋值公式
    i = i + 1

    # 输出循环次数值
    # print('循环次数', i)

    # 获取货币单位
    unit = currency_str_value[-3:]

    if unit == "CNY":
        # 输入的是人民币
        rmb_str_value = currency_str_value[:-3]
        # 将字符串转换为数字
        rmb_value = eval(rmb_str_value)
        # 汇率换算
        usd_value = rmb_value / USD_VS_RMB

        # 输出结果
        print('美元（USD）金额是： ', usd_value)

    elif unit == "USD":
        # 输入的是美元
        usd_str_value = currency_str_value[:-3]
        # 将字符串转换为数字
        usd_value = eval(usd_str_value)
        # 汇率换算
        rmb_value = usd_value * USD_VS_RMB

        # 输出结果
        print('人民币（CNY）金额是： ', rmb_value)

    else:
        # 其它情况
        print('目前版本尚不支持该种货币！')


    print('*********#########这是分割符，继续执行吧#########*********')
    # 带单位的货币的输入 为防止死循环 当循环结束后执行此语句
    currency_str_value = input('请输入带单位的货币金额(退出程序请输入Q)： ')

print('程序已退出！')
