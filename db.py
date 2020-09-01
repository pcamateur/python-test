import requests
from bs4 import BeautifulSoup as bs

url = 'https://datachart.500.com/ssq/history/newinc/history.php?start=00001'
headers1 = {'content-type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
response = requests.get(url, headers=headers1)
response.encoding = 'UTF-8'
response1 = response.text

oc = bs(response1, "html5lib")
t1 = oc.find_all('table')[2]
t2 = t1.find_all('tr')
t2.pop(0)
t2.pop(0)

times, rb, bb, dates = [], [], [], []

info = []

for t3 in t2:
    t4 = t3.find_all('td')
    times.append(t4[0].text)
    tt = (t4[1].text, t4[2].text, t4[3].text, t4[4].text, t4[5].text, t4[6].text)
    rb.append(tt)
    bb.append(t4[7].text)
    dates.append(t4[15].text)

prb = list(zip(rb, bb))
dic1 = dict(zip(dates, prb))
dic2 = dict(zip(times, dic1.items()))

print('1.Times\n2.Dates')
fv1 = input('Please type the Number:')
if fv1 == '1':
    fv2 = input('Please input the Times:')
    print(dic2[fv2])
    print('Times is:', fv2,'Date is:', dic2[fv2][0])
    print('-------------------------------------------')
    bl1 = []
    for isa1 in dic2[fv2][1][0]:
        bl1.append(isa1)
    print('Bingo is:', ' - '.join(bl1), '/', dic2[fv2][1][1])
    # print('Bingo is:', dic2[fv2][1][0][0], '-', dic2[fv2][1][0][1], '-', dic2[fv2][1][0][2], '-', dic2[fv2][1][0][3],
    #       '-', dic2[fv2][1][0][4], '-', dic2[fv2][1][0][5], '/', dic2[fv2][1][1])
elif fv1 == '2':
    dic3 = dict(zip(dates, times))
    fv3 = input("Please type the Date(format is YYYY-MM-DD):")
    print('Times is:', dic2[dic3[fv3]][0], 'Date is:', fv3)
    print('-------------------------------------------')
    bl = []
    for isa in dic2[dic3[fv3]][1][0]:
        bl.append(isa)
    print('Bingo is:', ' - '.join(bl), '/', dic2[dic3[fv3]][1][1])
else:
    print('Error type!Time to say Goodbye~')