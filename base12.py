# タプル # 値を変更できない

fruit = ('apple', 'banana', 'lemon')

print(fruit)
print(type(fruit))
print(fruit[0])
# fruit[1] = 'grape' # 値を変更できないのでエラーになる
fruit = fruit + ('grape',)
print(fruit)

list_fruit = ['apple', 'banana']
fruit = tuple(list_fruit)
print(fruit)  # ('apple', 'banana')
print(fruit.count('apple')) # 文字列にappleがいくつあるかを数える
print(fruit.index('banana')) # bananaの位置を返す

pos = (135, 35)

countries = {pos: 'Japan'} # (135, 35)に対応するのはJapanです # タプルの有効活用方法
print(countries.get((135,35))) # Japan