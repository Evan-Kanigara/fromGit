## Lambda ##

# def perkalian(a,b):
#     print(a*b)

# perkalian(2,3)

# x=lambda a,b: a*b
# print(x(2,3))

# y=lambda a,b,c: (a/b)*c
# print(y(1,2,3))

# z=lambda a:'Genap' if a%2==0 else 'Ganjil'
# print(z(4))
# print(z(3))

'''
Map
'''
# name_list='Andi Budi Caca'.split()

# def function(a):
#     return len(a)

# len_list=list(map(function,name_list))
# print(len_list)

# list_1='cokelat melon nangka'.split()
# list_2=[10000,5000,20000]
# couple_list=list(map(lambda a,b:a+str(b), list_1, list_2))
# print(couple_list)

'''
Filter
'''
# h=range(11)
# def kurang_lima(x):
#     if x<5:
#         return True
#     else: 
#         return False

# j=list(filter(kurang_lima,h))

# print(j)
# print(list(h))

# k=[1,2,3,4,5]
# l=[1,2,6,7,8]
# m=list(filter(lambda a:a not in k,l))
# print(m)

'''
latihan
'''
# masuk=[2,4,6,8]
# z=list(map(lambda a:a**2,masuk))
# print(z)


'''
quiz
'''
# word=['merdeka', 'hello', 'sohib', 'kari ayam', 'pesawat', 'mobil', 'loker', 'kamar', 'saya', 'motor', 'pertamax', 'merah']

# cari=str(input('Masukan huruf Anda: '))
# hasil = filter(lambda a: cari in a, word)
# print(list(hasil))

'''
reduce
'''
# from functools import reduce

# number=[6,2,3,4,5]
# number_sum=reduce(lambda a,b:a*b,number)
# print(number_sum)

# kata=['ini','ibu','budi']
# o=reduce(lambda a,b:a+b,kata)
# print(o)


'''
quiz
'''
# from functools import reduce
# angka=range(1,101)

# # c=list(filter(lambda a: a%2==0, angka))
# # print(c)
# # d=list(map(lambda a1: a1*2, c))
# # print(d)
# # e=reduce(lambda a2,b:a2+b,d)
# # print(e)

# print(reduce(lambda a2,b:a2+b,list(map(lambda a1: a1*2, list(filter(lambda a: a%2==0, angka))))))




'''
seven segment
'''

representations = {
    '0': (' _ ', '| |', '|_|'),
    '1': ('   ','  |', '  |'),
    '2': (' _ ', ' _|', '|_ '),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###'),
    '.': ('   ', '   ', '   ', '   ', '  #'),
}




def seven_segment(number):
    # treat the number as a string, since that makes it easier to deal with
    # on a digit-by-digit basis
    digits = [representations[digit] for digit in str(number)]
    print(digits)
    # now digits is a list of 5-tuples, each representing a digit in the given number
    # We'll print the first lines of each digit, the second lines of each digit, etc.
    for i in range(3):
        print("  ".join(segment[i] for segment in digits))

number=input('Input Number: ')
seven_segment(number)