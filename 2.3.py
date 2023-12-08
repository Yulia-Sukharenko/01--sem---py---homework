def saddle_point(mass):
    for i, row in enumerate(mass):
        max_in_row = max(row)
        max_index = row.index(max_in_row)
        column = [mass[j][max_index] for j in range(len(mass))]
        if max_in_row == min(column):
            return (i, max_index)
        else: return None


print('введите количество строк и столбцов ')
rows, columns = map(int, input().split())
mass = []
print('Введите элементы массива ')

for i in range(rows):
    row = list(map(int, input().split()))
    mass.append(row)

print(saddle_point(mass))
