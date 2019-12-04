Data = {"NIM":"L200184092", "Nama":"Ganno Tribuana Kurniaji", "Tempat/Tanggal_Lahir":"Surakarta / 7 November 1999", "Jenis_Kelamin":"Laki - laki", "Golongan_Darah":"A", "Alamat":"Genengan, Mojosongo, Jebres, Surakarta", "Agama":"Islam", "Status_Perkawinan":"Belum Kawin", "Pekerjaan":"Mahasiswa", "Kewarganegaraan":"Indonesia"}
def TampilNIM():
    print(Data["NIM"])
def TampilNama():
    print(Data["Nama"])
def TampilTTL():
    print(Data["Tempat/Tanggal_Lahir"])
def TampilJK():
    print(Data["Jenis_Kelamin"])
def TampilGD():
    print(Data["Golongan_Darah"])
def TampilAlamat():    
    print(Data["Alamat"])
def TampilAgama():    
    print(Data["Agama"])
def TampilSP():
    print(Data["Status_Perkawinan"])
def TampilPekerjaan():
    print(Data["Pekerjaan"])
def TampilKewarganegaraan():
    print(Data["Kewarganegaraan"])

print("Pilihan Yang Tersedia:")
print("f menampilkan bantuan ini")
print("z menampilkan NIM")
print("x menampilkan Nama")
print("c menampilkan Tempat/Tanggal Lahir")
print("v menampilkan Jenis Kelamin")
print("b menampilkan Golongan Darah")
print("n menampilkan Alamat")
print("m menampilkan Agama")
print("a menampilkan Status Perkawinan")
print("s menampilkan Pekerjaan")
print("d menampilkan Kewarganegaraan")
print("g untuk keluar")
print(" ")

f ='''Pilihan Yang Tersedia:
f menampilkan bantuan ini
z menampilkan NIM
x menampilkan Nama
c menampilkan Tempat/Tanggal Lahir
v menampilkan Jenis Kelamin
b menampilkan Golongan Darah
n menampilkan Alamat
m menampilkan Agama
a menampilkan Status Perkawinan
s menampilkan Pekerjaan
d menampilkan Kewarganegaraan
g untuk keluar'''

g = "Terima Kasih"
w = input("Masukkan huruf: ")
while w != "g":
    if w == "f":
        print(f)
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "z":
        TampilNIM()
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "x":
        TampilNama()
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "c":
        TampilTTL()
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "v":
        TampilJK()
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "b":
        TampilGD()
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "n":
        TampilAlamat()
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "m":
        TampilAgama()
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "a":
        TampilSP()
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "s":
        TampilPekerjaan()
        print(" ")
        w = input("Masukkan huruf: ")
    elif w == "d":
        TampilKewarganegaraan()
        print(" ")
        w = input("Masukkan huruf: ")
    else:
        print("perintah tidak dikenal")
        print(" ")
        w = input("Masukkan huruf: ")
print(g)

