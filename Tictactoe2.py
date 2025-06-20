# This is a sample Python script.
def sumgrp(grpcase):
    sum=0
    for i in grpcase:
        sum=i+sum
    return sum

def wrongK(K):
    for j in K:
        if my_var==K[j]:
            return 0
        elif my_var not in K:
            return 1
    return wrongK

case={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0}
G1=[case['A'],case['B'],case['C']]
G2=[case['D'],case['E'],case['F']]
G3=[case['G'],case['H'],case['I']]
G4=[case['A'],case['D'],case['G']]
G5=[case['B'],case['E'],case['H']]
G6=[case['C'],case['F'],case['I']]
G7=[case['A'],case['E'],case['I']]
G8=[case['G'],case['E'],case['C']]
grp=[G1,G2,G3,G4,G5,G6,G7,G8]

def wingrp(grp):
    for i in grp:
        resultaSomme=sumgrp(i)
        if resultaSomme==3:
            print("Joueur 1 est le gagnant")
            return 1
        elif resultaSomme==-3:
            print("Joueur 2 est le gagnant")
            return 1
        if (case['A']!=0) and (case['B']!=0) and (case['C']!=0) and (case['D']!=0) and (case['E']!=0) and (case['F']!=0) and (case['G']!=0) and (case['H']!=0) and (case['I']!=0):
            print("Ni le joueur 1, ni le Joueur 2 n'a réussi à gagner, EGALITE!")
            return 1
    return 0

J1=1
J2=-1
Tour=2
game = wingrp(grp)
while game==0:
    if Tour==1:
        Tour = 2
        J=J2
    else:
        Tour = 1
        J=J1
    print("A B C""\n""D E F""\n""G H I")
    print("\n",case['A'],case['B'],case['C'],"\n",case['D'],case['E'],case['F'],"\n",case['G'],case['H'],case['I'])
    print(f"Au Joueur {Tour} de choisir une case (lettre majuscule)")
    my_var = (input())
    #print (my_var)

    wrongK(case)

    if wrongK(case)==1:
        print("\n","Veuillez choisir une case en la nomant par sa lettre majuscule.")
        if Tour == 1:
            Tour = 2
            J = J2
        else:
            Tour = 1
            J = J1
    elif case[my_var]!=0:
        print("\n","Cette case à déjà était choisie!")
        if Tour == 1:
            Tour = 2
            J = J2
        else:
            Tour = 1
            J = J1
    else:
        case[my_var]=J
    G1 = [case['A'], case['B'], case['C']]
    G2 = [case['D'], case['E'], case['F']]
    G3 = [case['G'], case['H'], case['I']]
    G4 = [case['A'], case['D'], case['G']]
    G5 = [case['B'], case['E'], case['H']]
    G6 = [case['C'], case['F'], case['I']]
    G7 = [case['A'], case['E'], case['I']]
    G8 = [case['G'], case['E'], case['C']]
    grp = [G1, G2, G3, G4, G5, G6, G7, G8]
    game = wingrp(grp)