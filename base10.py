# Dictionary（辞書型）

car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015, 1: 100}

print(car['brand']) # 設定したkeyを[]の中に書く # keyが間違っているとその次の処理が実行できなくなる
print(car.get('brand')) # dict.get('key') # keyが存在しなかった場合はnone

print(car.get(1)) # 文字列の1ではなく数値の1に対応した値を取り出す

print(car.keys())
print(car.values())
print(car.items()) # キーと値の一覧