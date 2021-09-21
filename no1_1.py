n = int(input("Masukkan Tinggi : "))

for i in range (n):
    for j in range (n, i, -1):
        print('*', end='')
    print('')