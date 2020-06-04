print("====================== Membuat program konversi suhu ======================")
print("\n")

# print("========== Dari Celsius ==========")
# celcius = float(input("Masukkan suhu dalam celcius : "))
# print("Suhu : ", celcius, "derajat celcius")

# # konversi ke reamur
# reamur = (4 / 5) * celcius
# print("Suhu dalam reamur : ", reamur, "derajat reamur")

# # konversi ke fahrenheit
# fahrenheit = ((9 / 5) * celcius) + 32
# print("Suhu dalam fahrenheit : ", fahrenheit, "derajat fahrenheit")

# # konversi ke kelvin
# kelvin = celcius + 273
# print("Suhu dalam kelvin : ", kelvin, "derajat kelvin")


# print("========== Dari Fahrenheit ==========")
# suhu_fahrenheit = float(input("Masukkan suhu dalam fahrenheit : "))

# print("Suhu yang kamu input :", suhu_fahrenheit, 'derajat fahrenheit')

# suhu_kelvin = (((5 / 9) * suhu_fahrenheit) - 32) + 273
# print("Suhu dalam kelvin : ", suhu_kelvin, "derajat kelvin")


print("========== Dari Kelvin ==========")
suhu_kelvin = float(input("Masukkan suhu dalam kelvin : "))

print("Suhu yang kamu input :", suhu_kelvin, 'derajat kelvin')

suhu_fahrenheit = ((9 / 5) * (suhu_kelvin - 273)) + 32
print("Suhu dalam fahrenheit : ", suhu_fahrenheit, "derajat fahrenheit")
