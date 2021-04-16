print("==== Penggunaan Numerik ====")

nilai = input("Masukkan nilai siswa: ").split()

for i in range(0,len(nilai)):
    nilai[i] = int(nilai[i])

jumlah = len(nilai)
ratarata = sum(nilai)/jumlah

import math
print("Nilai valid rata-rata seluruh siswa: ", math.ceil(ratarata))

print("Nilai siswa tertinggi adalah ", max(nilai))

print("Nilai siswa terendah adalah ", min(nilai))