import random
from audioop import reverse

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

print('--15 uzd--')
'''Susikurkite funkciją, kuri per argumentus priimtų pažymių masyvą, bei
studento vardą su pavarde. 

Funkcija turėtų išvesti studento vardą ir pavardę, jo pažymius. 
Taip pat, suskaičiuoti vidurkį, bei jį išvesti. 

Už funkcijos ribų susikurkite reikiamus kintamuosius ir masyvus, arba
objektus studentų pažymiams saugoti ir užpildykite juos duomenimis.

Iškvieskite šią funkciją perduodant visus reikalingus duomenis.'''

def student_grades(grades, name, surname):
    print(f'{name} {surname} - { ', '.join( map(str, grades) ) }')
    sum = 0
    count = 0
    for sk in grades:
        sum += sk
        count += 1
    print(f'Grade sum: {sum}')
    print(f'Grade count: {count}')
    print(f'Grade point average: {sum / count}')

stName = 'John'
stSurname = 'Smith'
stGrades = [8, 9, 5, 6, 7]

student_grades(stGrades, stName, stSurname)

print('--16 uzd--')
def maxNumInList(maxNum):
    max = maxNum[0]
    for num in maxNum:
        if num > max:
            max = num
    print(f'Max number in list: {max}')

def generatedNum(ranNum, qty):
    for rand in range(qty):
        randomNum = random.randint(1, 100)
        ranNum.append(randomNum)

list1 = []
list2 = []
list3 = []

generatedNum(list1, 15)
generatedNum(list2, 66)
generatedNum(list3, 45)

print(list1)
maxNumInList(list1)
print(list2)
maxNumInList(list2)
print(list3)
maxNumInList(list3)

print('--17 uzd--')
def sentence():
    return 'Labas vakaras. Ketvirtadienis - mažasis penktadienis!'
print( sentence() )

print('--18 uzd--')
def randomNumber():
    return random.randint(1, 10)
print( randomNumber() )
print( randomNumber() )
print( randomNumber() )

print('--19 uzd--')
def studNameAvg(name, avg):
    return f'Studento {name} pažymių vidurkis - {avg}'
print( studNameAvg('Jono', 9.5))

print('--20 uzd--')
def minDivisor(num):
    for i in range(2, num + 1):
        if num % i == 0:
            return f'The lowest divisor of the number {num} is {i}'

for num in range(10, 30):
    print(minDivisor(num))

print('--21 uzd--')
def primeNum(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) +1 ):
        if num % i == 0:
            return False
    return True

for num in range(2, 15 +1):
    prime = primeNum(num)
    print(num, prime)

print('--22 uzd--')
def mathFunc1(a, b):
    return a + b
def mathFunc2(a, b, c):
    return a + b + c
def mathFunc3(a, b):
    return a - b

def generalFunc():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    c = random.randint(1, 50)
    print(f'{a} + {b} = {mathFunc1(a, b)}' )
    print(f'{a} + {b} + {c} = {mathFunc2(a, b, c)}')
    print(f'{a} - {b} = {mathFunc3(a, b)}')
generalFunc()
print()
generalFunc()

print('--23 uzd--')
def listSum(list):
    sum = 0
    for s in list:
        sum += s
    return sum

listOfNumbers1 = [5, 4, 6, 7, 8, 10, 33]
listOfNumbers2 = [4, 8, 14, 5, 9, 12, 58]

print(listOfNumbers1)
print( listSum(listOfNumbers1) )
print(listOfNumbers1)
print( listSum(listOfNumbers2) )

if listSum(listOfNumbers1) > listSum(listOfNumbers2):
    print('Pirmo masyvo suma didesnė')
else:
    print('Antro masyvo suma didesnė')

print('--24 uzd--')
print('---1 variantas. Maks')
def longestWord(list):
    max_length = 0
    max_word = ''
    for w in list:
        current_length = len(w)
        if current_length > max_length:
            max_length = current_length
            max_word = w
    return f'length = {max_length}, word = {max_word}'

wordList = ['eglute', 'zmogelis', 'katinas', 'keliautojai', 'saule']

print(longestWord(wordList))

print('---2 variantas. ChatGPT')
def longestWord2(list):
    maxWord = max(list, key=len)
    return maxWord

wordList2 = ['eglute', 'zmogelis', 'katinas', 'keliautojai', 'saule']
longest = longestWord2(wordList2)

print(f'word - {longest}')
print(f'Length - {len(longest)}')

print('--25 uzd--')
def studGrade(list):
    grades = 0
    for g in list:
        if g > 4:
            return True
    return False

gradeList1 = [8, 10, 5, 4, 9]
gradeList2 = [8, 7, 10, 9, 10]

print(studGrade(gradeList1))
#  nepabaigta

print('---PAPILDOMOS UŽDUOTYS---')

print('---1 uzd---')
def kinSum(a, b):
    print(a + b)
kinSum(5, 6)

print('---2 uzd---')
def PISq():
    return 9.8596
reiksme = PISq()
print(reiksme)

print('---3 uzd---')
def kinSan(a, b):
    return a * b
sandauga = kinSan(8, 9)
print(sandauga)

print('---4 uzd---')
def listLine(list):
    for i in list:
        print(i)
membersInList = ['yes', 'no', 8, 6.2, 'Hi']

listLine(membersInList)

print('---5 uzd---')

def minMax(a, b):
    return random.randint(a, b)
ranNum = minMax(10, 50)
print(ranNum)

print('---6 uzd---')
def minMaxLength(a, b, c):
    arr1 = [ random.randint(a, b) for a in range(c) ]
    return arr1

randomArr = minMaxLength(5, 80, 10)

print(f'List: {randomArr}')

print('---7 uzd---')
def sumArr(array):
    sumA = 0
    for a in array:
        sumA += a
    return sumA
sumOfArray = sumArr(randomArr)
print(sumOfArray)

print('---8 uzd---')
def avgArr(array):
    return sumArr(array) / len(array)

avgOfArray = sumArr(randomArr) / len(randomArr)
print(avgOfArray)

print('---9 uzd---')
def rectanglePrinting(a, b):
    for i in range(a):
        print('*  ' * b)

rectanglePrinting(5, 8)

print('---10 uzd---')
def sentLength(sent):
    return len(sent)

sentence = 'Šiandien labai graži diena'
print(sentLength(sentence))

print('---11 uzd---')
def codedSentence(sent):
    coded = sent[::-1]
    return coded

sntc = 'Šiandien labai graži diena'
coded_sentence = codedSentence(sntc)
print(codedSentence(sntc))