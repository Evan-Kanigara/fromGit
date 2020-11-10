# employee={
#     'nama': 'Andy',
#     'usia':20,
#     'married': True,
#     'jabatan':'IT Engineer',
#     'kendaraan':['mobil','motor'],
#     'address':{
#         'street':'Jalan Mawar',
#         'RT':5,
#         'RW':2,
#         'Zipcode':12345,
#         'geo':{
#             'lat':12345.63435,
#             'long':123343.243,
#         }

#     }
# }

# print(employee)
# print('Value di dalam key nama adalah:',employee['nama'])
# print('Value di dalam key kendaraan adalah:',employee['kendaraan'])
# print('Value di dalam key kendaraan index 0 adalah:',employee['kendaraan'][0])

# print('Value di dalam key adress adalah:',employee['address'])
# print('Value di dalam key adress nama jalan adalah:',employee['address']['street'])


# hari={
#     'senin':'monday',
#     'selasa':'tuesday',
#     'rabu':'wednesday',
#     'kamis':'thursday',
#     'jumat':'friday',
#     'sabtu':'saturday',
#     'minggu':'sunday'
# }

# input=str(input("Masukan nama hari dalam bahasa Indonesia (lowecase): "))
# print("bahasa inggris dari",input,'adalah',mydict[input])

# print(list(hari.keys())[list(hari.values()).index('friday')])
# print(list(hari.keys('minggu')))
# 'jumat' in list(hari)


# input=str(input("masukan nama hari (indonesia/inggris): "))
# input=input.lower()

# if input in list(hari):
#     print("maka bahasa inggris dari",input,"adalah",hari[input])
# elif input in list(hari.values()):
#     d=list(hari.keys())[list(hari.values()).index(input)]
#     print("maka bahasa indonesia dari",input,"adalah",d)
# else:
#     print("hari Anda salah, coba masukan lagi!")


#initialize dictionary with default values
karyawan=['Doni','Fiki','Akbar']
default={'designation':'app dev','salary':5000000}

res_dict=dict.fromkeys(karyawan,default)
print(res_dict)

print(res_dict['Doni'])
