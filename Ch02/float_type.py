#浮點
f, i =1.2345, 12345
print(type(f))#浮點float
f2=float(i)#轉浮點數就有小數點
print(f2)#印出f2---->12345.0
print(float.is_integer(f))#物件float.方法(或是物件.屬性) 檢查f=1.2345是否為整數

#來檢查一個浮點數數值是否等於整數(即小數點後是否全為0)
print(float.is_integer(f2))#True

#資料型態是否為整數
print(isinstance(f2, int))#False
print(round(f,2))#f=1.2345取兩個小數1.23
print(round(f))#f=1.2345四捨五入1(2<5)