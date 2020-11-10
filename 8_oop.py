class Employee:

    raise_amount=1.1
    employee_id=10000
    def __init__(self,first,last,pay):
        self.firstname=first
        self.lastname=last
        self.payment=pay

        # self.email=f'{first.lower()}.{last.lower()}@company.com'
        Employee.employee_id+=1
        self.id=Employee.employee_id
        #atribut

    # @property
    # def email(self):
    #     return f'{self.firstname.lower()}.{self.lastname.lower()}@company.com'
    
    @property
    def fullname(self): ##method
        return f"{self.firstname} {self.lastname}"

    def apply_raise(self):
        self.payment=int(self.payment*self.raise_amount)

    @fullname.setter
    def fullname(self,name):
        first,last=name.split()
        self.firstname=first
        self.lastname=last

    @fullname.deleter
    def fullname(self):
        print('Name Deleted!')
        self.firstname=None
        self.lastname=None

    @property
    def email(self):
        if self.firstname==None and self.lastname==None:
            print('This employee is no longer in this office')
        else:
            return f'{self.firstname.lower()}.{self.lastname.lower()}@company.com'

# emp_1=Employee('Evan','Kanigara',10000000)
# emp_2=Employee('Budi','Darmawan',2000000)

# print(emp_1.firstname)
# print('gaji sebelum dinaikin',emp_1.payment)
# print(emp_1.email)
# print(emp_1.fullname())
# emp_1.apply_raise()
# print('gaji setelah dinaikin',emp_1.payment)
# # print(emp_1.__dict__)
# # print(emp_2.__dict__)

# print('gaji pak budi sekarang',emp_2.payment)
# print('rate kenaikan gaji',emp_2.raise_amount)
# emp_2.apply_raise()
# print('gaji pak Budi setelah dinaikin',emp_2.payment)

# print('ID karyawan pak Evan',emp_1.id)
# print('ID karyawan pak Budi',emp_2.id)


'''
LATIHAN DI HARI OOP
'''
# antrean=int(input('masukan jumlah antrean: '))

# uang=[]
# def ticket(antrean):
    # for i in range(antrean):
    #     uangnew=int(input('masukan jumlah uang: '))
    #     uang.append(uangnew)
#     for u in uang:
#         print(u)
#         # try: 
#         # if u == 50:
#         #     uang.remove(25)
#         #     uang.remove(50)
#         # elif u==100:
#         #     uang.remove(100)
#         #     uang.remove(50)
#         #     uang.remove(25)
#         # except ValueError:
#         #     print('No')
            
#     print(uang)
#     if uang==[]:
#         print('Yes')
#     else:
#         print('no')
    
# # ticket(antrean)

# n=int(input('masukan jumlah antrean: '))
# # eval(input())
# # s=list(map(eval,input().split()))
# s=[]
# for i in range(n):
#         uangnew=int(input('masukan jumlah uang: '))
#         s.append(uangnew)
# def check1(mon,num):
#        x=sum(mon)
#        mon.sort()
#        if x<num:
#            return False
#        if num==25:
#            if mon[0]==25:
#                mon[0]=50
               
#                return True
#            else:
#                return False
#        if num==75:
#            if mon[0]!=25:
#                 return False
#            else:
#                if mon.count(50)!=0:
#                    mon.remove(25)
#                    mon.remove(50)
#                    mon.append(100)
#                    return True
#                elif mon.count(25)>=3:
#                     mon.remove(25)
#                     mon.remove(25)
#                     mon.remove(25)
#                     mon.append(100)
#                     return True
#                else:
#                    return False
        

# money=[]
# flag=True
# for i in range(n):
      
#       if s[i]==25:
           
#            money.append(25)
           
#       elif s[i]==50:
#            if check1(money,25)!=True:
               
#                flag = False
#                break
#       else:
#             if check1(money,75)!=True:

#                flag = False
#                break
#       #print(money)
           
# if(flag):
#        print("YES")
# else:
#        print("NO")
# print(money)

'''
Line of people (Evan Kanigara)
'''


# uang=([25,25,50,100])

# def tickets(masuk):
#     x=0
#     y=0
#     z=0
#     flag=True
#     uang=masuk
#     for i in uang:
#         if i==25:
#             x+=1        
#         elif i==50:
#             y+=1
#             if x>0:
#                 x-=1            
#             else:
#                 flag=False            
#         elif i==100:
#             z+=1
#             if x>0 and y>0:
#                 x-=1
#                 y-=1            
#             elif x>=3:
#                 x-=3            
#             else:
#                 flag=False            
#     if(flag):
#         print('YES')
#     else:
#         print('NO')

# tickets([25,25,25,100])

'''
inheritance
'''

class Developer(Employee):

    working_timeline=dict()

    def __init__(self,first,last,pay,prog_lang,projects=None):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang
        if projects==None:
            self.working_on=[]
        else:
            self.working_on=[projects]
        Developer.working_timeline[self.fullname()]=self.working_on

    def make_apps(self,apps):
        if apps not in self.working_on:
            self.working_on.append(apps)
            Developer.working_timeline[self.fullname()]=self.working_on
            print(f'{self.fullname()} adding {apps} to on going projects')

class Manager(Employee):
    def __init__(self,first,last,pay,employee=None):
        super().__init__(first,last,pay)
        if employee==None:
            self.employee_list=[]
        else:
            self.employee_list=[employees]

    def add_emp(self,emp):
        if emp not in self.employee_list:
            self.employee_list.append(emp)
            print(f'{emp.fullname()} succesfully added to your list')
        else:
            print(f'{emp.fullname()} already in your list')
    
    def remove_emp(self,emp):
        if emp in self.employee_list:
            self.employee_list.remove(emp)
            print(f'{emp.fullname()} succesfully remove from your list')
        else:
            print(f'{emp.fullname()} not in your list')

    def print_emps(self):
        for emp in self.employee_list:
            print(f'-->{emp.fullname()}')

    def set_raise_amt(self,emp,amount):
        emp.raise_amount=amount

'''
Property decorator, setter, deleter
'''
emp_1=Employee('John','Smith',10000000)
print(emp_1.firstname)
print(emp_1.email)
print(emp_1.fullname)

'Setter'

emp_1.fullname='Budi Prakoso'

print(emp_1.firstname)
print(emp_1.email)
print(emp_1.fullname)

'deleter'
del emp_1.fullname
print(emp_1.firstname)
print(emp_1.email)
print(emp_1.fullname)


# dev_1=Developer('Andi','Budiman',9000000,'Python')
# print(dev_1.firstname)
# print(dev_1.fullname())
# print(dev_1.email)
# print(dev_1.working_on)
# dev_2=Developer('Joni','Suherman',8000000,'HTML')
# print(dev_2.firstname)
# print(dev_2.fullname())
# print(dev_2.email)
# print(dev_2.working_on)
# print()
# dev_1.make_apps('hangman')
# # dev_2.make_apps('snake')
# print(dev_1.working_on)
# print(dev_2.working_on)
# dev_1.make_apps('sudoku')
# dev_3=Developer('Tatang','Jaludin',8000000,'HTML','Web Mainan')
# print(Developer.working_timeline)
# print()
# mgr_1=Manager('Sue','Smith',15000000)
# print(mgr_1.firstname)
# print(mgr_1.email)
# mgr_1.add_emp(dev_1)
# mgr_1.add_emp(dev_1)
# mgr_1.print_emps()

# mgr_1.set_raise_amt(dev_1, 1.5)
# print(dev_1.raise_amount)
# print(dev_2.raise_amount)

'''
latihan datetime 
'''

import datetime as dt

# string_date='2020/02/18'
# tanggal=dt.datetime.strptime(string_date,'%Y/%m/%d')
# print(tanggal.year)
# print(tanggal.month)
# print(tanggal.day)

now=dt.datetime.now()
# print(now)
# print(now.day)
# print(now.month)
# print(now.strftime('%d'))#tanggal format dua angka
# print(now.strftime('%m'))#tahun format dua angka
# print(now.strftime('%y'))#tahun format dua angka
# print(now.strftime('%A'))#nama hari
# print(now.strftime('%Y'))#tahun format empat angka
# print(now.strftime('%B'))#nama bulan
# print()
# print(now.strftime('%H')) #format 24 jam
# print(now.strftime('%I'))#format 12 jam
# print(now.strftime('%p'))#format am/pm
# print(now.strftime('%M'))#menit
# print(now.strftime('%S'))#econd/detik

'''
import function
# '''
# from waktu import Sekarang as skr
# print(skr.time)
# print(skr.tahun)
# print(skr.bulan)
# print(skr.hari)
# print(skr.jam)
# print(skr.menit)
# print(skr.detik)



