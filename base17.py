# all, any
# どちらもnotが使える

if all((True, 10 < 20, True)):
    print('allの中の処理')

if all((True, 30 < 20, True)): #1つでもFalseだと実行されない
    print('allの中の処理')

if any((False, 10 < 20, True)): #1つでもTrueだと実行される
    print('anyの中の処理')

if not any((False, 10 < 20, True)): #1つでもTrueだと実行されない
    print('anyの中の処理')