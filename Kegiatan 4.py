Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Ganno Tribuana Kurniaji"
>>> NIM = 1092
>>> Tinggi = 1.72
>>> Berat = 65
>>> TahunLahir = 1999
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # Because the "Aku" data is written in parentheses
>>> Aku[0]
1999
>>> # Because the first object in "Aku" data is "TahunLahir", The value of "TahunLahir" is 1999
>>> a = NIM % 4; Aku[a]
1999
>>> # Because the remaining result of 1092 divided by 4 is 0, so the result of Aku[0] is 1999
>>> type(Aku[a])
<class 'int'>
>>> # Because the value of "TahunLahir" is 0, 0 is an integer data type
>>> Aku[a:4]
(1999, 65, 1.72, 1092)
>>> # Because the first 4 object in the "Aku" data is "TahunLahir", "Berat", "Tinggi", and "NIM"
>>> type(Aku[4])
<class 'str'>
>>> # Because the fifth object in the "Aku" data is "Nama", The value of "Nama" is "Ganno Tribuana Kurniaji" that it is a string data type
>>> Aku[0] = "ok"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = "ok"
TypeError: 'tuple' object does not support item assignment
>>> # Because tuple element is cannot be changed
>>> type(Data)
<class 'list'>
>>> # Because the "Data" data is written in square brackets
>>> type(Data[4])
<class 'str'>
>>> # Because the fifth object in the "Data" data is "Nama", The value of"Nama" is "Ganno tribuana Kurniaji" that it is a string data type
>>> Data[4][5]
' '
>>> # Because there is no object in sixth object
>>> Data[4][a:6]
'Ganno '
>>> # Because there is only "Nama" object
>>> Data[0] = "ok"; Data
['ok', 65, 1.72, 1092, 'Ganno Tribuana Kurniaji']
>>> # Because the first object already changed with "ok"
>>> Data[-a]
'ok'
>>> # Because the first object in the "Data" data is "ok"
>>> range(a)
range(0, 0)
>>> # Because in the "a" data there is only 1 object 
