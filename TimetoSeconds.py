

a , b , c = input('enter saat,daghighe,sanie like the example: --> 01:23:45: ').split(':')
print(a,':',b,':',c)
a = int (a)
b = int (b)
c = int (c)
seconds = (a * 3600) + (b * 60) + c
print(seconds)