def beta(): #1 memanggil fungsi beta
    def c(): #2 men-declare fungsi c
        def c1(): #4 men-declare fungsi c1
            def c2(): #6 men-declare fungsi c2
                print("Hello world!") #8 print 'Hello world!'
            return [['a'],['b','g',{'test':c2}]] #7 mengembalikan list[1][2], lebih spesifik value 'test' yaitu c2, otomatis memanggil fungsi c2
        return c1  #5 mengembalikan c1 lalu otomatis memanggil fungsi c1
    return {'hello': ['a','b',c]} #3 memanggil value dictionary 'hello' dan list [2], yaitu 'c', otomatis memanggil fungsi c


beta()['hello'][2]()()[1][2]['test']()