## LOOP WHILE
# angka = 0
# while (angka <= 10):
#     print (angka)
#     angka +=1

##FOR 
# listitem = list(range(1,11,2))
# print(listitem)

# for i in range(1,11,2):
#     print (i)

## FOR I IN RANGE
# a = ''
# for i in range (1,11,1):
#     print ('nomor urut ke - ',i)

# a = ''
# for i in range (0,21,2):
#     print ('nomor urut ke - ',i)

# a = ''
# for i in range (1,20,2):
#     print ('nomor urut ke - ',i)

## FOR I IN RANGE
# a = ['A','B','C']
# for i in range (len(a)):
#     print ('nomor urut ke - ',i)
 # outputnya adalah 0,1,2
# a = ['A','B','C']
# for i in a:
#     print ('nomor urut ke - ',i)
# output adalah A,B,C

# a = ['A','B','C']
# z = ''
# for i in a:
#     z +=i 
# print (z)
# outputnya ABC

## LOOP DG HASIL *****
# z = ' '
# for i in range (5):
#     z += ' * '
# print (z)

## LOOP DG HASIL *** (tp vertikal)
# z = ''
# for i in range (3):
#     z += (' * \n')
# print (z)

##LOOP MENGELUARKAN PER KATA
# kata = ['aku', 'kamu','dia']
# z = ' '
# for i in kata:
#     z += i + 'ay'+' '
# print (z)

## LOOP OUTPUT BITANG K KOLOM, I BARIS
# z = ''
# for i in range (2):
#     for k in range (3):
#         z+=" x "
#     z += '\n'
# print(z)

##LOOP SEGITIGA KIRI 
# z = ''
# for i in range (3):
#     for j in range (0, i+1):
#         z += ' x '
#     z +='\n'
# print(z)

## solved 1cLOOP SEGITIGA KANAN
# z = ''
# for i in range (3,0,-1):
#     for j in range (i):
#         z += ' x '
#     z +='\n'
# print(z)

## solved 2 cLOOP SEGITIGA KANAN
# z = ''
# for i in range (3,0,-1):
#     for j in range (i):
#         z += ' x '
#     z +='\n'
# for k in range (1,3):
#     for l in range (0,k+1):
#         z+=' x '
#     z+='\n'

# print(z)

##SOLVED SEGITIGA NOMOR 3 

# z = ''
# for i in range (0,3,1):
#     for j in range (0, 7):
#         if j >= 3-i and j <= 3+i:
#             z += ' l '
#         else:
#             z+=' b '
#     z += '\n'
# print(z)

##SOLVED SEGITIGA NOMOR 4
# z= ''
# for i in range (3,-1,-1):
#     for j in range (0,7):
#         if j>= 3-i and j <= 3+i:
#             z += ' $ '
#         else:
#             z +=' o '
#     z+= '\n'
# print (z)

##SOLVED DIAGONAL SGTG

z= ''
for i in range (0,11):
    if i < 10:
        for j in range (0, 21):
            if j >= 10-i and j <= 10+i:
                z += ' * '
            else: 
                z += '   '    
        z += '\n'
    else:
        for k in range (11,-1, -1):
            for l in range (0, 21):
                if l >= 10-k and l <= 10+k:
                    z += ' * '
                else: 
                    z += '   '    
            z += '\n'
print (z)     

