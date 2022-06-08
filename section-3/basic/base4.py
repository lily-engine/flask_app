# 数値型

value = 1
# print(value)
# value = -2
# print(value)

# value = value + 4 #2
# print(value)
# print(value * 4) #8
# print(value / 3) #0.66666
# value = 10
# print(value // 3) #3
# print(value % 3) #1

value += 3 # value = value + 3
# print(value)
# print(value ** 3)

# 浮動小数点数
height = 175.5 # floatとして宣言される
print(height)
print(type(height))
print(height + 10) # 175.5 + 10.0

value = 8 # 1000 => 0010 　2桁右にずらす
print(value >> 2) # 0010　は10進数に直すと2
print(value << 3) # 1000 => 1000000 10進数に直すと64

print(12 & 21) # 01100 and 10101 = 00100 => 4
print(12 | 21) # 01100 or 10101 = 11101 => 29

value = 12
value &= 21 # value = value & 21
print(value)