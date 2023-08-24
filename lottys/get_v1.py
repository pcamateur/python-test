import requests
from bs4 import BeautifulSoup as bs
import csv


def get_html(url):
    try:
        headers = {'content-type': 'application/json',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
        response = requests.get(url, headers=headers)
        response.encoding = 'UTF-8'
        return response.text

    except:
        print('Webpage data not found!')


def get_data(url):
    html = get_html(url)
    oc = bs(html, "html5lib")
    t1 = oc.find_all('table')[2]
    t2 = t1.find_all('tr')
    t2.pop(0)
    t2.pop(0)
    return t2


def get_values(datas):
    times, rb1, rb2, rb3, rb4, rb5, rb6, bb, dates = [], [], [], [], [], [], [], [], []
    for ta in datas:
        tb = ta.find_all('td')
        times.append(tb[0].text)
        tt = (tb[1].text, tb[2].text, tb[3].text, tb[4].text, tb[5].text, tb[6].text)
        rb1.append(tt[0])
        rb2.append(tt[1])
        rb3.append(tt[2])
        rb4.append(tt[3])
        rb5.append(tt[4])
        rb6.append(tt[5])
        bb.append(tb[7].text)
        dates.append(tb[15].text)
    return times, rb1, rb2, rb3, rb4, rb5, rb6, bb, dates


# def list_dic(times, rb1, rb2, rb3, rb4, rb5, rb6, bb, dates):
#     list_a = []
#     for xa in range(len(times)):
#         list_a.append({'times': times[xa], 'rb1': rb1[xa], 'rb2': rb2[xa], 'rb3': rb3[xa], 'rb4': rb4[xa], 'rb5': rb5[xa],
#                        'rb6': rb6[xa], 'bb': bb[xa], 'dates': dates[xa]})
#     return list_a

# def list_dic(times, rb1, rb2, rb3, rb4, rb5, rb6, bb, dates):
#     headers = ['times', 'rb1', 'rb2', 'rb3', 'rb4', 'rb5', 'rb6', 'bb', 'dates']
#     list_a = []
#     for xa in range(len(times)):
#         list_a.append({headers[0]: times[xa], headers[1]: rb1[xa], headers[2]: rb2[xa], headers[3]: rb3[xa], 
#                        headers[4]: rb4[xa], headers[5]: rb5[xa], headers[6]: rb6[xa], headers[7]: bb[xa], headers[8]: dates[xa]})
#     return list_a

def list_dic(times, rb1, rb2, rb3, rb4, rb5, rb6, bb, dates):
    headers = ['times', 'rb1', 'rb2', 'rb3', 'rb4', 'rb5', 'rb6', 'bb', 'dates']
    list_a = []
    for xa in range(len(times)):
        list_a.append({headers[0]: times[xa], headers[1]: rb1[xa], headers[2]: rb2[xa], headers[3]: rb3[xa], 
                       headers[4]: rb4[xa], headers[5]: rb5[xa], headers[6]: rb6[xa], headers[7]: bb[xa], headers[8]: dates[xa]})
    return list_a




def check_lottery_prize(user_red_balls, user_blue_ball, lottery_data):
    for data in lottery_data:
        matched_red_balls = [ball for ball in user_red_balls if ball in [data['rb1'], data['rb2'], data['rb3'],
                                                                         data['rb4'], data['rb5'], data['rb6']]]
        matched_blue_ball = user_blue_ball == data['bb']

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

    return "未中奖"


def main():
    url = 'https://datachart.500.com/ssq/history/newinc/history.php?start=00001'
    lottery_data = get_data(url)
    lottery_values = get_values(lottery_data)
    
    # red_balls = [int(ball) for ball in input("请输入红球号码（用空格分隔）：").split()]
    # blue_ball = int(input("请输入蓝球号码："))
    
    red_balls = [int(ball) for ball in input("请输入红球号码（用空格分隔）：").split()]
    blue_ball = int(input("请输入蓝球号码："))

    
    prize = check_lottery_prize(red_balls, blue_ball, lottery_values)
    print("您的彩票中奖情况：", prize)

    headers = ['times', 'rb1', 'rb2', 'rb3', 'rb4', 'rb5', 'rb6', 'bb', 'dates']
    with open("d.csv", mode='w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, headers)
        writer.writerows(list_dic(*lottery_values))


if __name__ == '__main__':
    main()
