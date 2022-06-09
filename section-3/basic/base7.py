# 文字列型

fruit = 'apple'
print(fruit)
print(type(fruit))

print(fruit * 10) #文字列を掛け算できる # 文字列+数列はエラーになる
fruit_10 = fruit * 10
print(fruit_10)

new_fruit = fruit + 'banana' # 文字列どうしは+で連結できる
print(new_fruit) 

fruits = """apple
banana
grape
""" # 改行も含めて表示できる
print(fruits)

fruit = 'banana'
print(fruit[2]) # nが表示される
print(fruit[-1]) # マイナスの場合、後ろから数えるのでaが表示される

# encode, decode => bytes[] バイナリの型に文字列を変換する
# バイト型とは：8ビットの範囲で整数を表現するもの。-128〜127まで。
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8') # バイト型から文字列型に
print(str_fruit)
print(type(str_fruit))