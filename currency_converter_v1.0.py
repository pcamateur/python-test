"""
小象学院 梁斌老师 Python基础入门课 课件
Currency Converter
Version : v1.0
Date: Feb 21 2019
Student: pcamateur
"""

# 汇率
USD_VS_RMB = 6.77

# 人民币的输入
rmb_str_value = input('请输入人民币（CNY）金额： ')

# 将字符串转换为数字
rmb_value = eval(rmb_str_value)


# 汇率换算
usd_value = rmb_value / USD_VS_RMB

# 输出结果
print('美元（USD）金额是： ', usd_value)
