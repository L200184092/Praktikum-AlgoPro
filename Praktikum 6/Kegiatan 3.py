Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Ganno Tribuana Kurniaji"
>>> NIM = "L200184092"
>>> X = "1" + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # Because the "X" data had changed to integer data type
>>> type(b)
<class 'int'>
>>> # Because the "Nama" data has a "len" intruction
>>> a / b
47.47826086956522
>>> # Because the result of 1092 divided by 23 is 47.47826086956522
>>> a // b
47
>>> # Because the meaning of "//" is division with rounding down
>>> 10 * (a - 999)
930
>>> # Because the value of "a" minus 999 is 93, after that it will multiplied by 10 and the result is 930
>>> b ** 2
529
>>> # Because the meaning of "**" is square
>>> a % b
11
>>> # Because the meaning of "%" is remaining of the result
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # Because "12.5" is a decimal number
>>> a / c
87.36
>>> # Because the result of 1092 divided by 12.5 is 87.36
>>> a // c
87.0
>>> # Because the meaning of "//" is division with rounding down and the operand type is writed in decimal number
>>> a % c
4.5
>>> # Because the meaning of "%" is remaining of the result
>>> c > b
False
>>> # Because the "b" data has a bigger value than the "c" data
>>> type(c > b)
<class 'bool'>
>>> # Because "True" or "False" is a boolean data type
>>> a > b and b > c
True
>>> # Because in "and" operator symbol, if "True" meet with "True", The result is "True"
>>> a > 1100 or b < 10
False
>>> # Because in "or" operator symbol, if "False" meet with "False", The result is "False"
