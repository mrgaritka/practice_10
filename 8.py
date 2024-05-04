with open('input.txt', 'r') as f:
    mas = []
    for s in f:
        mas.append(s)

with open('output.txt', 'w+') as f1:
    cnt = 0
    control = 0
    for m in range(12):
        if m % 2 == 0 and m != 2:
            for d in range(31):
                cnt += int(mas[control])
                control += 1
            f1.write(str(cnt/31))
            f1.write('\n')
            cnt = 0
        elif m == 2:
            for d in range(28):
                cnt += int(mas[control])
                control += 1
            f1.write(str(cnt/30))
            f1.write('\n')
            cnt = 0
        else:
            for d in range(30):
                cnt += int(mas[control])
                control += 1
            f1.write(str(cnt/30))
            f1.write('\n')
            cnt = 0
print(control)