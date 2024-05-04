mas = []
with open('input.txt') as f1:
    for line in f1.readlines():
        mas.append(int(line))
with open('output.txt', 'w') as f2:
    try:
        f2.write(str(mas[0]/mas[1]+mas[2]))

    except ValueError:
        f2.write('data error')
    except ZeroDivisionError:
        f2.write('Division by 0')

