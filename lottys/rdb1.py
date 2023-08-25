import requests
from bs4 import BeautifulSoup as bs


def get_html(url):
    try:
        headers1 = {'content-type': 'application/json',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) '
                                  'Gecko/20100101 Firefox/78.0'}
        response = requests.get(url, headers=headers1)
        response.encoding = 'UTF-8'
        response1 = response.text
        return response1

    except:
        print('Webpage data not found!')


def get_data(wps):
    html = get_html(wps)
    oc = bs(html, "html5lib")
    t1 = oc.find_all('table')[2]
    t2 = t1.find_all('tr')
    t2.pop(0)
    t2.pop(0)
    return t2


def get_values(datas, times, rb, bb, dates):
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


def query_by_times_and_dates(bl, times, rb, bb, dates):
    print('1.Times\n2.Dates\n3.Check\n4.Quit')
    fv1 = input('Please type the Number: ')
    if fv1 == '1':
        fv2 = input('Please input the Times:')
        ld = list_dic(times, rb, bb, dates)[0]
        ld2 = ld[fv2]
        print('Times is:', fv2, 'Date is:', ld2[0])
        print('-------------------------------------------')
        for isa in ld2[1][0]:
            bl.append(isa)
        print('Bingo is:', ' - '.join(bl), '/', ld2[1][1])
        bl.clear()
    elif fv1 == '2':
        fv2 = input('Please type the Date(format is YYYY-MM-DD): ')
        ld = list_dic(times, rb, bb, dates)[1]
        ld0 = list_dic(times, rb, bb, dates)[0]
        ld2 = ld[fv2]
        print('Times is:', ld2, 'Date is:', fv2)
        print('-------------------------------------------')
        for isa in ld0[ld2][1][0]:
            bl.append(isa)
        print('Bingo is:', ' - '.join(bl), '/', ld0[ld2][1][1])
        bl.clear()
    elif fv1 == '3':
        url = 'https://datachart.500.com/ssq/history/newinc/history.php?start=00001'
        get_data(url)
        times, rb, bb, dates, bl = [], [], [], [], []
        a1 = get_data(url)
        get_values(a1, times, rb, bb, dates)
        b1 = get_values(a1, times, rb, bb, dates)
        # list_dic(b[0], b[1], b[2], b[3])
        check_bingo(b1[0], b1[1], b1[2], b1[3])
    elif fv1 == '4':
        print('Time to say Good-Bye!')
        exit()
    else:
        print('Error type!')
        
        
def check_bingo(times, rb, bb, dates):
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
        
        if len(matched_red_balls) == 6 and matched_blue_ball:
            print("一等奖")
        elif len(matched_red_balls) == 6:
            print("二等奖")
        elif len(matched_red_balls) == 5 and matched_blue_ball:
            print("三等奖")
        elif len(matched_red_balls) == 5 or (len(matched_red_balls) == 4 and matched_blue_ball):
            print("四等奖")
        elif len(matched_red_balls) == 4 or (len(matched_red_balls) == 3 and matched_blue_ball):
            print("五等奖")
        elif matched_blue_ball:
            print("六等奖")
        else:
            print("Sorry")
            
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
        
        if len(matched_red_balls) == 6 and matched_blue_ball:
            print("一等奖")
        elif len(matched_red_balls) == 6:
            print("二等奖")
        elif len(matched_red_balls) == 5 and matched_blue_ball:
            print("三等奖")
        elif len(matched_red_balls) == 5 or (len(matched_red_balls) == 4 and matched_blue_ball):
            print("四等奖")
        elif len(matched_red_balls) == 4 or (len(matched_red_balls) == 3 and matched_blue_ball):
            print("五等奖")
        elif matched_blue_ball:
            print("六等奖")
        else:
            print("Sorry")
            
        print("中奖号码是：", " - ".join(blank_temp_list), "/", list_datas0[list_datas2][1][1])
        blank_temp_list.clear()
            
            
            
        
        

def main():
    url = 'https://datachart.500.com/ssq/history/newinc/history.php?start=00001'
    get_data(url)
    times, rb, bb, dates, bl = [], [], [], [], []
    a = get_data(url)
    get_values(a, times, rb, bb, dates)
    b = get_values(a, times, rb, bb, dates)
    list_dic(b[0], b[1], b[2], b[3])
    
    loop_values = 1
    while loop_values != "quit":
        query_by_times_and_dates(bl, b[0], b[1], b[2], b[3])
        loop_values = input('Exit please type "quit",Enter to Continue!:')
        check_bingo(b[0], b[1], b[2], b[3])
    print('See your Next time!')


if __name__ == '__main__':
    main()
