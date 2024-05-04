with open('input.txt', 'r+') as f1:
    with open('output.txt', 'w') as f2:
        for s in f1:
            if s[0] == 'a' or s[0] == 'A':
                f2.write(s)