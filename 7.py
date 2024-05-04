with open('input.txt') as f1:
    with open('output.txt', 'w') as f2:
        for s in f1:
            if int(s) != 100:
                f2.write(s)