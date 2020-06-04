# NOT
print("================ Operasi NOT ================")
a = True
not_a = not a

print("Data a =", a)
print("Not a =", not_a)

# OR (Jika salah satu True maka hasilnya pasti True)
print("================ Operasi OR ================")

a = False
b = False
c = a or b
print(a, "OR", b, "=", c)

a = True
b = False
c = a or b
print(a, "OR", b, " =", c)

a = False
b = True
c = a or b
print(a, " OR", b, "=", c)

a = True
b = True
c = a or b
print(a, " OR", b, " =", c)

# AND (Jika salah satu False maka hasilnya pasti False)
print("================ Operasi AND ================")

a = False
b = False
c = a and b
print(a, "AND", b, "=", c)

a = True
b = False
c = a and b
print(a, "AND", b, " =", c)

a = False
b = True
c = a and b
print(a, " AND", b, "=", c)

a = True
b = True
c = a and b
print(a, " AND", b, " =", c)

# XOR (Pembanding dan yang dibandingkan harus berbeda, jika sama hasilnya pasti False)
print("================ Operasi XOR ================")

a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)

a = True
b = False
c = a ^ b
print(a, "XOR", b, " =", c)

a = False
b = True
c = a ^ b
print(a, " XOR", b, "=", c)

a = True
b = True
c = a ^ b
print(a, " XOR", b, " =", c)
