from time import sleep
from os import system
from termcolor import colored as CC
# Spada ciemnoszary złom i uderza w ziemię - //GOTOWE
# płonące odłamki fruwają w powietrzu      - //GOTOWE
# przez chwilę stoi taki szary             - //GOTOWE
# zaczyna pulsować troszkę jaśniejszym szarym       - //GOTOWE
# zmienia kolor na jasnoszary                       - //GOTOWE
# przebiegają go kolory - niebieski jako finalny kolor i np żółty
# przemienia swoją postać od razu kolorując się z jasnoszarego na niebieski, ale troszę wolniej
# niebieski pulsuje teraz delikatnie
# przelatują przez niego kolory: żólty czerwony, biały - dwie różne sekwencje




n = "\n"
od  = ""
w1  = od + "     _____________     "
w2  = od + "    ╱ ___________ ╲    "
w3  = od + "   ╱╱╱           ╲ ╲   "
w4  = od + "  ╱╱╱             ╲ ╲  "
w4_1= od + " ╱╱╱               ╲╲╲ "
w5  = od + "╱╱╱                 ╲╲╲"
w6  = od + "╲╲╲      _____      ╱╱╱"
w7  = od + " ╲╲╲    ╱ ___ ╲    ╱╱╱ "
w8  = od + "  ╲╲╲  ╱ ╱   ╲ ╲  ╱╱╱  "
w9  = od + "   ╲╲╲╱ ╱     ╲╲╲╱╱╱   "
w10 = od + "    ╲╱╱╱       ╲╲╱╱    "

kolory = ['yellow', 'blue']
k = ['cyan', "green", "green"]
d = len(k)

licznik = 0
for x in range(1,17):
    a = " "*26
    sleep(0.0481-0.00141*x*2)
    system("clear")
    print('\x1b[1;30;10m'+("{}{}{}{}{}{}{}{}{}{}{}".format("\n"*x+a+w1+n,a+w2+n,a+w3+n,a+w4+n,a+w4_1+n,a+w5+n,a+w6+n,a+w7+n,a+w8+n,a+w9+n,a+w10+n)+'\x1b[0m'))
    licznik +=1

w2  = od + "      ___________ ╲"
w3  = od + "                 ╲ ╲"
w4  = od + "   ╱╱             ╲ ╲  "
w4_1= od + " ╱╱╱               ╲   "
w5  = od + "╱╱╱                    "
w6  = od + "╲╲╲      _____         "
w7  = od + " ╲╲╲    ╱ ___ ╲     ╱╱ "
w9  = od + "  ▁   ╱ ╱     ╲╲╲╱╱╱   "
w10 = od + "   ▁ ╱╱╱       ╲╲╱╱    "
a = " "*26
system("clear")
print(CC("{}{}{}{}{}{}{}{}{}{}{}".format("\n"*6+a+w1+n,a+w2+n,a+w3+n,a+w4+n,a+w4_1+n,a+w5+n,a+w6+n,a+w7+n,a+w8+n,a+w9+n,a+w10+n),  k[licznik % d]))
sleep(0.001)
w9  = od + "      ╱ ╱     ╲╲╲╱╱╱   "
w10 = od + " ▁ ▁ ╱╱╱       ╲╲╱╱    "
szary = ['\x1b[1;30;10m', '\x1b[0m']
for x in range(100):
    odlamek = "\╲╲-─-╱╱/|"
    odlamek = ['\x1b[0;31;10m' + "\\" + '\x1b[0m', '\x1b[0;31;10m' + "╲" + '\x1b[0m', '\x1b[0;31;10m' + "╲" + '\x1b[0m',
               '\x1b[0;31;10m'+"-"+'\x1b[0m', '\x1b[0;31;10m' + "─" + '\x1b[0m', '\x1b[1;34;10m' + "╱" + '\x1b[0m',
               '\x1b[0;31;10m' + "╱" + '\x1b[0m',  '\x1b[1;30;10m'+"/"+'\x1b[0m', '\x1b[0;31;10m' + "|" + '\x1b[0m']

    odlamek1 = ['\x1b[1;30;10m'+"\\"+'\x1b[0m', '\x1b[1;34;10m' + "╲" + '\x1b[0m', '\x1b[0;31;10m' + "╲" + '\x1b[0m',
                '\x1b[0;31;10m'+"-"+'\x1b[0m', '\x1b[0;31;10m' + "─" + '\x1b[0m', '\x1b[0;31;10m' + "╱" + '\x1b[0m',
                '\x1b[0;31;10m' + "╱" + '\x1b[0m', '\x1b[0;31;10m'+"/"+'\x1b[0m', '\x1b[0;31;10m' + "|" + '\x1b[0m' ]
    odlamek_kp = "/╱╱--╲╲\|"
    odlamek_kp = odlamek1
    pz = -int(x * (x - 50) / 300)+1
    pzk = -int((x-5) * ((x-5) - 50) / 500)+1
    odstep = " " * (25 - int(x / 10))
    k = odstep + odlamek[x % len(odlamek)]
    lk = len(odstep) + 1
    szary = ['\x1b[1;30;10m', '\x1b[0m']

    odstep_kp = " " * (int(x / 5.5))
    kp = odstep_kp + odlamek_kp[x % len(odlamek_kp)]

    odstep_kg = " " * (int(x / 3))
    kg = odstep_kg + odlamek_kp[x % len(odlamek_kp)]

    poczatek = "\n"*16
    p2  = lk * int(pz != 2) * " " + int(pz == 2) * k + " " * ( + int(x / 10)) + szary[0] + w1 + szary[1] + n
    p1  = lk * int(pz != 1) * " " + int(pz == 1) * k + " " * ( + int(x / 10)) + szary[0] + w2 + szary[1] + int(pzk == 3) * kg + n
    p0  = lk * int(pz != 0) * " " + int(pz == 0) * k + " " * ( + int(x / 10)) + szary[0] + w3 + szary[1] + int(pzk == 2) * kg + n
    p_1 = lk * int(pz != -1) * " " + int(pz == -1) * k + " " * ( + int(x / 10)) + szary[0] + w4 + szary[1] + int(pzk == 1) * kg + n
    p_2 = lk * int(pz != -2) * " " + int(pz == -2) * k + " " * ( + int(x / 10)) + szary[0] + w4_1 + szary[1] + int(pz == 3) * kp +int(pzk == 0) * kg + n
    p_3 = lk * int(pz != -3) * " " + int(pz == -3) * k + " " * ( + int(x / 10)) + szary[0] + w5 + szary[1] + int(pz == 2) * kp +  int(pzk == -1) * kg + n
    p_4 = lk * int(pz != -4) * " " + int(pz == -4) * k + " " * ( + int(x / 10)) + szary[0] + w6 + szary[1] + int(pz == 1) * kp +  int(pzk == -2) * kg + n
    p_5 = lk * int(pz != -5) * " " + int(pz == -5) * k + " " * ( + int(x / 10)) + szary[0] + w7 + szary[1] + int(pz == 0) * kp +  int(pzk == -3) * kg + n
    p_6 = lk * int(pz != -6) * " " + int(pz == -6) * k + " " * ( + int(x / 10)) + szary[0] + w8 + szary[1] + int(pz == -1) * kp +  int(pzk == -4) * kg + n
    p_7 = lk * int(pz != -7) * " " + int(pz == -7) * k + " " * ( + int(x / 10)) + szary[0] + w9 + szary[1] + int(pz == -2) * kp +  int(pzk == -5) * kg + n
    p_8 = lk * int(pz != -8) * " " + int(pz == -8) * k + " " * ( + int(x / 10)) + szary[0] + w10 + szary[1] + int(pz == -3) * kp +  int(pzk == -6) * kg + n

    obiekt = "{}{}{}{}{}{}{}{}{}{}{}{}".format(poczatek,p2, p1, p0, p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8)
    sleep(0.007)
    system("clear")
    print(obiekt)

kolor = ['cyan', "green", "green"]
d = len(kolor)
licznik = 0
jszary = ['\x1b[2;35;10m', '\x1b[0m']
for x in range(1,25):
    kolor = szary
    if x%6 == 0:
        kolor = jszary
    a = " "*26
    sleep(0.06)
    system("clear")
    print(kolor[0]+("{}{}{}{}{}{}{}{}{}{}{}".format("\n"*16+a+w1+n,a+w2+n,a+w3+n,a+w4+n,a+w4_1+n,a+w5+n,a+w6+n,a+w7+n,a+w8+n,a+w9+n,a+w10+n))+kolor[1])
    if x == 1:
        sleep(1.5)
    licznik +=1
sleep(0.5)
od  = "                          "

q1  = od +"     _____________\n"
q2  = od +"     ╲___________ ╲\n"
q3  = od +"   ╱             ╲╲╲\n"
q4  = od +"  ╱╱              ╲╲╲\n"
q4_1= od +" ╱╱╱                  \n"
q5  = od +"╱╱╱       ____               \n"
q6  = od +"╲╲╲      ╱  _ ╲            \n"
q7  = od +" ╲╲╲    ╱ ╱  ╲ ╲     ╱╱\n"
q8  = od +"  ╲╲╲  ╱ ╱╱   ╲╲╲  ╱╱╱\n"
q9  = od +"      ╱╱╱╱     ╲╲╲╱╱╱\n"
q10 = od +"     ╱╱╱╱       ╲╲╱╱\n"

w1 = od + w1 + "\n"
w2 = od + w2 + "\n"
w3 = od + w3 + "\n"
w4 = od + w4 + "\n"
w4_1=od + w4_1 +"\n"
w5 = od + w5 + "\n"
w6 = od + w6 + "\n"
w7 = od + w7 + "\n"
w8 = od + w8 + "\n"
w9 = od + w9 + "\n"
w10= od + w10 +"\n"

kolory = ['yellow', 'blue']
k = ['cyan', "green", "cyan"] #"green", "green"
k = ["yellow"]
licznik = 0
d = len(k)
for x in range(1,180):
    a = ""
    if x == 20:
        w10 = q10
    elif x == 25:
        w9 = q9
    elif x == 30:
        w8 = q8
    elif x == 35:
        w7 = q7
    elif x == 40:
        w6 = q6
    elif x == 45:
        w5 = q5
    elif x == 50:
        w4_1 = q4_1
    elif x == 55:
        w4 = q4
    elif x == 60:
        w3 = q3
    elif x == 65:
        w2 = q2
    elif x == 70:
        w1 = q1

    sleep(0.02)
    system("clear")
    print(CC("{}{}{}{}{}{}{}{}{}{}{}".format("\n"*16+a+w1,a+w2,a+w3,a+w4,a+w4_1,a+w5,a+w6,
                                             a+w7,a+w8,a+w9,a+w10),  k[licznik % d]))
    licznik +=1


for x in range(1,180):
    a = ""
    if x == 20:
        pass

    sleep(0.01)
    system("clear")
    print(CC("{}{}{}{}{}{}{}{}{}{}{}".format("\n"*16+a+w1,a+w2,a+w3,a+w4,a+w4_1,a+w5,a+w6,a+w7,a+w8,a+w9,a+w10),  k[licznik % d]))
    licznik +=1

