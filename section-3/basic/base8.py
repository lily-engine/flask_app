# int str 変換
int_num = 12
str_num = str(int_num)
print(str_num)
print(type(str_num))
# print('num= '+int_num) # TypeError
print('num= '+str(int_num)) # num= 12 # 文字列の連結
float_num = -20.5
str_float = str(float_num)
print(str_float)
print(type(str_float))

# str => int, float
msg = '12'
int_msg = int(msg)
float_msg = float(msg)
print(int_msg)
print(type(int_msg))
print(float_msg)
print(type(float_msg))