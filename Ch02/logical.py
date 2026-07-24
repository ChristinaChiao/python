#邏輯運算子
print((1<2) and ('A' == 'a'))
#ascii table 中A=65，a=97  https://www.ascii-code.com/

print((-1<0) or (-1 > 100))#其一正確，顯示True
print(not ('A' != 'a'))#最裡面的()先執行，裡面是1，外面否定->0
print(not 2)#2不是0->1，外面否定->0

#當我們做and 跟or，為真(有東西)才有結果輸出
print(2 and 3)#前面為真，後面也為真，後面的結果
print(2 and 0)#前面為真，後面也為否，結果就是否
print(0 and 3)#前面為否，即使後面為真，結果就是否
print(2 or 3)#前面為真，前面的結果
print(3 or 2)

print('a' or 'b')
print(''or 'b')