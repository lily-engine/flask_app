# リスト

list_a = [1,2,3,4]
list_b = [] # 空のリストを宣言

print(list_a)
print(list_a[-1])

list_a = [1,[1,2,'apple'],3,'banana']
print(list_a[1][2]) # apple
list_a[1][2] = 'lemon' # 中身の書き換え
print(list_a) # [1, [1, 2, 'lemon'], 3, 'banana']

# リストのメソッド

list_a = [1,2,3,4,5]

list_b = list_a[1:4:2] # :3だと0〜2番目 # 3:だと3〜4番目 # 1:4だとインデックス[1]〜[3] # 1:4:2だと、1つ飛ばしでインデックス[1][3]
print(list_b)

# append：要素の追加, extend：リストの拡張, insert：特定の場所に要素を追加, clear：リストのクリア
list_a.append('apple') # 配列の後ろにappleを追加
print(list_a)
