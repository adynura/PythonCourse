# FUNDAMENTAL PROGRAMMING
# COMPARISON OPERATORS
# boolean expressions
x = 10 > 3
y = 10 <= 3
z = 10 <= 20
a = 10 == 10
c = 10 != 5
print(f"{x} {y} {z} dan {a}")

# tersebut dibawah akan menghasilkan 'false' karena integer tidak sama dengan string
#
M = 10 == "10"

# --------------------------------------------------
# CONDITIONAL STATEMENTS
# jangan lupa, pake titik dua untuk menentukan statement berikutnya

# btw indentasi atau tab itu penting karena jika tdak sejajar maka dinggap diluar apps lainnya
temperature = 35
if temperature > 30:  # if condition
    print("its warm")  # jika statements of conditionnya benar, maka akan
    # perintah yang ada di space ini yang nyanyi line ini akan dikerjakan
    print("Drinking water")
elif temperature > 24:  # elif jika ada condition lainnya
    print("it's getting hot in here")
else:  # kalo tidak ada nilai yang masuk di condition, ya mau gimana lagi
    print("End")
print("Done")

# CONTOH CONDITION IF ELSE
kerja = input("apa pekerjaanmu: ")
print("owh, jadi pekerjaanmu itu", kerja)
passion = input("emang itu ya passion kamu: ")
if passion == "iya":
    print("keren!aku juga dulu ingin jadi", kerja, " tapi ga jadi,hehe")
elif passion == "enggak":
    print("owh, okay....jadi kamu kerja dibidang yg ga kamu sukai dong ya, hmm")
else:
    print("owh gitu ya...")
# -----------------------------------------------------
# TERNARY OPERATOR
umur = 32
if umur >= 30:
    print("tua")
else:
    print("masih muda lah ya")
# diatas merupakan if condition bentuk biasa dan tidak ada yang salah, tapi
# ada cara yang lebih simpel

usia = 31
# alih-alih menggunakan bentuk seperti contoh biasa diatas, gunakan saja Ternary operator
# if usia >= 31:
#    message = "okay"
# else:
#    message = "not okay, yet!"

message = "okay" if usia >= 31 else "not okay, yet!"
print(message)

# ------------------------------------------------------
# LOGICAL OPERATORS
# and, or, not
high_income = True
good_credit = True
student = False
# and = jika salah satu dari dua kondisi atau lebih adalah false, maka hasilnya false
# or = jika salahsatu dari dua atau lebih kondisi true, maka hasilnya adalah true
# not = adalah kebalikan dari nilai yang ada, jika true maka akan jadi false
if (high_income or good_credit) and not student:
    print("eligible")
else:
    print("not eligible")

# ---------------------------------------------------
# SHORT-CIRCUIT EVALUATION
#
# CHAINING COMPARISON OPERATORS
# contoh:
age = 55
if 20 <= age < 55:  # << itu yang dimaksud dengan chaining comparison
    print("masih mudah")
