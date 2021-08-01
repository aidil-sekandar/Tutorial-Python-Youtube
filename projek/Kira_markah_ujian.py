print("""******** SMK AIDIL ********
****** MARKAH UJIAN 1 *****""")

input('\nNama : ')
input('Kelas : ')

jumlah_markah = float(0)
subjek = ['BM','BI','MATH','SAINS']

for i in subjek:
    print("")
    print(i)
    markah = int(input("Masukkan markah : "))

    if markah >= 80:
        gred = 'A'
    elif markah >= 70:
        gred = 'B'
    elif markah >= 60:
        gred = 'C'
    elif markah >= 50:
        gred = 'D'
    else:
        gred = 'F'

    print(f'GRED : {gred}')
    jumlah_markah += markah 


purata_markah = float(jumlah_markah / 4)
if purata_markah >= 80:
    keputusan_keseluruhan = 'CEMERLANG'
elif purata_markah >= 60:
    keputusan_keseluruhan = 'SEDERHANA'
elif purata_markah >= 50:
    keputusan_keseluruhan = 'BAIK'
else:
    keputusan_keseluruhan = 'MEMUASKAN'


print('\n***************************')
print(f"JUMLAH MARKAH : {jumlah_markah}")
print(f"PURATA MARKAH : {purata_markah}")
print('***************************')
print(f"KEPUTUSAN KESELURUHAN : {keputusan_keseluruhan}")
