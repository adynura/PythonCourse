import math

# VARIABLE
# Primitive type in python
# INTEGER or number
var_integer = 1000
# FLOAT or decimal
var_float = 2.99
# BOOLEAN (True / False)
var_boolean = True
# STRING or text
var_string = "this is a string, works like a magic"

# THE OUTPUT
print("VARIABLE")
print(var_integer)
print(var_float)
print(var_boolean)
print(var_string)


# ------------------------------------------
# VARIABLE NAME
# 1. harus mampu mendeskripsikan dengan jelas fungsi dan tujuan variabel tsb
# 2. Python itu case sensitive, jadi sebaiknya gunakan lowercase semua
# 3. gunakan underscore sebagai pengganti spasi

contoh_nama_var = "string ini disimpan di variabel contoh_nama_var"

# THE OUTPUT
print("variable name:")
print(contoh_nama_var)


# -------------------------------------------
# STRINGS
# gunakan single atau double quotes atau triple double quotes
course = "python programming"
# len adalah sebuah fungsi, fungsi adalah sekumpulan kode yang bisa
# digunakan untuk melakukan fungsi tertentu.
# len adalah fungsi yang dapat menghitung jumlah karakter pada suatu string
print(len(course))
# gunakan indeks ([0]) untuk mendapatkan urutan huruf tertentu pada suatu string
# adapun indeks[0] menunjukan ingin mendapatkan karakter pertama.
# kalo indeks[-1] untuk mendapat karakter terakhir pada string tersebut
print(course[0])
print(course[-1])
# [0:3] artinya akan mengambil data pertama sebanyak 3 karakter
# [0:] jika setelah colon ga dinyatakan angkanya berarti semua karakter
# pada string tersebut dipanggil.
print(course[0:])
print(course[:3])  # untuk memanggil tiga karakter pertama.


# -------------------------------------------------
# STRINGS II
# \ special character, atau biasa disebut escape
course_string = "Python \'s python programming"
print(course_string)

# --------------------------------------------------
# penggabungan variabel:
first = "mosh"
last = "hamedani"
# cara atau syntax untuk menggabungkan dua atau lebih variable
full = f"{first} {last}"
# OUTPUT
print(full)


# ---------------------------------------------------
# STRING METHODS
course = "     python programming"
# setelah menuliskan nama variabel yng tipe datanya string, tambahkan
# tanda baca titik untuk memilih methods dari variabel string tsb
# sebagai contoh:
# upper() adalah method yg berfungsi menjadikan string huruf kecil semua
print(course.upper())

# title() adalah methods yg berfungsi menjadikan huruf pertama tiap kata
# menjadi kapital
print(course.title())

# strip() adalah methods yang memiliki fungsi untuk menghapus white space
print(course.strip())

# find("") adalah method untuk mencari suatu karakter pada string, hasilnya
# adalah angka indeks urutan karakter pada string yang dimaksud.
print(course.find("pro"))

# replace("", "") adalah method untuk mengganti karakter tertentu dengan
# karakter lainnya pada string yang dimaksud
print(course.replace("p", "j"))

# method "" in merupakan method mencari karakter tapi hasilnya adalah
# boolean, begitupun dengan " " not in
print("pro" in course)
print("swift" not in course)

# --------------------------------------------------
# NUMBERS
x = 1  # integer
x = 1.1  # float
x = 1 + 2j  # complex number

# WORKING WITH NUMBERS
# built in function round untuk melakukan pembulatan
print(round(2.9))

# built in function abs atau absolute untuk mendapatkan nilai ril
print(abs(-2.9))

# method ceil yang didapat dari library math berfungsi untuk mencari nilai
# atap dari suatu bilangan
print(math.ceil(2.2))

# menambahkan comment untuk testng git
print("end of session one")
