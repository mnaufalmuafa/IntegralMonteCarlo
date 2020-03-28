import random as rand

def fungsi(x) :
    return 0.75*x

def isInCurve(x,n,N,BatasAtas) :
    y = fungsi((1/N)*n*BatasAtas)
    if x < y :
        return 1
    return  0

print('Fungsi : y = 3/4 * x')
print('Selang : [0,4]')
N = int(input('Banyak Percobaan : '))
BatasKiri = 0
BatasKanan = 4
BatasBawah = fungsi(BatasKiri)
BatasAtas = fungsi(BatasKanan)
print('Batas bawah : '+str(BatasBawah))
print('Batas atas : '+str(BatasAtas))
arrBilanganAcak = []
for i in range(0,N) :
    arrBilanganAcak.append(rand.uniform(BatasAtas,BatasBawah))
    if i == N-1 :
        BanyakBenar = 0
        for j in range(0,N) :
            if (isInCurve(arrBilanganAcak[j],j+1,N,BatasKanan) == 1) :
                BanyakBenar = BanyakBenar + 1
            if (j == N-1) :
                print('Banyak benar : ',BanyakBenar)
                luasKurva = BanyakBenar*(BatasKanan-BatasKiri)*(BatasAtas-BatasBawah)/N
                print('Luas kurva jika dihitung dengan metode monte carlo : ',luasKurva)
                SolusiAnalitik = 0.75 * 4 * 4 + 0.75*0*0
                print('Solusi analitik : ',SolusiAnalitik)