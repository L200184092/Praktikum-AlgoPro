import shelve

data = open("L200184092", "r")
NIM = data.readline()
TL = data.readline()
Nama = data.readline()
Kota = data.readline()
data.close()

data = shelve.open("Ganno")
data["newdata"] = [NIM, TL, Nama, Kota]
data.close()
