document = open("L200184092", "w")
document.write("L200184092 \n")
document.write("11/07/1999 \n")
document.write("Ganno Tribuana Kurniaji \n")
document.write("Surakarta")
document.close()

data = open("L200184092", "r")
NIM = data.readline()
TL = data.readline()
Nama = data.readline()
Kota = data.readline()
data.close()

print(NIM)
print(TL)
print(Nama)
print(Kota)

