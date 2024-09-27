import math

a = int(input("Masukkan a: "))  
b = int(input("Masukkan b: ")) 

jumlah = a + b
selisih = b - a
hasil_kali = a * b
sisa_pembagian = a % b
pembagian = a / b if b != 0 else "Tidak bisa dibagi dengan nol"
log_a = math.log10(a) if a > 0 else "a harus lebih besar dari 0"
pangkat = a ** b

hasil = {
    "Jumlah a dan b": jumlah,
    "Selisih antara b dengan a": selisih,
    "Hasil kali a dan b": hasil_kali,
    "Sisa pembagian a dengan b": sisa_pembagian,
    "Pembagian a dengan b": pembagian,
    "Log10(a)": log_a,
    "a pangkat b": pangkat
}

print(f"Jumlah a dan b: {jumlah}")
print(f"Selisih antara b dengan a: {selisih}")
print(f"Hasil kali a dan b: {hasil_kali}")
print(f"Sisa pembagian a dengan b: {sisa_pembagian}")
print(f"Pembagian a dengan b: {pembagian}")
print(f"Log10(a): {log_a}")
print(f"a pangkat b: {pangkat}")
