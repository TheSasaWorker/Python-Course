program = input('Please select which program you want to use. 1/2/3 ')
if program == '1':
    a = int(input('Please insert first number. '))
    mod = int(input('Please insert modulus. '))
    x =  6969
    def modfunc(a, mod):
        x = lambda a, mod : a % mod
        return x(a, mod)
    print(modfunc(a, mod))
elif program == '2':
    prop = 'Andrei are cinci mere verzi si sapte pere rosii stricate.'
    print(prop.replace(" pere rosii stricate", ""))
elif program == '3':
    nr_dec = int(float(input('Please insert a decimal number. ')))
    copy_of_nr_dec = nr_dec
    bin = ' '
    while copy_of_nr_dec > 0:
        mod2 = copy_of_nr_dec % 2
        bin = bin + str(mod2)
        copy_of_nr_dec = copy_of_nr_dec // 2
    print()
    print(str(nr_dec) + ' is equal to ' + bin[::-1] + 'in binary')
    