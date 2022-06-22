# リスト

list_a = [1,2,3,4]
list_b = [] # 空のリストを宣言

print(list_a)
print(list_a[-1])

list_a = [1,[1,2,'apple'],3,'banana']
print(list_a[1][2]) # apple
list_a[1][2] = 'lemon' # 中身の書き換え
print(list_a) # [1, [1, 2, 'lemon'], 3, 'banana']

# リストのメソッド  ## endは含まれずにend未満になる。

list_a = [1,2,3,4,5]

list_b = list_a[1:4:2] # :3だと0〜2番目 # 3:だと3〜4番目 # 1:4だとインデックス[1]〜[3] # 1:4:2だと、1つ飛ばしでインデックス[1][3]
print(list_b)

# append：要素の追加, extend：リストの拡張, insert：特定の場所に要素を追加, clear：リストのクリア
list_a.append('apple') # 配列の後ろにappleを追加
print(list_a)
# list_a.append(['banana', 'melon']) # リストの中にリストが入る。
# print(list_a)
list_a.extend(['banana', 'melon']) # リストの中に要素を入れる＝リストの拡張
print(list_a)
list_a.insert(1, 'grape') # index[1]に要素を追加
print(list_a)
# list_a.clear() # リストの中身を削除
# print(list_a)

# remove：要素の削除, pop：要素の取り出し, count：要素のカウント, index：要素の検索
list_a = [0,1,1,2,2,3,3,3,4]
list_a.remove(3) # 一番左から数えて最初に登場する3を削除する
print(list_a)
value = list_a.pop() # popで弾かれた要素を格納。
print(list_a, value) # popによって、最後に追加された要素を取り出せる。
print(list_a.count(0))
print(list_a.index(1)) # 1が最初に登場するインデックスを表示（ここでは1）

# copy
print(list_a)
# list_b = list_a
# list_b[0] = 'AAA' # list_aと_bの格納先が一緒なので、bの値を書き換えるとaの値も書き換わる
# print(list_a) 
list_b = list_a.copy()
list_b[0] = 'AAA' # copyを使うと、aは書き換わらない
print(list_a)

# sort reverse
list_a = ['banana', 'apple', 'lemon', 'grape']
print(list_a)
# list_a.sort()
# print(list_a)
list_a = sorted(list_a)
print(list_a) # 昇順
list_a.reverse()
print(list_a) # 降順