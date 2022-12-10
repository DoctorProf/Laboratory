from random import randint
m = []
m1 = []
m2 = []
M = int(input('Введите M-'))
N = int(input('Введите N-'))
for i in range(M):
    m.append([])
    for j in range(N):
        m[i].append(randint(1,5))
    print(m[i])
print('\n')

for i in range (M):
    colums=0
    for j in range (N):
        colums +=m[j][i]
    m1.append(colums)
print(m1 ,'\n')

for i in range(M-1):
    if m1[i] > m1[i+1]:
        for i in range(M):
            for j in range(N-1):
                m[i][j], m[i][j+1] = m[i][j+1],m[i][j]

for i in m:
    print(i)
print('\n')

for i in range (M):
    colums=0
    for j in range (N):
        colums +=m[j][i]
    m2.append(colums)
print(m2)