print("==== Penggunaan String ====")

identitas = input("Masukkan nama panggilan Anda: ")
str = "good night,"
s = str.capitalize()
nama = identitas.capitalize()
print(s, nama)

str = "good night,"
waktu = str.replace("night", "morning")
s = waktu.capitalize()
print(s, nama)

a = nama.count("a")
i = nama.count ("i")
u = nama.count("u")
e = nama.count ("e")
o = nama.count("o")
print("Huruf vokal yang terdapat pada nama Anda adalah" ,a + i + e + o, "huruf")