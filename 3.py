with open('input.txt', 'r') as f1:
    k = ''
    for s in f1:
        k += s[0]
with open('output.txt', 'w') as f2:
    f2.write(k)
            