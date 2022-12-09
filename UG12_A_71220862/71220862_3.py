a = int(input("masukkan pembatas :"))
b = int(input("Masukkan angka yang dilarang :"))

for i in range(0,a,1):
    if i == b:
        continue
    print(i,end='')