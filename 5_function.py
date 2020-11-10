# def hello():
#     print("Hello World!")

# hello()


# def power():
#     print(3**2)

# power()

# def power2(x):
#     print('print dari dalam function',x**2)
#     return(x**2)

# power2(4)

# hasilpower=power2(5)
# print('hasil print',hasilpower)

# def power3(angka, pangkat):
#     return angka**pangkat

# hasilpower3=power3(2,5)
# print('hasil power 3 adalah',hasilpower3)

# def calculator(angka1,operator,angka2):
#     if operator =='x':
#         return f'Hasil perkalian dari {angka1} {operator} {angka2} adalah {angka1*angka2}'
#     elif operator=='^':
#         print(angka1**angka2)
#         return angka1**angka2
#     elif operator=='+':
#         return angka1+angka2
#     elif operator=='-':
#         print(angka1-angka2)
#         return angka1-angka2
#     elif operator=='/':
#         print(angka1/angka2)
#         return angka1/angka2
#     else:
#         print("operator tidak ditemukan")

# ang1=int(input('masukan angka 1: '))
# op=input('masukan operator: ')
# ang2=int(input('masukan angka 2: '))
# x=calculator(ang1,op,ang2)
# print(x)

# application=['evankanigara','oke','koreng&']


# for app in application:
#     true=0
#     for i in app:
#         if (ord('a')<=ord(i)<=ord('z')) or (ord('A')<=ord(i)<=ord('Z')) or(i==' '):
#             true+=1
#         else:
#             true+=0

#     print('true:',true)
#     print('len: ',len(app))
#     if true==len(app):
#         print(f'{app} is an english name')
#     else:
#         print(f'{app} is not english name')


# beta={'hello':'hello'}

# print(beta['hello'])

# # beta()['hello'][2]()()[1][2]['test']()

# huruf=('a')

# huruf()


# def function1():
#     A={'Name':'Andy'}
#     return 

# function1()['Name']


# A={'oke':'11'}

# print('adalah',A['oke'])

# A={
#     'oke':'satu'
# }

# print(A['oke'])

# list=['oke','oke1']

# list[1]

# def beti():


# def myMain(key):
#     def ExecP1():
#         print("hello")
#     def ExecP2():
#         pass
#     def ExecP3():
#         pass
#     def ExecPn():
#         pass 
#     locals()['Exec' + key]()

# def returnFunction():
#     def myFunction():
#         print('hello!')
#     return myFunction

# returnFunction()()

# def asi():
#     print('hello!')
#     return asi

# asi()[1]



# def getu():
#     var='asu'
#     return var


# b=getu()
# print(b)


# def anjing():
#     return 69

# a=anjing()
# print(a)

# anjingg="this is a long sentence"
# yy=anjingg.split()[0]
# print(yy)

# def beta():
#     da=print('Andy')
#     return {'Name': da, 'Age': 20}

# beta()['Name']


# beta()['hello'][2]()()[1][2]['test']()

# def beta():
#     return{'Name': ['a','b',c], 'Age': 20}

# def c():
#     return print('berhasil')

# beta()['Name'][2]()


# def returnFunction():
#     def myFunction():
#         print('hello!')
#     return myFunction

# returnFunction()()

# def beta():
#     return{'Name': ['a','b',c], 'Age': 20}

# def c():
#     def c1():
#         print('berhasil')
#     return c1

# beta()['Name'][2]()()


# def beta():
#     def c():
#         def c1():
#             print('berhasil')
#         return c1    
#     return {'Name': ['a','b',c], 'Age': 20}


# beta()['Name'][2]()()



# def beta():
#     def c():
#         def c1():
#             a=print('berhasil')
#             return [1,a]
#         return c1    
#     return {'Name': ['a','b',c], 'Age': 20}


# beta()['Name'][2]()()[1]



# def beta():
#     def c():
#         def c1():
#             f=print('berhasil')
#             return [['a'],['b','g',f]]
#         return c1    
#     return {'Name': ['a','b',c], 'Age': 20}


# beta()['Name'][2]()()[1][2]


# def beta():
#     def c():
#         def c1():
#             f=print('berhasil')
#             return [['a'],['b','g',{'test':f}]]
#         return c1    
#     return {'Name': ['a','b',c], 'Age': 20}


# beta()['Name'][2]()()[1][2]['test']


# def beta():
#     def c():
#         def c1():
#             def c2():
#                 return print("Hello world!")
#             return [['a'],['b','g',{'test':c2}]]
#         return c1    
#     return {'hello': ['a','b',c], 'halo': 20}


# beta()['hello'][2]()()[1][2]['test']()

a=[23,25,17]
a.sort()
print(a)