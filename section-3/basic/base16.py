#if and or not

# msg = 'yellow'
# if msg == 'blue':
#     print('すすめ')
# elif msg == 'red':
#     print('とまれ')
# else:
#     print('それ以外の処理')

age = 70
if age < 20:
    print('20未満')
elif age <= 40: #20以上で実行される
    print('20以上、40以下です')
elif age >= 60:
    print('60以上です')
else:
    print('それ以外の年齢')

# and or not
gender = 'woman'
age = 10
if gender == 'man' or age < 20:
    print('未成年もしくは男性です')

if not gender == 'man': #条件式の否定　#if not != gender でも同じ（!= は≠）
    print('男ではない')