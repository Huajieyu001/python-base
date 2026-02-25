

for i in range(1, 10):
    count = i
    for j in range (1, i + 1):
        print(f'{j}*{i}={i*j}', end='\t')
    print()