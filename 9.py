import os
os.makedirs(r"simple")

with open('input.txt', 'r') as f1:
    with open(r'simple\output2.txt', 'w') as f2:
        k = 1
        for s in f1:
            if k % 2 == 0:
                f2.write(s)
            k+=1
