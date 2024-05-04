with open('input.txt', 'r') as f1:
    with open('output.txt', 'w') as f2:
        for s in f1:
            if len(s)>20:
                f2.write(s)