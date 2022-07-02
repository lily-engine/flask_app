#1
num = 10

#2
print(type(num))

#3
num_str = str(num)

#4
num_list = [num_str, '20', '30']

#5
num_list.append('40')

#6
num_tuple = tuple(num_list)

#7
val = input()
num_tuple = num_tuple + (val,)
print(num_tuple)

#8
num_set = {'40', '50', '60'}
print(num_set)

#9
num_tuple = set(num_tuple)
print(num_tuple | num_set)

#10
num_dict = {'num_tuple' : num_str}
print(num_dict)

#11
print(len(num_list))

#12
if not 'MyKey' in num_dict:
    print('Does not exist.')
## より短く書きたい場合は
## print(num_dict.get('Mykey', 'Does not exist.'))
## Mykeyが存在しない場合は第二引数が取り出される。

#13
num_list.extend(['50', '60'])
print(num_list)

#14
number = int(input())
# 以下のように記述すると、50以下だった場合はis_under_50にTrueが格納される。
is_under_50 = int(val) < 50
print('is_under_50 = {}'.format(is_under_50))
# if number < 50:
#     is_under_50 = True
# else:
#     is_under_50 = False
# print(is_under_50)

#15
print(f'num_str = {num_str}')

#16
print(dir(num_dict))