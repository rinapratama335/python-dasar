a = 4
b = 2

# Lebih besar dari (>)
print("=========== Lebih Besar Dari ===========")
hasil = a > 3
print(a, "> 3 =", hasil)

hasil = b > 3
print(b, "> 3 =", hasil)

hasil = b > 2
print(b, "> 2 =", hasil)

# Kurang dari (<)
print("=========== Kurang Dari ===========")
hasil = a < 3
print(a, "< 3 =", hasil)

hasil = b < 3
print(b, "< 3 =", hasil)

hasil = b < 2
print(b, "< 2 =", hasil)

# Lebih dari sama dengan (>=)
print("=========== Lebih Dari Sama Dengan ===========")
hasil = a >= 3
print(a, ">= 3 =", hasil)

hasil = b >= 3
print(b, ">= 3 =", hasil)

hasil = b >= 2
print(b, ">= 2 =", hasil)

# Kurang dari sama dengan (<=)
print("=========== Kurang Dari Sama Dengan ===========")
hasil = a <= 3
print(a, "<= 3 =", hasil)

hasil = b <= 3
print(b, "<= 3 =", hasil)

hasil = b <= 2
print(b, "<= 2 =", hasil)

# Sama dengan (==)
print("=========== Sama Dengan ===========")
hasil = a == 4
print(a, "== 4 :", hasil)
hasil = b == 4
print(b, "== 4 :", hasil)

# Tidak sama dengan (!=)
print("=========== Sama Dengan ===========")
hasil = a != 4
print(a, "!= 4 :", hasil)
hasil = b != 4
print(b, "!= 4 :", hasil)

# is dan is not
print("=========== is dan is not ===========")
a = 4  # 4 ini adalah nilai literal
object_a = id(a)
object_hex_a = hex(id(a))
b = 4
object_b = id(b)
object_hex_b = hex(id(b))
hasil = object_a is object_b
print(object_a, "is", object_b, ":", hasil)

print("")
hasil = object_hex_a is object_hex_b
print(object_hex_a, "is", object_hex_b, ":", hasil)
