print("Kalkulator Kimia")
print("1 = Molaritas (mol/L)")
print("2 = Normalitas (eq/L)")

# Pilihan pengguna
pilih = input("Pilih 1 atau 2: ")

# Input jumlah mol atau ekivalen
jumlah = float(input("Masukkan jumlah mol atau ekivalen: "))

# Input volume larutan dalam liter
volume = float(input("Masukkan volume larutan (liter): "))

# Perhitungan
hasil = jumlah / volume

# Output hasil
if pilih == "1":
    print("Molaritas =", hasil, "mol/L")
elif pilih == "2":
    print("Normalitas =", hasil, "eq/L")
else:
    print("Pilihan tidak valid.")
