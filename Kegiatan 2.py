document = open("L200184092", "w")
document.write("L200184092 \n")
document.write("11/07/1999 \n")
document.write("Ganno Tribuana Kurniaji \n")
document.write("Surakarta")
document.close()

import shelve
data = open("L200184092", "r")
NIM = data.readline()
TL = data.readline()
Nama = data.readline()
Kota = data.readline()
data.close

data = shelve.open("Ganno")
data["newdata"] = [Nama, Kota, TL, NIM]
data.close()

data = shelve.open("Ganno")
print(data["newdata"][0])
print(data["newdata"][1])
print(data["newdata"][2])
print(data["newdata"][3])

