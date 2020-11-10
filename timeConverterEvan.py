# def timeConverter(seconds):
#     if seconds>359999 or seconds<0:
#         return print('Invalid input')
#     else:
#         input=seconds
#         jam=input//3600
#         jam1=input%3600
#         menit=jam1//60
#         detik=jam1%60
#         string_date=f'{str(jam).zfill(2)}:{str(menit).zfill(2)}:{str(detik).zfill(2)}'
        
#         return print(string_date)

# timeConverter(7201)
# timeConverter(3600)
# timeConverter(359999)
# timeConverter(360000)
# timeConverter(-1)


# huruf='abcdefghijklmnopqrstuvwxyz'
# def enkripsi(kata):
#     data=[]
#     # kata = input('Input text here: ')
#     for i in kata:
#         if i in huruf:
#             data.append(huruf[(huruf.index(i)+3)%26])
#             # print(i.strip())
#             # print()
#             # print(i)
#         else:
#             data.append(i)
#     output=''.join(data)
#     return print(output)

# enkripsi("evan kanigara")

bintang=int(input("masukan jumlah bintang: "))
binmin=bintang-1
bin='*'*(bintang-1)
count=0
for i in range(binmin):
    a=(' '*i)+('*'*(binmin-(i*2)))
    count+=1
    if count==bintang/2:
        a=(' '*i)+('*')
        count+=1
    elif count>bintang/2: #i=6
        a=(' '*(i-2))+('*'*(i-2))
    print(a)
print(count)
# print(range(bintang-1))