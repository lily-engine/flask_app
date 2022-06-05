# 論理型
is_animal = False
if is_animal: # Falseであれば実行されない
    print('動物です')

is_man = False
is_adult = True

# or文 両方がfalseだと処理が実行されない。
if is_man or is_adult:
    print('男か大人です')

# and文
if is_man and is_adult:
    print('成人男性です')