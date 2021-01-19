'''

# create    Al'ma (Vorotynov Kirll)
# group     20IS1bzi
# variant   6

'''
import math

'''
# lab 
/* ====== start ====== */
'''
a = 0
x = 0
resault_list = []

while a == 0:
    print('Enter a:')
    a = float(input())
    if (a == 0):print('another true')

while x == 0:
    print('Enter x:')
    x = float(input())
    if (x == 0):print('another true')

G = -((16 * a ** 2 + 24 * a * x - 27 * x ** 2) / (45 * a ** 2 - 29 * a * x + 4 * x ** 2))
F = -(math.atan(10 * a ** 2 + 13 * a * x - 30 * x ** 2))
Y = (math.log(2 * a ** 2 + 19 * a * x + 9 * x ** 2 + 1)) / (math.log(10))

resault_list.append(round(G,3))
resault_list.append(round(F,3))
resault_list.append(round(Y,3))

print('min', min(resault_list))
print('max', max(resault_list))

# def hand_switch(n):
#     if n == 1:
#         G = -((16 * a ** 2 + 24 * a * x - 27 * x ** 2) / (45 * a ** 2 - 29 * a * x + 4 * x ** 2))
#         return G
#     if n == 2:
#         F = -(math.atan(10 * a ** 2 + 13 * a * x - 30 * x ** 2))
#         return F
#     if n == 3:
#         Y = (math.log(2 * a ** 2 + 19 * a * x + 9 * x ** 2 + 1)) / (math.log(10))
#         return Y
#     else:
#         return 'fatal error.'
print(('input data: a= {} x= {}').format(a, x) )
print(('resault g= {}, f= {}, y= {}').format( round(G,3), round(F,3), round(Y,3)) )

#print(('hand switch finish : {}').format(round(hand_switch(n), 3)))


'''
/* ====== end ====== */
'''