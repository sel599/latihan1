# INTRO
fungsi print
usia = 22
usia = 32
print(usia)

jomblo = True
print(jomblo)
#data type
print(type(usia))
print(type(jomblo))


#FUNGSI ARITMATIKA
import math
a = 31
b = 20
print('hasilnya kalinya {}, hasil baginya {}, hasil mod {}'.format (a*b,a/b,a%b))
print('hasilnya kalinya {}, hasil baginya {}, hasil mod {}'.format (math.sqrt(a*b),math.ceil(a/b),a%b))
print('hasilnya kalinya {}, hasil baginya {}, hasil mod {}'.format (math.floor(a), math.floor(a/b),a%b))

# FUNGSI STRING
x = 'halo dunia saya'
print(len(x))
print(x.index('halo'))
print(x.split(' '))
print(x.lower())
print(x.upper())
print(x.strip(x[-1]))
print(x.replace('h','k'))
print('hasilnya x*x adalah {}'.format (x+' '+x))
print(x[1:]) # mulai print dari indeks k 1 dst
print(x[:])

##SOLVED INTRO 1
q : silakan buat inputan untuk angka dst
a  = input('nama kamu? ')
b = int(input('usia kamu?'))
c = input('jk ?')
d = input('work?')

print('nama kamu : {}, usia kamu {} tahun'.format (a,b))
# print('usia kamu : {}'.format (b))
print('usia kamu : {}'.format (c))
print('usia kamu : {}'.format (d))

##SOLVED INTRO 2
a = int(input('silakan input angka : '))
import math
print('haisl kuadratnya adalah {} '.format (math.pow(a,2)))

# SOLVED 3
x = 4
y = 3
z = 2
import math
print('w = {}'.format(math.pow(((x+(y*z))/x*y),z)))

#SOLVED 4
day= int(input('sialakn input hari : '))
tahun = day//360
bulan = (day%360)/30
minggu = ((day%360)%30)/7
hari = ((day%360)%30)%7
import math
print('hasilnya adalah  {} tahun {} bulan {} minggu {} hari'.format (tahun,math.floor(bulan),math.floor(minggu),hari))

#SOLVED 5
a = (4/14*49)
b = (10 /14 *49)
print('nilai usia andi 2 th lg {} tahun dan usia budi 2 tahun lagi {} tahun'.format (a+2, b+2))

#SOLVED 6
q : buatlah algoritma untuk menghitung karakter string pada kalimat
a = input('silakan input kalimat ')
b = input ('huruf yg akan dihitung ')
print ('memiliki huruf {} sebanyak {}' .format (b, a.count(b)))

#SOLVED 7
print('jarak mobil A& b 120 m, A berjalan 60km/h dari T dan B berjalan 40 km dari B. A & B start jam 9. Jam berpa A & B tabrakan?')
jarakAB = 120
Va = 60
Vb = 40
t = 9
tab = (jarakAB/(Va + Vb))*60
tab_h = tab//60
tab_m = tab%60

print('waktu tabrakan adalah {} jam {} menit'. format (t+tab_h , tab_m))

#SOLVED 8
print('given a fiur-digit number, perform its cyclic ritation by two digits. try to solve it only by using num method')
a = int(input('input  digit angka : '))
first = a//10
second = a%10
print('hasilnya adalah {}{} '.format(second,first))

#SOLVED 9
print('given a radius of the circle,calculate the area of the circle')
r = int(input('radius : '))
import math
print('luasnya dalah  : {}'.format ((r**2)*math.pi))

#SOLVED 10
print( ' input 1 34, input 2 98 haisl output 3948')
a = int(input('input 2 digit angka : '))
b = int(input('input 2 digit angka :  '))

a1 = a//10
a2 = a%10
b1=b//10
b2=b%10
print('outputnya : {}{}{}{}'.format(a1,b1,a2,b2))

#SOLVED 11
print('input sebuah kalimat I am a student at Purwadhika. Remove a maka hasilnya Im student t Purwdhik')
b = input('silakan input kalimat: ')
print('hasilnya : {}'. format (b.replace('a','')))

#SOLVED 12
print('input : makan hati, output : hati makan')
x = input('silakan input 2  kata : ')
x1 = x.split(' ')
print('output : {} {}'. format  (x1[1],x1[0]))


