# x=5
# y='5'
# z=6

# print(x==y)

# nilai=int(input('masukan nilai: '))
# if nilai >=80:
#     print('Murid lulus')
# else:
#     print("Murid tidak lulus")


# nilai=int(input('Masukan nilai: '))
# if nilai>=80 and nilai<100:
#     print("nilai A")
# elif nilai<80 and nilai>=60:
#     print("nilai B")
# else:
#     print("nilai C")

# print(~(5>6))

# nilai=int(input("masukan nilai: "))
# if nilai%2==0:
#     print('genap')
# else:
#     print('ganjil')

# massa=input('Masukan massa: ')
# tinggi=input('Masukan tinggi (cm): ')
# if massa.isnumeric()==False or tinggi.isnumeric()==False:
#     print("Masukan angka!")
# else:
#     massa=int(massa)
#     tinggi=int(tinggi)
#     print('Berat anda',massa,'kg, tinggi Anda',tinggi/100,'m')
#     imt=((massa/tinggi)/tinggi)*10000
#     if imt>=40:
#         print("obesitas")
#     elif imt>=30 and imt<40:
#         print("sangat berlebih")
#     elif imt>=25 and imt<30:
#         print("berlebih")
#     elif imt>=18.5 and imt<25:
#         print('ideal')
#     else:
#         print('kurang')


massa=int(input('Masukan massa: '))
tinggi=int(input('Masukan tinggi (cm): '))
print('Berat anda',massa,'kg, tinggi Anda',tinggi/100,'m')
imt=((massa/tinggi)/tinggi)*10000
if imt>=40:
    print("obesitas")
elif imt>=30 and imt<40:
    print("sangat berlebih")
elif imt>=25 and imt<30:
    print("berlebih")
elif imt>=18.5 and imt<25:
    print('ideal')
else:
    print('kurang')


