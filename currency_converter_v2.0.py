"""
Currency Converter 小象学院 梁斌老师 Python基础入门课 课件
Version : v2.0
Date: Feb 21 2019
Student: pcamateur
New:根据输入判断是人民币还是美元，进行相应的换算计算
"""

# 汇率
USD_VS_RMB = 6.77

# 带单位的货币的输入
currency_str_value = input('请输入带单位的货币金额： ')

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
