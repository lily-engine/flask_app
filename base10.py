# Dictionary（辞書型）

car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015, 1: 100}

print(car['brand']) # 設定したkeyを[]の中に書く # keyが間違っているとその次の処理が実行できなくなる
print(car.get('brand')) # dict.get('key') # keyが存在しなかった場合はnone

print(car.get(1)) # 文字列の1ではなく数値の1に対応した値を取り出す

print(car.keys()) # キーの一覧
print(car.values()) # 値の一覧
print(car.items()) # キーと値の一覧

for k, v in car.items(): # キーがk、値がvにそれぞれ格納される
    print('key = {}, value = {}'.format(k,v))

if 'brand' in car:
    print('carのブランドは{}'.format(car['brand'])) # brandというキーが存在する場合だけ、処理を実行できる

