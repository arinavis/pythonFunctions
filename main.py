import random

# FUNKCIJOS 2024-10-08

arr = [1, 5, 10]
# sum = 0
# count = 0
# for i in arr:
#     count += 1
#     sum += i
# print(round(sum / count, 1))

def avg(arr):
    sum = 0
    count = 0
    for i in arr:
        count += 1
        sum += i
    return sum / count
print( avg(arr) )

def funkcija():
    print('labas')
funkcija()

print('--1 uzd--')
def prisistatymas(name, choice):
    print(f'Mano vardas - {name}, pasirinkau programavimą, nes {choice}.')

prisistatymas('Arina', 'įdomu')
prisistatymas('Arina', 'įdomu')
prisistatymas('Arina', 'įdomu')

print('--2 uzd--')
def eilerastis():
    print('Pieva, gegule raiba')
    print('Ant vėjų,')
    print('Niekas kitas –')
    print('Motulė')
    print('Tave siuvinėjo!')
    print()
eilerastis()
eilerastis()
eilerastis()
eilerastis()
eilerastis()

print('--3 uzd--')
def text1():
    return 'Labas'
def text2():
    return 'vakras.'
def text3():
    return 'Ką tu?'
print(text1(), text2(), text3())

print('--4 uzd--')
def text_1():
    print('pirma eilutė')
def text_2():
    print('antra eilute')
def text_3():
    text_1()
    text_2()

text_1()
text_2()
print()
text_3()

print('--5 uzd--')













