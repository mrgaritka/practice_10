with open('input.txt', encoding='utf-8') as f1:
    string = f1.read()
print(string)
with open('output.txt', 'w', encoding='utf-8') as f2:
    for i in string:
        if ord(i) > 223:
            j = ord(i) - 32
            f2.write(chr(j))
        else:
            f2.write(i)

