# mobil=['Toyota','Honda','Marcedes']

# print(type(mobil))
# print(mobil)

# #indexing
# print(mobil[0])
# print(mobil[1])

# #slicing
# print(mobil[0:2])
# print(mobil[:3])
# print(mobil[2:7])

# #append
# mobil.append('BMW')
# print(mobil)
# mobil.append('Marcedes')
# print(mobil)

# #pop-remove
# hasil_pop=mobil.pop()
# print(mobil)
# print(hasil_pop)

# #index
# print('Index dari mobil Toyota:', mobil.index('Toyota'))
# print('Index dari y adalah:', mobil[0].index('y') )

# mobil=['Toyota','Honda','Marcedes']
# print(mobil[mobil.index('Marcedes')].index('s'))

#Membuat copy
# mobil_copy=mobil.copy()
# print(mobil)
# print(mobil_copy)

# mobil_copy.pop()
# print(mobil)
# print(mobil_copy)

# mobil2=mobil
# print(mobil)
# print(mobil2)

# mobil2.pop()
# print(mobil)
# print(mobil2)


#Exercise
#1
# jumlah=int(input('Masukan jumlah pisang yang mau dibeli: '))
# print("Harga satu pisang 3000")
# harga=jumlah*3000
# if harga>100000:
#     print("Anda mendapat diskon 10% maka harga totalnya adalah ",harga*0.9)
# elif harga>50000 and harga<=100000:
#     print("Anda mendapat harga diskon 5%m maka harga totalnya adalah ",harga*0.95)
# else:
#     print("Harga totalnya adalah",harga)


#2
# gaji=int(input("Masukan gaji Anda: "))
# year=int(input("Years of service: "))
# if year>10:
#     print("Selamat Anda mendapat bonus! Total gaji Anda adalah:",gaji*1.1)
# else:
#     print("Gaji Anda adalah:",gaji)

#3
# umur1=int(input("Masukan umur 1: "))
# umur2=int(input("Masukan umur 2: "))
# umur3=int(input("Masukan umur 3: "))

# if umur1>umur2 and umur1>umur3:
#     print("Umur 1 adalah yang paling tua")
# elif umur2>umur1 and umur2>umur3:
#     print("Umur 2 adalah yang paling tua")
# elif umur3>umur1 and umur3>umur2:
#     print("Umur 3 adalah yang paling tua")
# else:
#     print("Tidak ada yang lebih tua")

jumlahkelas=int(input("Masukan jumlah kelas: "))
kehadiran=int(input("Masukan jumlah kehadiran Anda: "))
totalkehadiran=kehadiran/jumlahkelas
if totalkehadiran>0.5:
    print("Anda boleh ikut ujian")
else:
    print("Anda tidak boleh ikut ujian")



if berat.isnumeric()==False or tinggi.isnumeric()==False:
    print("Masukan angka!")