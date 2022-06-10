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

# countメソッド。ある特定の文字列の中に文字が何個あるか。

msg = 'ABCDEABC'
print(msg.count('ABCDEF')) # 存在しない文字列だと0

# startswith：何で始まるか、endswith：何で終わるか

print(msg.startswith('ABCD')) # msgの文字列がABCDで始まる場合True
print(msg.endswith('C'))

# strip（両端）, rstrip（右）, lstrip（左） # 文字列を削除したい場合に使う

msg = ' ABC '
print(msg)
print(msg.strip()) # デフォルトでスペースが削除される
msg = 'ABCDEFABC'
print(msg.strip('CBA')) # 右端と左端両方のABCを削除 # DEFが残る
print(msg.rstrip('CBA')) # 左端からABCが削除される
print(msg.lstrip('CBA')) # 右端からABCが削除される

# upper（大文字変換）, lower（小文字変換）, swapcase（大文字・小文字入れ替え）, replace（文字変換）, capitalize（最初だけ大文字に変換）

msg = 'abcABC'
msg_u = msg.upper() # 大文字
msg_l = msg.lower() # 小文字
msg_s = msg.swapcase() # 大文字小文字入れ替え ABCabc
print(msg_u)
print(msg_l)
print(msg_s)

msg = 'ABCDEABC'
msg_r = msg.replace('ABC', 'FFF', 1)
print(msg_r) # FFFDEFFF # 1を引数に取ると、一番左のABCだけ変換。

msg = 'hello WOrld'
print(msg.capitalize()) # 最初だけ大文字に、それ以外は小文字に

# 文字列の一部取り出し、format, islower, isupper

msg = 'hello, my name is taro'
print(msg[:6]) # [:5]で5番目の文字まで取り出せるので、helloと表示
print(msg[6:]) # 6番目以降取り出せる
print(msg[1:6]) # index[1]からindex[6-1]まで取り出せる
print(msg[1:10:2]) # 最後に:2を入れると、1つ飛ばしで取り出せる。

print('hello {}'.format('Taro'))
name = 'Jiro'
print(f'hello {name}') # 変数を展開して表示
print(f'{name=}') # デバッグしたいときに便利

msg = 'apple'
print(msg.islower()) # 全て小文字かをTrue/Falseで判定
print(msg.isupper()) # 全て大文字か

# find, index, rfind, rindex
msg = 'ABCDEABC'
print(msg.find('ABC')) # 文字列のインデックスを検索。見つからない場合は-1。左端のABCのみ確認。
print(msg.rfind('ABC')) # 右端のABCを確認。インデックスは左から数えるので5と表示される。
print(msg.find('ABCE')) # 見つからない場合は-1
print(msg.index('ABCE')) # 見つからない場合はエラー
print(msg.rindex('ABC'))