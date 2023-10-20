name1 = input('Enter your name ')
name1 = list(name1.lower())
name2 = input('Enter your loved ones name ')
name2 = list(name2.lower())

var = list('loves')
newl1 = []

newl1.extend(name1)
newl1.extend(var)
newl1.extend(name2)
x = 0
value = []
for i in newl1:
    n = 0
    total = 0
    for j in newl1:
        if newl1[x] == newl1[n]:
            total = total + 1
        n = n + 1
    value.append(total)

    x = x + 1
newl2 = dict(zip(newl1, value))
val_list = list(newl2.values())

# 1st val_list over

while len(val_list) > 2:
    if len(val_list) % 2 == 0:
        vari_list = []
        x = len(val_list) - 1
        n = 0
        for i in val_list:
            if n < len(val_list) / 2:
                vari = val_list[n] + val_list[x]
                n = n + 1
                x = x - 1
                vari_list.append(vari)
    elif len(val_list) % 2 != 0:
        vari_list = []
        a = int((len(val_list) + 1) / 2)
        n = 0
        x = len(val_list) - 1
        for i in val_list:
            if n < a - 1:
                vari = val_list[n] + val_list[x]
                n = n + 1
                x = x - 1
                vari_list.append(vari)
        vari_list.append(val_list[a - 1])
    val_list = vari_list

s = [str(i) for i in val_list]
res = "".join(s)
res = list(res)
if len(res) > 2:
    val_list = [eval(i) for i in res]
    while len(val_list) > 2:
        if len(val_list) % 2 == 0:
            vari_list = []
            x = len(val_list) - 1
            n = 0
            for i in val_list:
                if n < len(val_list) / 2:
                    vari = val_list[n] + val_list[x]
                    n = n + 1
                    x = x - 1
                    vari_list.append(vari)
        elif len(val_list) % 2 != 0:
            vari_list = []
            a = int((len(val_list) + 1) / 2)
            n = 0
            x = len(val_list) - 1
            for i in val_list:
                if n < a - 1:
                    vari = val_list[n] + val_list[x]
                    n = n + 1
                    x = x - 1
                    vari_list.append(vari)
            vari_list.append(val_list[a - 1])
        val_list = vari_list
    s = [str(i) for i in val_list]
    res = "".join(s)
    print(f'Your love percentage is {res}%')
else:
    s = [str(i) for i in val_list]
    res = "".join(s)
    print(f'Your love percentage is {res}%')
