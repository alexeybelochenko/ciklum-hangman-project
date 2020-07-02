default = 'транзистор'
template = "_"*len(default)


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def chars_replace(char, indexs):
    temp = list(template)
    for i in indexs:
        temp[i] = char
    
    string = "".join(temp)
    return string

is_game = True
life = 5
while is_game and life != 0 and template != default:
    char = str(input())
    indexs = find(default, char)
    if len(indexs) != 0:
        for i in indexs:
            template = chars_replace(char, indexs)
        print(template)
    else:
        life -= 1
        print(f'Буквы нет и у вас осталось {life} жизней')

print('Вы допустили предельное количество ошибок')