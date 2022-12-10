from random import randint
m1 = []
m2 = []
def Fill(m1, m2):
    M = int(input('Введите M-'))
    for i in range(M):
        m1.append(randint(1, 5))
        m2.append(randint(-5, 0))
    print(tuple(m1), tuple(m2))
Fill(m1, m2)
m3 = m1 + m2
count = m3.count(0)
print(tuple(m3), count)