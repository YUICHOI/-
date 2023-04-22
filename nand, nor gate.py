A = 1
B = 1
C = 1
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


def nand(A,B):
    if A+B==0:    
        return 1
    if A+B==1:
        return 1
    if A+B==2:
        return 0    
NAND = nand(A,B)

def NOR(NAND,C):
    if NAND+C==0:
        return 1
    else:
        return 0
NOR = NOR(NAND,C)

print('X=', NOR)

def nand(A,NOR):
    if A+NOR==0:    
        return 1
    if A+NOR==1:
        return 1
    if A+NOR==2:
        return 0    
NAND1 = nand(A,NOR)

print('Y=', NAND1)

def NOR(NAND1,C):
    if NAND1+C==0:
        return 1
    else:
        return 0
NOR1 = NOR(NAND1,C)

print('Z=',NOR1)