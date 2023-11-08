def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


circle_file = input("Введите имя файла с координатами окружности: ")
points_file = input("Введите имя файла с координатами точек: ")
results = []

try:
    with open(circle_file, 'r') as f:
        circle_x, circle_y = map(float, f.readline().split())
        radius = float(f.readline())

    with open(points_file, 'r') as f:
        for line in f:
            point_x, point_y = map(float, line.split())
            dist = distance(circle_x, circle_y, point_x, point_y)

            if dist == radius:
                results.append("0 - точка лежит на окружности")
            elif dist < radius:
                results.append("1 - точка внутри")
            else:
                results.append("2 - точка снаружи")

    for result in results:
        print(result + '\n')

except FileNotFoundError:
    print("Один или оба файла не найдены")
