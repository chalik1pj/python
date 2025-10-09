angka = [1, 2, 3, 4]
pangkat = []

for n in angka:
  pangkat.append(n**2)
print(pangkat)

# Namun, alih-alih membuat kode program seperti di atas. Anda dapat melakukan hal berikut.
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)