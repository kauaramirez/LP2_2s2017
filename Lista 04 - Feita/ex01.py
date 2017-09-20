def mdc(n1,n2):
    resto = 1
    if n1 > 0 and n2 >0:
        if n1 > n2 and n1:
            while resto is not 0:
                resto = n1 % n2
                n1 = n2
                n2 = resto
                return n1
                if n1 < n2:
                    while resto is not 0:
                        resto = n2 % n1
                        n2 = n1
                        n1 = resto
                        return n2
    else:
        print ('Não é possivel calcular o MDC com números negativos')
        
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
res = mdc(n1,n2)
print('O MDC de ',n1,' e ',n2,' é, ',res)
