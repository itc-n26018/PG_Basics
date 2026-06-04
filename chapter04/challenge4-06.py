def squared(x):
    """ 
    渡された数値の2乗を計算する。
    引数: x (int)
    戻り値: xを2乗した値。
    """
    return x ** 2


def print_Powerful(Powerful)
    """ 
    渡された値をコンソールに出力する。
    引数: Powerful, データ型: 文字列
    """
    print(Powerful)


def add_char(a, b, c, x=80, y=90):
    """
    指定された数式に基づいて計算を行う。
    必須引数: a (int)
    必須引数: b (int)
    必須引数: c (int)
    オプション引数: x (int), デフォルト値: 80 
    オプション引数: y (int), デフォルト値: 90
    戻り値: 計算した結果の値。
    """
    return a + b - c * (x + y)


def devided(x):
    """
    引数の数値を2で割った整数値を返す。
    引数: x (割られる数)
    戻り値: (int) 2で割った商（小数点以下切り捨て）
    """
    return x // 2

def multiply(x):
    """
    引数の数値を4倍した値を返す。
    引数: x (かける数)
    戻り値: (int) 4倍された値
    """
    return x * 4


def to_float(string):
    """
    文字列を浮動小数点数に変換する。
    引数: string (変換したい数値形式の文字列)
    戻り値: 
        float: 変換に成功した場合
        None: 変換に失敗した場合
    例外: ValueError (失敗したときにエラーメッセージが出力される)
    """
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string")    
