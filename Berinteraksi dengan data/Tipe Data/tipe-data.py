# Tipe Data Primitif
x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))


# Mutable vs Immutable
var = 10
print(var)
print(id(var))

var = 11
print(var)
print(id(var))

# Tipe Data Boolean
x = True
print(type(x))

x = False
print(type(x))

# Tipe Data String
x = 'Dicoding'
print(type(x))

# String Multi Line
multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum'at yang lalu."""

print(multi_line)

# Mengakses karakter pada string
x = 'Dicoding'
print(x[0])

# Anda dapat mengakses beberapa substring dengan menggunakan metode indexing dan slicing.
x = 'Dicoding'
print(x[2:])

# Anda dapat menampilkan teks/string berdasarkan input dari pengguna dengan berbagai cara.

# 1. Formatted String
name = "Perseus Evans"
print(f"Hello, nama saya {name}")
# 2. %-formatting
print("Nama saya %s" % (name))
# 3. str.format()
print("Nama saya {}".format(name))

# Tipe Data Collection
# List
x = [1, 2.2, 'Dicoding']
print(type(x))

# Setiap data atau elemen dalam list memiliki indeks yang selalu dimulai dari 0. Anda dapat mengakses setiap indeks pada list dengan metode indexing.
# implementasi slicing pada Python.
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

# Tuple
x = (1, "Dicoding", 1+3j)
print(type(x))

# Set
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

# OOP
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

# Dictionary
x = {
  'name': 'Perseus Evans',
  'age': 20,
  'isMarried': False
}

print(type(x))

# 1. Menambah data pada dictionary
x ['Job'] = "Web Developer"
print(x)
# 2. Menghapus data pada dictionary
del x['isMarried']
print(x)
# 3. Mengubah data pada dictionary
x['age'] = 21
print(x)