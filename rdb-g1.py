import requests
from bs4 import BeautifulSoup as bs

# 这段代码是一个用于查询双色球历史开奖号码的程序。以下是对每个函数的注释说明：

# get_html(url):

# 从给定的URL获取网页的HTML内容。
# 参数 url：要获取的网页的URL。
# 返回值：如果成功获取到HTML内容，则返回HTML文本；否则返回 None。

# get_data(wps):

# 从HTML内容中解析出双色球历史开奖数据。
# 参数 wps：包含历史开奖数据的网页的URL。
# 返回值：包含历史开奖数据的列表。

# get_values(datas):

# 从历史开奖数据中提取时间、红球、蓝球和日期。
# 参数 datas：包含历史开奖数据的列表。
# 返回值：分别包含时间、红球、蓝球和日期的列表。

# list_dic(times, rb, bb, dates):

# 将时间、红球、蓝球和日期转换成字典形式。
# 参数 times：包含时间的列表。
# 参数 rb：包含红球的列表。
# 参数 bb：包含蓝球的列表。
# 参数 dates：包含日期的列表。
# 返回值：两个字典，第一个字典将时间作为键，对应的字典项为日期和开奖号码；第二个字典将日期作为键，对应的字典项为时间。

# query_by_times(times, list_datas):

# 根据用户输入的时间查询相关的开奖信息。
# 参数 times：包含时间的列表。
# 参数 list_datas：包含历史开奖数据的字典。
# 无返回值，直接打印查询结果。

# query_by_dates(dates, list_datas):

# 根据用户输入的日期查询相关的开奖信息。
# 参数 dates：包含日期的列表。
# 参数 list_datas：包含历史开奖数据的字典。
# 无返回值，直接打印查询结果。

# check_bingo(times, rb, bb, dates):

# 根据用户选择不同的查询方式，调用上述函数进行相关的查询操作。
# 参数 times：包含时间的列表。
# 参数 rb：包含红球的列表。
# 参数 bb：包含蓝球的列表。
# 参数 dates：包含日期的列表。
# 无返回值，根据用户输入进行相应的操作。

# main():

# 主函数，负责整个程序的流程控制。
# 无参数和返回值，直接调用其他函数完成查询功能。
# 上方if name == 'main':部分：

# 检查该模块是否作为独立程序运行。
# 如果是，则调用 main() 函数开始执行程序逻辑。

# 注意：这段代码使用了第三方库 requests 和 BeautifulSoup。requests 用于发送 HTTP 请求获取网页内容，BeautifulSoup 用于解析 HTML 文档。请确保已经安装了这两个库。


def get_html(url):
    try:
        headers = {'content-type': 'application/json',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
        response = requests.get(url, headers=headers)
        response.encoding = 'UTF-8'
        return response.text
    except Exception as e:
        print('Webpage data not found!')
        print(e)
        return None

def get_data(wps):
    html = get_html(wps)
    if html:
        oc = bs(html, "html5lib")
        t1 = oc.find_all('table')[2]
        t2 = t1.find_all('tr')
        t2 = t2[2:]
        return t2
    else:
        return []

def get_values(datas):
    times, rb, bb, dates = [], [], [], []
    for ta in datas:
        tb = ta.find_all('td')
        times.append(tb[0].text)
        tt = (tb[1].text, tb[2].text, tb[3].text, tb[4].text, tb[5].text, tb[6].text)
        rb.append(tt)
        bb.append(tb[7].text)
        dates.append(tb[15].text)
    return times, rb, bb, dates

def list_dic(times, rb, bb, dates):
    prb = list(zip(rb, bb))
    dic1 = dict(zip(dates, prb))
    dic2 = dict(zip(times, dic1.items()))
    dic3 = dict(zip(dates, times))
    return dic2, dic3

def query_by_times(times, list_datas):
    fv2 = input('Please input the Times:')
    ld = list_datas[fv2]
  
    print('Times is:', fv2, 'Date is:', ld[0])
    print('-------------------------------------------')
    bl = []
    for isa in ld[1][0]:
        bl.append(isa)
    print('Bingo is:', ' - '.join(bl), '/', ld[1][1])
    bl.clear()

def query_by_dates(dates, list_datas):
    fv2 = input('Please type the Date(format is YYYY-MM-DD): ')
    ld = list_datas[fv2]

    print('Times is:', ld, 'Date is:', fv2)
    print('-------------------------------------------')
    bl = []
    for isa in dates[ld][1][0]:
        bl.append(isa)
    print('Bingo is:', ' - '.join(bl), '/', dates[ld][1][1])
    bl.clear()

def check_bingo(times, rb, bb, dates):
    def calculate_prize(matched_red_balls, matched_blue_ball):
        if len(matched_red_balls) == 6 and matched_blue_ball:
            return "一等奖"
        elif len(matched_red_balls) == 6:
            return "二等奖"
        elif len(matched_red_balls) == 5 and matched_blue_ball:
            return "三等奖"
        elif len(matched_red_balls) == 5 or (len(matched_red_balls) == 4 and matched_blue_ball):
            return "四等奖"
        elif len(matched_red_balls) == 4 or (len(matched_red_balls) == 3 and matched_blue_ball):
            return "五等奖"
        elif matched_blue_ball:
            return "六等奖"
        else:
            return "Sorry"

    print('1.Times\n2.Dates\n3.Reverse Query\n4.Quit')
    user_input_1 = input("Please type the Number: ")
    
    if user_input_1 == '1':
        user_input_2 = input("Please Enter the Times: ")
        list_datas = list_dic(times, rb, bb, dates)[0]
        list_datas2 = list_datas[user_input_2]
        
        user_red_list = [ball for ball in input("Input your Red Ball with Space: ").split()]
        user_blue = input("Input your Blue Ball: ")
        
        blank_temp_list = []
        
        for source_red_data in list_datas2[1][0]:
            blank_temp_list.append(source_red_data)
        
        
        matched_red_balls = [ball for ball in user_red_list if ball in blank_temp_list]
        matched_blue_ball = user_blue == list_datas2[1][1]
        
        prize = calculate_prize(matched_red_balls, matched_blue_ball)
        
        print(prize)
        print("中奖号码是：", " - ".join(blank_temp_list), "/", list_datas2[1][1])
        blank_temp_list.clear()
        
    elif user_input_1 == '2':
        user_input_2 = input('Please type the Date(format is YYYY-MM-DD):')
        list_datas = list_dic(times, rb, bb, dates)[1]
        list_datas0 = list_dic(times, rb, bb, dates)[0]
        list_datas2 = list_datas[user_input_2]
        
        user_red_list = [ball for ball in input("Input your Red Ball with Space: ").split()]
        user_blue = input("Input your Blue Ball: ")
        
        blank_temp_list = []
        
        for source_red_data in list_datas0[list_datas2][1][0]:
            blank_temp_list.append(source_red_data)
        
        
        matched_red_balls = [ball for ball in user_red_list if ball in blank_temp_list]
        matched_blue_ball = user_blue == list_datas0[list_datas2][1][1]
        
        prize = calculate_prize(matched_red_balls, matched_blue_ball)
        
        print(prize)
        print("中奖号码是：", " - ".join(blank_temp_list), "/", list_datas0[list_datas2][1][1])
        blank_temp_list.clear()

def main():
    url = 'https://datachart.500.com/ssq/history/newinc/history.php?start=00001'
    datas = get_data(url)
    
    if len(datas) > 0:
        times, rb, bb, dates = get_values(datas)
        list_datas = list_dic(times, rb, bb, dates)
        
        while True:
            print('1.Times\n2.Dates\n3.Check\n4.Quit')
            fv1 = input('Please type the Number: ')
            
            if fv1 == '1':
                query_by_times(times, list_datas[0])
            elif fv1 == '2':
                query_by_dates(list_datas[0], list_datas[1])
            elif fv1 == '3':
                check_bingo(times, rb, bb, dates)
            elif fv1 == '4':
                print('Time to say Good-Bye!')
                break
            else:
                print('Error type!')
    else:
        print('No data found!')

if __name__ == '__main__':
    main()
