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
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        bit = n % 2
        binario = str(bit) + binario
        n //= 2
    return binario

def SuBi(m,n):
    Dem=BiDe(m)
    Den=BiDe(n)
    return (DeBi(Dem+Den))
    
def Rebi(m,n):
    Dem=BiDe(m)
    Den=BiDe(n)
    return (DeBi(Dem-Den))
    
def MuBi(m,n):
    Dem=BiDe(m)
    Den=BiDe(n)
    return (DeBi(Dem*Den))
    
def DiBi(m,n):
    Dem=BiDe(m)
    Den=BiDe(n)
    return (DeBi(Dem//Den))