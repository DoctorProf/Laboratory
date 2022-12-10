from random import randint
m = []
max = 0
M = int(input('Введите M-'))
N = int(input('Введите N-'))
for i in range(M):
    m.append([])
    for j in range(N):
        m[i].append(randint(1,5))
    print(m[i])

max = {
    "value": None,
    "i": -1,
    "j": -1,
    "print":lambda:print("Масимальное значение:", max["value"])
}

for i in range(M):
    for j in range(N):
        if max["value"] == None or max["value"] < m[i][j]:
            max["value"] = m[i][j]
            max["i"]=i
            max["j"]=j

for i in range(M):
    m[i].pop(max["j"])

m.pop(max["i"])
2
for i in range(len(m)):
    print(m[i])

max["print"]()