def BiDe(n):
    binario=str(n)
    rever=binario[::-1]
    p_dos=0
    for i, j in enumerate(rever):
        p_uno=(2**i)*int(j)
        if p_uno!=0:
            p_dos+=p_uno
    return p_dos

def DeBi(n):
    binario=[]
    while(True):
        if (n==0 or n==1):
            binario.append(n)
            break
        else:
            if (n%2==0):
                binario.append(0)
            elif (n%2==1):
                binario.append(1)
        cociente=n//2
        n=cociente
    rf=binario[::-1] #[::-1]-->Invertir lista
    bf=""
    for i in range(len(binario)):
        bf+=str(rf[i])
    return bf

def SuBi(m,n):
    Dem=BiDe(m)
    Den=BiDe(n)
    return (DeBi(Dem+Den))
    
def Rebi(m,n):
    Dem=BiDe(m)
    Den=BiDe(n)
    return (DeBi(Dem-Den))
    
def MuBi(m,n):        #11010 % 101
    Dem=BiDe(m)
    Den=BiDe(n)
    return (DeBi(Dem*Den))
    
def DiBi(m,n):
    Dem=BiDe(m)
    Den=BiDe(n)
    return (DeBi(Dem//Den))