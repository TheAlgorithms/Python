nilaiPasti = {
    "sangat benar": 1,
    "benar": 0.7,
    "mungkin": 0.5,
    "kurang benar": 0.3,
    "tidak benar": 0
}

gejala = {
    "susah tidur": nilaiPasti["benar"],
    "sakit perut": nilaiPasti["kurang benar"],
    "mudah marah": nilaiPasti["benar"],
    "mudah stres": nilaiPasti["mungkin"],
    "susah konsentrasi": nilaiPasti["benar"],
    "susah makan": nilaiPasti["kurang benar"]
}

gejala2 = [gejala["susah tidur"], gejala["sakit perut"], gejala["mudah marah"],
           gejala["mudah stres"], gejala["susah konsentrasi"], gejala["susah makan"]]


def pilihanUser(jawaban):
    if jawaban == 1:
        nilai = 1
    elif jawaban == 2:
        nilai = 0.7
    elif jawaban == 3:
        nilai = 0.5
    elif jawaban == 4:
        nilai = 0.3
    else:
        nilai = 0
    return nilai


print("Indikator:")
print("Ketik 1 jika sangat benar")
print("Ketik 2 jika benar")
print("Ketik 3 jika mungkin")
print("Ketik 4 jika kurang benar")
print("Ketik 5 jika tidak benar")
nama = input("Masukkan nama kamu: ")
g1 = int(input("Apakah kamu sering susah tidur? "))
g2 = int(input("Apakah kamu sering sakit perut? "))
g3 = int(input("Apakah kamu sering mudah marah? "))
g5 = int(input("Apakah kamu sering mudah stres? "))
g4 = int(input("Apakah kamu sering susah berkonsentrasi? "))
g6 = int(input("Apakah kamu sering susah makan? "))

caseUser = [pilihanUser(g1), pilihanUser(g2), pilihanUser(
    g3), pilihanUser(g4), pilihanUser(g5), pilihanUser(g6)]
# inputUser = [0.5, 0, 0.5, 0.7, 0.7, 0.5]

# menghitung cf
cf = []
angka = 0
while angka < len(gejala2):
    cf_val = gejala2[angka] * caseUser[angka]
    cf.append(cf_val)
    angka = angka+1


# combine
cfold = cf[0]
angka2 = 1
while angka2 < len(cf):
    kom = cfold + cf[angka2] * (1-cfold)
    cfold = kom
    angka2 = angka2 + 1

presentase = kom * 100
print("Halo " + nama+" Presentase Rindu Kamu: " + "%.2f" % presentase+"%")
