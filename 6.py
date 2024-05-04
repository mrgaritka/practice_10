with open('input.txt') as f1:
    mas = []
    for line in f1:
        mas.append(line)
with open('output.txt', 'w') as f2:
    try:
        if len(mas) - 1 == int(mas[0]):
            f2.write('YES')
        else:
            f2.write('NO')
    except ValueError:
        f2.write('ERROR')