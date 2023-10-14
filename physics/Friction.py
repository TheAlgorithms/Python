print("------------------------------------------------")
print("| Menhitung Koefisien Gesek Statis dan kinentik |")
print("------------------------------------------------")


# Menghitung koefisien gesek statis
def hitung_koefisien_gesek_statis(gaya_gesek_statik, gaya_normal):
    koefisien_gesek_statis = gaya_gesek_statik / gaya_normal
    return koefisien_gesek_statis


# Menghitung koefisien gesek kinetik
def hitung_koefisien_gesek_kinetik(gaya_gesek_kinetik, gaya_normal):
    koefisien_gesek_kinetik = gaya_gesek_kinetik / gaya_normal
    return koefisien_gesek_kinetik


# Memasukkan nilai-nilai gaya gesek statis, gaya gesek kinetik, dan gaya normal
gaya_gesek_statik = float(input("Masukkan nilai gaya gesek statik (N): "))
gaya_gesek_kinetik = float(input("Masukkan nilai gaya gesek kinetik (N): "))
gaya_normal = float(input("Masukkan nilai gaya normal (N): "))

# Menghitung dan mencetak koefisien gesek statis dan kinetik
koefisien_statis = hitung_koefisien_gesek_statis(gaya_gesek_statik, gaya_normal)
koefisien_kinetik = hitung_koefisien_gesek_kinetik(gaya_gesek_kinetik, gaya_normal)

print("Koefisien gesek statis =", koefisien_statis)
print("Koefisien gesek kinetik =", koefisien_kinetik)
