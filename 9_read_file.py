# data=open('kata.txt','r')
# # print(data.read())
# # text=data.read()
# # print(text)

# lines=(data.readlines(2))
# print(lines)
# # for line in lines:
# #     print(line)

# # data2=open('kata2.text','w')
# # data2.write('Ini dibuat di Python')

# # data3=open('kata3.py','w')
# # data3.write("print('Ini dibuat di Python')")

# # abc=open('nama.txt','r')
# # # text=(abc.read()).replace(',','')
# # # print(text)

# # text_list=(abc.read()).split(', ')
# # print(text_list)

# # list_nama=open('list_nama.txt','w')
# # for i in text_list:
# #     list_nama.write(f'{i}\n')

# data_diri=open('daftar_nama.csv','r')
# x=data_diri.read().split('\n')
# print(x)

# header_list=x[0]
# print('header list:',header_list)
# header_element=header_list.split(',')
# print('header element:',header_element)

# value_list=x[1:]
# print(value_list)
# data=[]
# for i in value_list:
#     a=i.split(',')
#     header_value=dict(zip(header_element, a))
#     data.append(header_value)

# # print(data)

# json=open('daftar_nama.json','r')
# print(type(json.read()))

# import json

# with open('daftar_nama.json',mode='r') as daftar:
#     output=json.load(daftar)

# print(output[0])
# print(type(output))
# for i in range(len(output)):
#     print(output[i])

# output.append({'nama':'Dede','usia':24,'kota':'Bekasi'})

# print(output)
# with open('daftar_nama_update.json','w') as update:
#     json.dump(output,update)


# '''
# pakai csv
# '''
# import csv
# list_data=[]

# nama=open('daftar_nama.csv','r')
# read=csv.DictReader(nama)
# for data in read:
#     list_data.append(dict(data))

# #nama lain
# with open('daftar_nama.csv','r') as nama:
#     read=csv.DictReader(nama)
#     for data in read:
#         list_data.append(dict(data))

# print(list_data)

# with open('daftar_nama_update.csv','w') as update:
#     columns=list_data[2].keys()
#     write=csv.DictWriter(update, fieldnames=columns)
#     write.writeheader()
#     write.writerows(list_data)
# print()
# print(columns)


'''
tugas
'''
# import csv
# import json

# ##Dari CSV ke JSON
# with open('daftar_nama_update.csv') as nama:
#     reader = csv.DictReader(nama)
#     rows = list(reader)
#     print(rows)

# with open('converted_daftarnama.json', 'w') as nama1:
#     json.dump(rows, nama1)
#

import json
import csv

with open('converted_daftarnama.json',mode='r') as daftar:
    output=json.load(daftar)

print(output[0])
print(type(output))
for i in range(len(output)):
    print(output[i])

with open('converted_json.csv', 'w') as outf:
    dw = csv.DictWriter(outf, output[0].keys())
    dw.writeheader()
    for row in output:
        dw.writerow(row)

# import datetime as dt

# # string_date='2020/02/18'
# # tanggal=dt.datetime.strptime(string_date,'%Y/%m/%d')
# # print(tanggal)

# def timeConverter(seconds):
#     if seconds>359999:
#         return print('Invalid input')
#     else:
#         input=seconds
#         jam=input//3600
#         jam1=input%3600
#         menit=jam1//60
#         detik=jam1%60
#         string_date=f'{str(jam).zfill(2)}:{str(menit).zfill(2)}:{str(detik).zfill(2)}'
        
#         return print(string_date)

# timeConverter(360000)

