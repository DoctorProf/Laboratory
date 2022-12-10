from random import randint
m = []
max = 0
M = int(input('Введите M-'))
N = int(input('Введите N-'))
for i in range(M):
    m.append([])
    for j in range(N):
        m[i].append(randint(-10,10))
    print(m[i])
    
for i in range(M):
    if i % 4 == 3:
       print(f'Минимальный{i + 1}={min(m[i])}')
