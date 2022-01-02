def show_field(f):    # функция отображение игрового поля
    num ='  0 1 2'
    print(num)
    for row, i in zip(f, num.split()):
        print(f"{i} {' '.join(str(j) for j in row)}")

def users_input(f, user):    # функция опроса игрока
    while True:
        place = input(f"Ходит {user} .Введите координаты:").split()
        if len(place) != 2:                                     # проверка количества введенных значений
            print('Введите две координаты')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):      # проверка введенных значений на возможность преобразования в число
            print('Введите числа')
            continue
        x, y = map(int, place)
        if not (x >= 0 and x < 3 and y >= 0 and  y < 3):        # проверка введенных значений на выход из диапазона
            print('Вышли из диапазона')
            continue
        if f[x][y] != '-':                  # проверка заполненности клетки
            print('Клетка занята')
            continue
        break
    return x, y


def win_position(f, user):    # функция проверки выигрышных позиций
    f_list=[]
    for l in f:
        f_list += l
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p))) == 3:
            return True
    return False


def start(field):           # функция повторения хода игроками

    count = 0
    while True:
        show_field(field)
        if count % 2 == 0:              # проверка хода крестика или нолика
            user = 'x'
        else:
            user = 'o'
        if count < 9:                   # проверка на возможность дальнейшего хода
            x, y = users_input(field, user)
            field[x][y] = user
        elif count == 9:                # проверка на достижение максимального количество ходов
            print('Ничья')
            break
        if win_position(field, user):   # проверка на выигрышную комбинацию
            print(f"Выиграл {user}")
            show_field(field)
            break
        count += 1


field = [['-'] * 3 for _ in range(3)]    # создаем игровое поле

start(field)
