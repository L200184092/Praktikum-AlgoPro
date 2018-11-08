## Program Akun
## Dibuat oleh Ganno L200184092
import random
angka = random.randint(0,1000)

Nama = 'Ganno Tribuana Kurniaji'
TanggalLahir = '7 November 1999'
NamaSingkat = Nama[0] + '. ' + Nama[6] + '. ' + Nama[15:23]
Username = Nama[0] + TanggalLahir[0] + TanggalLahir[11:15]
Password = Nama[0:4] + str(angka)
