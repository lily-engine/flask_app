# 辞書型のメソッド
car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}

tmp_car = {'country': 'Japan', 'prefecture': 'Aichi', 'model': 'カローラ'} # modelをカローラに変更

car.update(tmp_car) # 追加、更新
print(car)

car['city'] = 'Toyota-shi' # 直接追加
car['year'] = 2017 # 直接更新
print(car)

value = car.popitem() # 最後に追加した要素の取り出し→元の辞書型からはcityが消える
print(car)
print(value) # ('city', 'Toyota-shi')

value = car.pop('model') # pop()は、キーを指定して値を取り出し→元の辞書からmodelがなくなる
print(car)
print(value) # カローラ

car.clear() # {}
print(car)

del car # delは、変数を表示する。 # NameError: name 'car' is not defined
print(car)