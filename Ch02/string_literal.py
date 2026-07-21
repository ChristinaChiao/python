#字串片面(長詞)string literal不可片面被修改
word="goal"
word="f"+word[1:]#正確 ---->word[0]="f"(報錯)
print (word)