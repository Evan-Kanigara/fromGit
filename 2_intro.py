import math

# No 1
# x=4
# y=3
# z=2
# w=((x+y*z)/(x*y))**z
# print("Hasilnya:",w)

#No 2
# angka=int(input('Masukan angka:'))
# pangkat=int(input('Masukan pemangkat:'))
# print("Pangkat",pangkat,"dari angka",angka,"adalah:",angka**pangkat)

#No 3
# totalhari=int(input('masukan hari:'))
# tahun=str(math.floor(totalhari/360))
# bulan=str(math.floor((totalhari%360)/30))
# minggu=str(math.floor(((totalhari%360)%360)/7))
# hari=str(math.floor(((totalhari%360)%360)%7))

# print(str(totalhari),"hari adalah",tahun,"tahun",bulan,"bulan",hari,"hari")

#No 4
# total=int(input("total umur Andi dan Budi:"))
# rasio=float(input('Rasio umur andi dan Budi:'))

# umur_budi=(total*10)/(10+(rasio*10))
# umur_andi=total-umur_budi
# print('Umur Andi 2 tahun lagi adalah:{}'.format(umur_andi+2))
# print(f'Umur Budi 2 tahun lagi adalah:{umur_budi+2}')

# print(1+0.5)
# print(2*0.5)
# print(round(10//5.5,5))

#No.5
# word='Halo Dunia'.lower()
# cari=input(f'Input huruf yang ingin dicari dari {word}:').lower()
# word2=word.replace(cari,'')
# print(f'huruf {cari} ada {len(word)-len(word2)} buah')

# Jarak=int(input("Masukan jarak:"))
# speedA=int(input("Masukan kecepatan A:"))
# speedB=int(input("Masukan kecepatan B:"))
# Jam=int(input('Masukan jam:'))
# Menit=int(input('Masukan menit:'))
# Jam_akhir=math.floor((Jarak/(speedA+speedB)+(Jam+(Menit/60))))
# menit_akhir=math.ceil(((Jam+(Menit/60)+(Jarak/speedA+speedB))-Jam_akhir)%60)
# print('akan bertabrakan dalam',Jam_akhir,'jam dan',menit_akhir,'menit')