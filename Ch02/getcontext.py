import decimal#匯入decimal(精準度高)模組
d1=decimal.Decimal.from_float(123.4567)#把浮點資料123.4567轉成decimal的資料型別
d2=decimal.Decimal.from_float(34.5678)#把浮點資料34.5678轉成decimal的資料型別

print(d1+d2)#158.0244999999999961914909363(預設是28位有效位數)

print(decimal.getcontext())#取出目前decimal資料型別運算的設定值
print(decimal.getcontext().prec)#印出上敘設定值中prec的值
print(decimal.getcontext().rounding)#印出上敘設定值中rounding的值"奇數進位"
decimal.getcontext().prec=8 #將28位改成8位有效位數(包含整數跟小數)
print(d1+d2)#158.024499(9為基數，進位02450)

