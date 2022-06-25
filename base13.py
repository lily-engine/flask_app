# セット（同じ値を持つことがない）

set_a = {'a', 'b', 'c', 'd', 'a', 12} # 型が違っても入れられる # セットにリスト型を入れることはできない
print(set_a) # aは1つだけ入る
print('e' in set_a) # False
print('a' in set_a) # True
print('a' not in set_a) # False

print(len(set_a)) # 長さを求める→5


# add, remove, discard, pop, clear

set_a.add('A')
print(set_a)

set_a.remove('a') # 存在しない要素を指定するとKeyErrorになる
print(set_a)

set_a.discard(12) # 存在しない要素を指定してもエラーにはならない
print(set_a)

val = set_a.pop # setから任意の要素が取り出される
print(val, set_a)

set_a.clear()
print(set_a)