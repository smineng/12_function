# 2分課題 : 2つの整数の和を返す関数　add を使ってね

def add(a: int, b: int) -> int:
    return a + b

#y = add(a=3, b=4)

#print(y) # ここで7が出力されればOK!!


# 課題2: 2つの整数の差を返す関数を定義してね

def diff(a: int, b: int) -> int:
    return a - b

#y1 = diff(a=4, b=3)

#print(y1)

#subはサブストラクションの略
#先にy1から考えてdef(関数)を作る ※関数の設計、テスト駆動開発
#y1のdiffの真ん中でコントロール+Tを押したら変えれる(Renameする)



if __name__ == '__main__':

    y = add(a=3, b=4)
    print(y)

    y1 = diff(a=4, b=3)
    print(y1)