#if文

class ClassA():
    def __init__(self,a):
        self.a = a
    
    # bool(var)で以下のメソッドが呼ばれる。
    def __bool__(self):
        if self.a == 'a':
            return True
        return False

var = ClassA('a')
print('boolの計算結果:{}'.format(bool(var))) #bool関数でvarという変数を中に入れた場合の計算結果がTrueの場合は、if文のなかの処理が実行される

if var:
    print('if文の中の処理')