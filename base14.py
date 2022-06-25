# セット
## 和集合：union,|
## 積集合：intersection,&
## 差集合：difference, -
## 対象差：symmetric_difference, ^    どちらか一方に含まれているけれど両方に含まれていない要素

s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

u = s | t # {'d', 'c', 'f', 'a', 'b', 'e'}
# u = s.union(t)

print(u)

u = s & t # s.intersection(t) # {'d', 'c'}
print(u)

u = s - t # s.difference(t) # {'a', 'b'}
print(u)

u = s ^ t  # s.symmetric_difference(t) # {'e', 'f', 'b', 'a'}
print(u)

s |= t # tの要素をsに追加する
print(s)

# issubset（別の集合に含まれているか）, issuperset（別の集合を含んでいるか）, isdisjoint（重複要素はないか）
s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}
u = {'cherry'}

print(s.issubset(t)) # sの要素はtに含まれている #True
print(t.issuperset(s)) # tはsの要素を全て含んでいる #True

print(t.isdisjoint(s)) # 重複要素がひとつでもある場合はFalse
print(t.isdisjoint(u)) # True