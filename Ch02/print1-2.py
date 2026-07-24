print('Python', 3.8)
print('Taipei', 'Taichung', 'Tainan', sep=', ')
print('Kaohsiung', 'Pingtung', sep='\t')
print('Price List: ', end='')#預設是換行，改空白
money= 30
print('陽春麵', money, '元')

print('%c%s先生'% ('張', '無忌'))#2->2
wt, price = 3, 20.5
print('%s%d斤, 共%f元'% ('香蕉', wt, wt*price))