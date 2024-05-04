with open('input.txt', 'r') as f1:
    with open('output.txt', 'w') as f2:
        date = f1.readline()
        if int(date[3:]) % 2 == 0 and int(date[3:]) != 2:
            date = int(date[3:])*31 + int(date[:2])
        elif int(date[3:]) != 2:
            date = int(date[3:]) * 28 + int(date[:2])
        else:
            date = int(date[3:]) * 30 + int(date[:2])

        count = f1.readline()

        for line in range(int(count)):
            number, dateind = f1.readline().split()
            if int(dateind[3:]) % 2 == 0 and int(dateind[3:]) != 2:
                dateind = int(dateind[3:]) * 31 + int(dateind[:2])
            elif int(dateind[3:]) != 2:
                dateind = int(dateind[3:]) * 28 + int(dateind[:2])
            else:
                dateind = int(dateind[3:]) * 30 + int(dateind[:2])
            if date - dateind > 3:
                f2.write(number)
                f2.write('\n')

