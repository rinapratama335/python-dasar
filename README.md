## Mengenal Operasi Komparasi

- Operasi komparasi adalah operasi yang digunakan untuk membandingkan nilai.
- Setiap hasil dari operasi komparasi adalah boolean
- Operator yang dipakai di antaranya adalah >, <, >=, <=, ==, !=, is, is not

Khusus untuk `is` dan `is not` digunakan untuk membandingkan dua/lebih variabel atau object. Sebelumnya `is` dan `is not` bis digunakan untuk syntax literal tetapi perkembangan python saat ini sudah tidak mendukung lagi.

syntax literal itu seperti ini : `a == 5` => a ada nilainya (yaitu 5) dan memakan memory. sedangkan 5 adalah nilai literalnya. Nah `is` dan `is not` ini tidak bisa dipakai di kondisi sytax literal seperti ini.

`is` dan `is not` dipakai untuk membandingkan object identity. Apa itu object identity?? Di python ketika nilai literal dismpan ke dalam memory maka dia akan memiliki `id`. Nah `id` object dari nilai literal inilah yang akan dibandingkan oleh si `is` dan `is not` tersebut.

contohnya adalah :

```
a = 4
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
```

Kode di atas menunjukkan bahwa kita membandingkan object identity dari nilai literal tersebut. Object identity ini bisa berupa `id` dan bisa juga berupa `hexadesimal` dari nilai literal tersebut.
Jika kita memaksa untuk membadingkannya dengan nilai literal maka akan terdapat warning dari python.
