# 2進数、8進数、16進数

age = 0b111 # 7
print(age)
age = 0o11 # 9
print(age)
age = 0x11 # 17
print(age)

# 2進数 => 文字列　# 15をそれぞれの進数にすると？
print(bin(15)) # 0b1111 #bin()：2進数
print(oct(15)) # 0o17 #oct()：8進数
print(hex(15)) # 0xf #hex()：16進数