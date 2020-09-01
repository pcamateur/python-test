import requests
from bs4 import BeautifulSoup as bs

url = 'http://www.boc.cn/sourcedb/whpj'
headers1 = {'content-type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
response = requests.get(url, headers=headers1)
response.encoding = 'UTF-8'
response1 = response.text

oc = bs(response1, "html5lib")
t1 = oc.find_all('table')[1]
t2 = t1.find_all('tr')
t2.pop(0)

names = []
curs = []
dates = []

for t3 in t2:
    t4 = t3.find_all('td')
    names.append(t4[0].text)
    curs.append(t4[5].text)
    dates.append(t4[6].text)

dd = dict(zip(names, curs))

names_digit_list = [ndl for ndl in range(len(names))]

dds = dict(zip(names_digit_list, names))
sdd = dict(zip(names, names_digit_list))
# print(dds)
mo = eval(input('请输入金额：'))
print('请根据查询的货币名称，输入相应编号！')

for k,v in dds.items():
    print(str(k) + ":" + v)

nas = eval(input('请输入货币名称编号(人民币输入99)：'))
if nas != 99:
    na = dds[nas]
else:
    na = '99'
if na in names or na == '99':
    if na == '99':
        nes = eval(input('请输入货币名称编号：'))
        ne = dds[nes]
        if ne in names:
            def queryr2(cash1, namo1):
                values_x1 = dd[namo1]
                vx1 = float(values_x1)
                cv1 = vx1 / 100
                val1 = cash1 / cv1
                val = round(val1, 2)
                return val
            print(str(mo) + '人民币兑换成' + ne + '是：', str(queryr2(mo, ne)))
        elif na == ne:
            print('输入的货币名称重复，程序无法执行~')
        else:
            print('您输入的货币未知，请重新确认！')
    else:
        def query2r(cash2, namo2):
            values_x2 = dd[namo2]
            vx2 = float(values_x2)
            cv2 = vx2 / 100
            val2 = cash2 * cv2
            vals = round(val2, 2)
            return vals
        print(str(mo) + na + '兑换成人民币是：', str(query2r(mo, na)))
else:
    print('您输入的货币未知，请重新确认！')
