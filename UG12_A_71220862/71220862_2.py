a = input("masukkan nama :")
b = 0 
for i in range (len(a)):
    b = b + 1
    print(a[0:b])
for i in range(len(a)):
    b = b - 1
    print(a[0:b])