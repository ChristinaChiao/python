#字串切片string slicing
flavor="fig pie"
print(flavor[0:3])#0開頭
print(flavor[3:7])#7超過就把後面的輸出
print(flavor[3:])
print(flavor[:])
print(flavor[:14])#14超過就把後面的輸出
print(flavor[13:15])#13跟15都超過輸出0

print(flavor[-7:-4])
print(flavor[-7:0])#-7=0---> 等於[0:0]
print(flavor[-7:])#沒有設定結束
print(flavor[-3:])#沒有設定結束