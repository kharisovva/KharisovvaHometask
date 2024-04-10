field = [[" "] * 3 for i in range(3)]
def field_show():
    print(f" 0 1 2")
    for i in range(3):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")

def ask():
    while True:
        coordinates = input("Ваш ход:").split()

        if len(coordinates) != 2:
            print("Введите две координаты")
            continue

        x, y = coordinates
        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа")

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Координаты вне поля")
            continue

        if field[x][y] != " ":
            print("Клетка занята")
            continue

        return x, y

def win_check():
    winner = [((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2)),((0,0),(1,0),(2,0)), ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2)), ((0,0), (1,1), (2,2)), ((0,2),(1,1),(2,0))]
    for cord in winner:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False

count = 0
while True:
    count += 1
    field_show()
    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask()
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win_check():
        print("Победа")
        break

    if count == 9:
        print("Ничья")
        break


