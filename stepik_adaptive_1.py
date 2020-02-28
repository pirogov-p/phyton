x = int(input())
tousend = 0
hundert = 0
ten = 0
number = 0

tousend = x // 1000
print ('M' * tousend, end = '')


hundert = (x-tousend*1000)//100
if hundert < 4:
    print ('C' * hundert, end = '')
elif hundert == 4:
    print('CD', end='')
elif hundert > 4 and hundert < 9:
    print ('D', end='')
    print ('C'* ((x-tousend*1000-500)//100), end='')
elif hundert == 9:
    print ('DM', end='')

ten = (x-tousend*1000 - hundert*100)//10
if ten < 4:
    print ('X' * ten, end = '')
elif ten == 4:
    print('XL', end='')
elif ten > 4 and ten < 9:
    print ('L', end='')
    print ('X'* ((x-tousend*1000-100*hundert-50)//10), end='')
elif ten == 9:
    print ('XC', end='')

number = (x-tousend*1000- hundert*100 - ten*10)
if number < 4:
    print ('I' * number, end = '')
elif number == 4:
    print('IV', end='')
elif number > 4 and number < 9:
    print ('V', end='')
    print ('I'* (x-tousend*1000-hundert*100 - ten*10 - 5), end='')
elif number == 9:
    print ('IX', end='')