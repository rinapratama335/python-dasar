from ctypes import c_double

data_integer = 1
print("data :", data_integer, "bertipe", type(data_integer))

data_float = 1.5
print("data :", data_float, "bertipe", type(data_float))

data_string = "irwanto"
print("data :", data_string, "bertipe", type(data_string))

data_bool = True
print("data :", data_bool, "bertipe", type(data_bool))


data_complex = complex(5, 6)
print("data :", data_complex, "bertipe", type(data_complex))

# kita bisa menggunakan tipe data dari bahasa C
data_c_double = c_double(10.5)
print("data :", data_c_double, "bertipe", type(data_c_double))
