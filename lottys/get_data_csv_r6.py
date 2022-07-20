import requests
from bs4 import BeautifulSoup as bs
import csv


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


def get_values(datas, times, rb1, rb2, rb3, rb4, rb5, rb6, bb, dates):
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


# def list_dic(times, rb, bb, dates):
#     prb = list(zip(rb, bb))
#     dic1 = dict(zip(dates, prb))
#     dic2 = dict(zip(times, dic1.items()))
#     dic3 = dict(zip(dates, times))
#     return dic2, dic3


def list_dic(times, rb1, rb2, rb3, rb4, rb5, rb6, bb, dates):
    list_a = list()
    for xa in range(len(times)):
        list_a.append({'times':times[xa],'rb1':rb1[xa],'rb2':rb2[xa],'rb3':rb3[xa],'rb4':rb4[xa],'rb5':rb5[xa],'rb6':rb6[xa],'bb':bb[xa],'dates':dates[xa]})
    return list_a



def main():
    url = 'https://datachart.500.com/ssq/history/newinc/history.php?start=00001'
    # get_data(url)
    times, rb1, rb2, rb3, rb4, rb5, rb6, bb, dates, bl = [], [], [], [], [], [], [], [], [], []
    a = get_data(url)
    # get_values(a, times, rb1, rb2, rb3, rb4, rb5, rb6, bb, dates)
    b = get_values(a, times, rb1, rb2, rb3, rb4, rb5, rb6, bb, dates)
   
    ld = list_dic(b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8])
    # print(ld)
    headers = ['times', 'rb1', 'rb2','rb3','rb4','rb5','rb6', 'bb', 'dates']
    with open("d.csv", mode = 'w', encoding = 'utf-8-sig', newline = '') as f:
        writer = csv.DictWriter(f, headers)

        writer.writerows(ld)



if __name__ == '__main__':
    main()
