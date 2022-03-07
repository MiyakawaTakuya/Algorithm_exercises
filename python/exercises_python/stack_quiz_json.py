"""
Input {'key1': 'value1', 'key2': [1, 2, 3], 'key3': (1, 2, 3)}  Output True
Input [{'key1': 'value1', 'key2': [1, 2, 3], 'key3': (1, 2, 3)} Output False
"""
#Jsonの括弧のフォーマットを正す
#ロジックを考える力を身につけよ アイデアが浮かぶかが大事

def validate_format(chars: str) -> bool:
    lookup = {'{': '}', '[': ']', '(': ')'}  #連想配列
    stack = []
    for char in chars:
        # if c in lookup.keys():
        if char in lookup:
            stack.append(lookup[char])  #キーに指定してある括弧の左側を読み込んだら
        if char in lookup.values():  # バリューに指定してある括弧の右側を読み込んだら
            if not stack:    #その時点でstackが空だった場合は
                return False
            if char != stack.pop():   #読み込んだ値とpopした値が一致しなかったら
                return False
    if stack:  #なのかしらstackの中に入っていたら(この時点では空であるべき)
        return False
    return True


if __name__ == '__main__':
    import json
    d = {'key1': 'value1', 'key2': [1, 2, 3], 'key3': (1, 2, 3)}
    s = json.dumps(d)
    print(s)
    print(validate_format(s))
    s += '('
    print(s)
    print(validate_format(s))
