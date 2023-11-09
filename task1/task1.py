import sys


def show_path(n, m):
    if n < 1:
        return []
    path = [1]
    circular_array = list(range(1, n + 1))
    current_index = 0
    while True:
        current_index = (current_index + m - 1) % n
        if current_index == 0:
            return path
        else:
            path.append(circular_array[current_index])


if len(sys.argv) != 3:
    print("Введите строку, где n и m - положительные целые числа больше 0: "
          "python task1.py <n> <m>")
else:
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        if n <= 0 or m <= 0:
            print("Введите целые положительные числа больше 0")
        else:
            path = show_path(n, m)
            print(''.join(map(str, path)))
    except ValueError:
        print("Ошибка в аргументах")
