def ishora_topish(inp):
    chap_qism, ong_qism = inp.split(" = ")
    sonlar = chap_qism.split(" * ")
    ong_qism = int(ong_qism)

    belgilashlar = ["+"] * (len(sonlar) - 1)
    while True:
        natija = int(sonlar[0])
        for i in range(len(belgilashlar)):
            if belgilashlar[i] == "+":
                natija += int(sonlar[i + 1])
            elif belgilashlar[i] == "-":
                natija -= int(sonlar[i + 1])


        if natija == ong_qism:
            ifoda = sonlar[0]
            for i in range(len(belgilashlar)):
                ifoda += belgilashlar[i] + sonlar[i + 1]
            return ifoda + " = " + str(ong_qism)


        for i in range(len(belgilashlar) - 1, -1, -1):
            if belgilashlar[i] == "+":
                belgilashlar[i] = "-"
                break
            else:
                belgilashlar[i] = "+"
        else:
            break

    return "Mos keladigan birikma topilmadi"


inp = "3 * 5 * 8 * 10 * 4 = 12"
natija = ishora_topish(inp)
print(natija)
