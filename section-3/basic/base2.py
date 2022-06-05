# 変数の応用

animal = 'dog'
print(animal)

# 定数
LEGAL_AGE = 20  # 20と書いているだけだと他の人が見たときに理解しにくい
age = 18

if age < LEGAL_AGE:
    print('未成年')
else:
    print('成人')

# format文
print(f'age = {age}')
print(f'{age=}')
print("age = {}".format(age))