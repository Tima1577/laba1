file = open("1.txt")
q = ""
qer = list(file)
for i in qer:
    q += i.replace("\n", "")
print("Количество символов с пробелами:", len(q))
bezprob = len(q.replace(" ", "").replace(",", "").replace(":", ""))
print("Количество символов без пробелов и знаков припенания:", bezprob)
dn = []
name = ''
des = ''
f = False
abil = []
for i in qer:
    if f:
        if "]" not in i:
            f = i.replace("\n", "").replace(",", "").replace("      ", "")
            f = f.replace('"', "")
            abil.append(f)
        else:
            f = False
    if "name" in i:
        buf = ""
        for i1 in i:
            if '    "name": "' not in buf:
                buf += i1
            else:
                if i1 != '"':
                    name += i1
                else:
                    break
    if '"description"' in i:
        buf = ""
        for i1 in i:
            if '    "description": "' not in buf:
                buf += i1
            else:
                if i1 != '"':
                    des += i1
                else:
                    break
    if '"abilities"' in i:
        f = True
    if des != "" and name != "":
        dn.append([len(des), name])
        des = ''
        name = ''
dn.sort()
print("Наибольшее описание имеет этот покемон:", dn[-1][1])
maxl = ""
slov = 0
for i in abil:
    if slov < len(list(i.split())):
        slov = len(list(i.split()))
        maxl = i
print("Самая длинная способность:", maxl)
