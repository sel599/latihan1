## MATERI ASSIGNMENT OPERATOR
# a = 40
# a*= 2 # ini sama dengan a = 40 *2
# a-= 2
# print('usia andi : {} '.format (a))

##COMPARISON OPERATOR
# x = 5
# y = '5'
# print(x == y)
# print(x > int(y))
# print(x >= int(y))
# print( x < int(y))
# print(x <= int(y))

##COMPARISON OPERATORS
# x = 5
# y ='5'
# z = 6

# print(x == int(y) and int(y) < z)
# print( x == int(y) or int(y) < z)
# print( not(x==int(y)) or int(y)<z)


##SOLVED 1
# a = int(input('input bilangan : '))
# if a%2 == 0:
#     print('genap')
# else:
#     print('ganjil')

##SOLVED 2
BB = int(input('BB dlm kg : '))
TB = int(input('Tb dalam m : '))
TB1 = TB/100
IMT = BB/(TB1**2)
if IMT < 18.5:
    print('IMT adalah {}, BB KRG'.format (IMT))
elif IMT >= 18.5 and IMT < 24.9:
    print ('IMT adalah {}, BB pas'.format (IMT))
else :
    print ('IMT adalah {}, BB lebih'.format (IMT))
