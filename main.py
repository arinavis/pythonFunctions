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
def randSum():
    ranNum1 = random.randint(1, 5)
    ranNum2 = random.randint(5, 10)
    print(f'{ranNum1} + {ranNum2} = {ranNum1 + ranNum2}')
randSum()
randSum()
randSum()
randSum()

print('--6 uzd--')
# info = ['var', 'pav', 'amz', 'DU', 'et', 'spec']

# def pol(var, pav, amz, DU, et, spec):
#     return var, pav, amz, DU, et, spec
# result = pol('Jonas', 'Karalevičius', 31, 2000, 1, 'Pareigūnas')
# print(*result)

def pol(var, pav, amz, DU, et, spec):
    print(f'Policininkas vardu {var}, pavarde {pav}, kurio amžius {amz} metai, uždirbantis {DU} eurų per mėnesį ir dirbanti {et} etatu specializuojasi kaip {spec}.')
pol('Jonas', 'Karalevičius', 31, 2000, 1, 'Pareigūnas')

print('--7 uzd--')

def sk():
    for i in range(10):
        print( random.randint(1, 10) )
for a in range(5):
    sk()
    print()

print('--8 uzd--')
def atsSk():
    print( random.randint(1, 500) )
for i in range(10):
    atsSk()

print('--9 uzd--')
def pasisveikinimas(vardas):
    print('Labas,', vardas)
def atsisveikinimas(vardas):
    print('Viso gero,', vardas)

pasisveikinimas('Petras')
atsisveikinimas('Ona')

print('--10 uzd--')
def skaiciai(sk1, sk2):
    if sk1 > sk2:
        print(sk1)
    elif sk2 > sk1:
        print(sk2)
    else:
        print('skaičiai lygūs')
skaiciai(1,2)
skaiciai(5,2)
skaiciai(3,3)

print('--11 uzd--')
def auto(marke, model, gm, dt):
    print(f'Parduodamas automobilis {marke} {model}, {gm} metų gamybos. Automobilio variklio darbo tūris - {dt} l.')
auto('Audi', 'R8', 2006, 5.0)

print('--12 uzd--')
'''12.Sukurkite funkciją sumai skaičiuoti, ši funkcija per argumentus turėtų
gauti du skaičius, bei išvesti patį veiksmą kartu su atsakymu (pvz 7 + 5 =
12). 

Sukurkite tokias pačias funkcijas skirtumui, sandaugai ir dalmeniui
rasti. 

Sukurkite dar vieną funkciją, kuri sugeneruotų du atsitiktinius
skaičius, bei iškviestų kitas 4 funkcijas, perduodant joms sugeneruotus
skaičius. Šią bendrąją funkciją iškvieskite keletą kartų.'''

def suma(num1, num2):
    print(f'Suma: {num1} + {num2} = {num1 + num2}')
suma(5, 6)

def skirtumas(num1, num2):
    print(f'Skirtumas: {num1} - {num2} = {num1 - num2}')
skirtumas(8, 4)

def sandauga(num1, num2):
    print(f'Sandauga: {num1} * {num2} = {num1 * num2}')
sandauga(9, 6)

def dalyba(num1, num2):
    print(f'Dalyba: {num1} / {num2} = {num1 / num2}')
dalyba(20, 4)
print('---Random---')
def atsitiktinis():
    s1 = random.randint(1, 10)
    s2 = random.randint(1, 10)
    suma(s1, s2)
    skirtumas(s1, s2)
    sandauga(s1, s2)
    dalyba(s1, s2)
    print()

atsitiktinis()
atsitiktinis()
atsitiktinis()

print('--13 uzd--')
def zodziu_masyvas(list):
    sarasas = ', '.join(map(str, list))
    print(f'Sąrašas: {sarasas}')
    for z in list:
        print(f'Ilgis žodžio {z} - {len(z)} simboliai')

masyvas = ['žmogus', 'pelė', 'bakterijos']

zodziu_masyvas(masyvas)

print('--14 uzd--')
def skaiciu_masyvas(list):
    for i in list:
        print(f'{i} - {i * i / 2}')

skmasyvas1 = [5, 8, 11, 15, 4]
skmasyvas2 = [1, 11, 2, 22, 3, 33, 4, 44, 5, 55]

skaiciu_masyvas(skmasyvas1)
print()
skaiciu_masyvas(skmasyvas2)
















