# i = 1
# while i<=10:
#     print(i*2)
#     i+=1

# print('selesai')

# i = 1
# while i<=10:
#     if i <=5:
#         print(i*2)
#     else:
#         print(i*3)
#     i+=1

# i=1
# while i<=20:
#     if i%2==1:
#         print(i,'itu ganjil')
#     else:
#         print(i,'itu genap')
#     i+=1

# i=0
# while i<=3:
#     a=int(input('masukan password: '))
#     if a==12345:
#         print('password correct')
#         break
#     else:
#         if i<=2:
#             print('password incorrect')
#         else:
#             print('Try again later')
#     i+=1


# a=str(input("masukan kata: "))
# i=0
# while i<len(a): # evan => 4 // 3 // 0 = e // 1 = v // 2 = a // 3 = n
#     if a[i] in 'aiue':
#         a=a.replace(a[i],'o')
#         i+=1
#     else:
#         i+=1
#         continue
# print(a)

# n=int(input('masukan angka factorial: '))

# def factorial(n):
#     if n==0:
#         return 1
#     elif n == 1:
#         return 1
#     elif n <0:
#         return 'must be positive digit'
#     else:
#         result=1
#         i=n
#         while i!=1:
#             result*=i
#             i-=1
#         return result

# print('hasilnya adalah:',factorial(n))


# n=int(input('masukan angka factorial: '))

# def factorial(n):
#     if n==0:
#         return 1
#     elif n == 1:
#         return 1
#     elif n <0:
#         return 'must be positive digit'
#     else:
#         return n*factorial(n-1)

# print('hasilnya adalah:',factorial(n))


# for i in range(1,11):
#     if i==5:
#         continue
#     else:
#         print(i*2)

# for i in range(6):
#     print('*')

# a_list=['Budi','Andi','Candi','Dedi','Edi']
# b_list=['kapiten','dokter','tukang','polisi','perawat']
# # for i in range(len(a_list)):
# #     print(f'Halo nama saya {a_list[i]}! Pekerjaan saya adalah {b_list[i]}')

# for i,j in zip(a_list,b_list):
#     print(f'Halo nama saya {i}, pekerjaan saya {j}')

# p=str(input('masukan kata: ').lower())
# i=1
# n=len(p)
# b=''
# while i <= n:
#     b=b+p[n-i]
#     i+=1

# if p==b:
#     print('maka adalah kata palindrome')
# else:
#     print('bukan kata palindrome')


a=int(input('Masukan jumlah baris: '))
def bintang(a):
    for a in range(1,a+1):
        c=print ('* '*a)
    return c
bintang(a)

# a=int(input('Masukan jumlah baris: '))
# def bintang1(a):
#     for a in reversed(range(1,a+1)):
#         c=print ('*'*a)
#     return c
# bintang1(a)

# a=int(input('Masukan jumlah: '))
# print(list(range(1,a+1)))

# a=int(input('Masukan jumlah: '))
# print(list(range(a, 0, -1)))


# a=int(input('Masukan jumlah angka: '))
# def fizzbuzz(a):
#     for a in range(1,a+1):
#         if a%3==0 and a%5==0:
#             c=print('fizzbuzz')
#         elif a%5==0:
#             c=print('buzz')
#         elif a%3==0:
#             c=print ('fizz')
#         else:
#             c=print(a)
#     return c
# fizzbuzz(a)

# 'case 2'
# d=list(input('Masukan list: '))
# i=0
# e=[]
# for i in range(len(d)):
#     k=-(i+1)
#     e.append(d[k])

# print(e)

