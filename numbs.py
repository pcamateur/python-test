import random
num = random.randint(0, 999)
def rn(n):
    if num < 100:
        if num < 10:
            ns1 = "00" + str(num)
            return ns1
        elif 9 < num < 100:
            ns1 = "0" + str(num)
            return ns1
        else:
            print('Number is Error!')

    elif 99 < num < 1000:
        ns1 = str(num)
        return ns1
    else:
        print('Values is Error!')

ns = rn(num)

inum = str(input('Please input Numbers or type "exit" to finish:'))
n = 0
dic = {}
while inum != "exit" and ns != inum:
    n += 1
    if inum == 'a':
        print(ns)
        break
    elif inum == 'c':
        print(ns)
    elif inum == 'h':
        print(dic)
    elif len(inum) > 3 or len(inum) < 3:
        print("The digit is must = 3!")
    elif inum.isdigit():
        if ns[0] == inum[0]:
            if ns[1] == inum[1]:
                val = 'R2E1' #001
            elif ns[2] == inum[2]:
                val = 'R2E1' #010
            else:
                val = 'R1E2' #011
            print(val)
            dic[n] = list((inum, val))
        else:
            if ns[1] == inum[1]:
                if ns[2] == inum[2]:
                    val = 'R2E1' #100
                else:
                    val = 'R1E2' #101
                print(val)
                dic[n] = list((inum, val))
            else:
                if ns[2] == inum[2]:
                    val = 'R1E2' #110
                else:
                    val = 'R0E3' #111
                print(val)
                dic[n] = list((inum, val))

    else:
        pass
    inum = str(input('Please input a digit,Thanks!If you want quit,please input "exit":'))

print('The Number is:', ns)
print('Game Over!')
