# リスト

list_a = [1,2,3,4]
list_b = [] # 空のリストを宣言

print(list_a)
print(list_a[-1])

list_a = [1,[1,2,'apple'],3,'banana']
print(list_a[1][2]) # apple
list_a[1][2] = 'lemon' # 中身の書き換え
print(list_a) # [1, [1, 2, 'lemon'], 3, 'banana']