A = 1
B = 1

"""
7404 NOT게이트

def NOT(A,B):
    if A==1:
        return 0
    if A==0:
        return 1





"""

"""""
#7400nand게이트
def nand(A,B):
    if A+B==0:    
        return 1
    if A+B==1:
        return 1
    if A+B==2:
        return 0    
NAND = nand(A,B)
"""

""""
7402NOR게이트

def NOR(A,B):
    if A+B==0:
        return 1
    else:
        return 0
NOR = NOR(A,B)

print(NOR)

"""
def NOR(A,B):
    if A+B==0:
        return 1
    else:
        return 0
NOR = NOR(A,B)

print('U=',NOR)


def NOT(A):
    if A==1:
        return 0
    if A==0:
        return 1
NOT1 = NOT(A)
print('V=',NOT1)

def NOT(B):
    if B==1:
        return 0
    if B==0:
        return 1
NOT2 = NOT(B)
print('W=',NOT2)

def NOT(NOR):
    if NOR==1:
        return 0
    if NOR==0:
        return 1
NOT = NOT(NOR)
print('X=',NOT)

def nand(NOT1,NOT2):
    if NOT1+NOT2==0:    
        return 1
    if NOT1+NOT2==1:
        return 1
    if NOT1+NOT2==2:
        return 0    
NAND = nand(NOT1,NOT2)
print('Y=',NAND)