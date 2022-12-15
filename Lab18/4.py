def getDict(file):
    dct = {}
    symbols = ["!", ".", ",", "\n", "—"]
    prepcon = ["и", "а", "но", "в", "с", "на", "от", "это", "под", "Та", "над", "у", "из", "ну", "для"] # И другие предлоги
    with open(rf"{file}.txt", "r", encoding= "utf-8") as f:
        for line in f.readlines():
            line = line.lower()
            for i in symbols:
                line = line.replace(i, "")
            line = line.split(" ")
            for i in line:
                if i in prepcon and not i in dct: dct[i] = 1
                elif i in prepcon: dct[i] += 1
    return dct

def display(dct, namespace):
    print("'" * 5, namespace, "'" * 5)
    for i in dct.items(): print(f"{i[0]}: {i[1]}")
    print("Всего союзов: ", sum(dct.values()))

dct_1 = getDict("test1")
dct_2 = getDict("test2")

display(dct_1, " File_1 ")
display(dct_2, " File_2 ")
