import decimal
f1, f2=10.0, 3.0

d1= decimal.Decimal(10)
d2= decimal.Decimal('3.0')
print(type(d1))#類別
print(f1/f2)#10.0/3.0

#整數除以浮點數(記憶體小的會轉成大的)自動(隱形)轉換 10/3.0 ---->10.0/3.0
print(d1/d2)#10/3.0
print(decimal.getcontext().prec)#decimal固定位數28

d3= decimal.Decimal('2.345')
d4= decimal.Decimal('6.78')
print(d3+d4)#+,-法：取小數點位數最多的(d3-->3位數，d4-->2位數)
print(d3*d4)#乘法:兩者後的小數點位數相加(3+2=5)
