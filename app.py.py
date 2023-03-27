# CR @z.a

# Meminta pengguna untuk memasukkan nilai numerik
input_str = input("Masukkan nilai-nilai numerik, pisahkan dengan koma: ")

# Memisahkan nilai-nilai numerik menjadi list
nilai_list = input_str.split(",")

# Mengubah nilai dalam list dari string ke float 
nilai_list = [float(nilai) for nilai in nilai_list]

# Menghitung rata-rata dari nilai dalam list 
rata_rata = sum(nilai_list) /len(nilai_list)

# Mencetak hasil 
print("Nilai rata-ratanya adalah:", rata_rata)
