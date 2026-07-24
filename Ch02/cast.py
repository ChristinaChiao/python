#cast強制轉換
i1 = 10
f1 = float(i1)#10.0
print(i1, f1, type(f1))

f2 = 1234.5678
i2 = int(f2)
print(f2, i2, type(i2))#無條件捨去小數

i3 = round(f2)
print(f2, i3, type(i3))#f2四捨五入

s=str(i2)
print(s, type(s))#i2=1234

b=bool(f1)
print(b, type(b))#布林：有東西就是true