x=5
y=x
print(id(x), id(y))#顯示記憶體位置
x=3+y
print(id(x), id(y))#x變成3+y所以會換位置，y的位置不變
print(x, y)

a,b = 2,3
print(id(a), id(b))
a,b=b,a#a跟b數值對調，所以位置也對調
print(id(a), id(b))
print(a, b)
