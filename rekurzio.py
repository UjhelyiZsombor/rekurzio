def szamell(a = 1,b = 1):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print('Csak számokat adjál meg!')
        return False
    return True



def szorz(a, b):
    a = int(a)
    b = int(b)
    a_a = abs(a)
    b_a = abs(b)
    
    if b_a <= 0:
        return 0

    ered = szorz(a_a, b_a - 1) + a_a
    if (a < 0 and b >= 0) or (a >= 0 and b < 0):
        ered = -ered

    global runszor
    runszor += 1
    print(f"{runszor}. futás után az eredmény: {ered}")
    return ered


def hatvany(a, k):
    a = int(a)
    k = int(k)
    if k == 0:
        return 1
    if k < 0:
        return 1 / hatvany(a, -k)
    
    ered = a * hatvany(a, k - 1)
    global runhat
    runhat += 1
    print(f"{runhat}. futás után az eredmény: {ered}")

    return ered

def Fibonacci(n,memo = None):
    if memo is None:
        memo = {}
    memo[1] = 0
    memo[2] = 1
    if n == 1:
        ered = 0
    elif n == 2:
        ered = 1
    elif n in memo:
        ered = memo[n]
    else:
        ered = Fibonacci(n-1,memo) + Fibonacci(n-2,memo)

    memo[n] = ered
    return ered

def Fibonaccikiir(n,memo = None):
    global runfib
    if memo is None:
        memo = {}
    memo[1] = 0
    memo[2] = 1
    if n == 1:
        ered = 0
    elif n == 2:
        ered = 1
    elif n in memo:
        ered = memo[n]
    else:
        ered = Fibonacci(n-1,memo) + Fibonacci(n-2,memo)

    runfib += 1
    print(f"{runfib}. futás után az eredmény: {ered}")
    memo[n] = ered
    return ered

        

def B(n, k, memo=None):
    if memo is None:
        memo = {}
        
    if k == 0 or k == n:
        ered = 1
        return ered
    
    if (n, k) in memo:
        ered = memo[(n, k)]
        return ered
        
    ered = B(n-1, k-1, memo) + B(n-1, k, memo)
    memo[(n, k)] = ered
    return ered

def Bkiir(n, k, memo=None):
    global runb
    if memo is None:
        memo = {}
        
    if k == 0 or k == n:
        ered = 1
        runb += 1
        print(f"{runb}. futás után az eredmény: {ered}")
        return ered
    
    if (n, k) in memo:
        ered = memo[(n, k)]
        runb += 1
        print(f"{runb}. futás után az eredmény: {ered}")
        return ered
        
    ered = B(n-1, k-1, memo) + B(n-1, k, memo)
    memo[(n, k)] = ered
    runb += 1
    print(f"{runb}. futás után az eredmény: {ered}")
    return ered

def euler(n, k=None):
    global runeu
    if k is None:
        k = n
    if k < 0:
        ered = 1 / euler(n, -k)  
        return ered
    if k == 0:
        ered = 1
        return ered


    ered = (1 + 1 / n) * euler(n, k - 1)
    runeu += 1
    print(f"{runeu}. futás után az eredmény: {ered}")
    return ered
 

def kiir_szor():
    kod = '''def szorz(a, b):
    a = int(a)
    b = int(b)
    a_a = abs(a)
    b_a = abs(b)
    
    if b_a <= 0:
        return 0
    
    ered = szorz(a_a, b_a - 1) + a_a
    if (a < 0 and b >= 0) or (a >= 0 and b < 0):
        ered = -ered
    
    return ered\n'''
    return kod

def kiir_hat():
    kod = '''def hatvany(a, k):
    if k == 0:
        return 1
    if k < 0:
        return 1 / hatvany(a, -k)
    return a * hatvany(a, k - 1)\n'''
    return kod

def kiir_fib():
    kod = '''def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)\n'''
    return kod

def kiir_bin():
    kod = '''def B(n, k, memo=None):
    if memo is None:
        memo = {}
        
    if k == 0 or k == n:
        return 1
    
    if (n, k) in memo:
        return memo[(n, k)]
        
    ered = B(n-1, k-1, memo) + B(n-1, k, memo)
    memo[(n, k)] = ered
    return ered\n'''
    return kod

def kiir_eu():
    kod = '''def euler(n, k=None):
    if k is None:
        k = n
    if k < 0:
        return 1 / euler(n, -k)  
    if k == 0:
        return 1

    return (1 + 1 / n) * euler(n, k - 1)\n'''
    return kod



kilepes = True
while kilepes:
    runszor = 0
    runhat = 0
    runfib = 0
    runb = 0
    runeu = 0
    print('1. Szorzás')
    print('2. Hatványozás')
    print('3. Fibonacci')
    print('4. Bionimális')
    print('5. Euler')
    print('6. Kilépés')
    valaszt = input('Kérlek válassz egyet az alábbi lehetőségek közül: ')
    if valaszt.isdigit():
        valaszt = int(valaszt)
    if valaszt == 1:
        szorzando = input('\nKérem a szorzandót! ')
        szorzo = input('Kérem a szorzót! ')
        print(f"\nA rekurzió kódja: \n{kiir_szor()}")
        if szamell(szorzando,szorzo):
            print(f"\nA szorzás eredménye: {szorz(szorzando,szorzo)}\n")
            
    elif valaszt == 2:
        alap = input('Kérem a hatványalapot! ')
        kitevo = input('Kérem a kitevőt! ')
        if szamell(alap,kitevo):
            print(f"\nA rekurzió kódja: \n{kiir_hat()}")
            print('\nA hatványozás eredménye:',hatvany(alap,kitevo),'\n')
    elif valaszt == 3:
        elem = input('Hány elemet kérsz? ')
        if szamell(elem):
            elem = int(elem)
            if elem > 0:
                print(f"\nA rekurzió kódja: \n{kiir_fib()}\n")
                for i in range(1,elem+1):
                    Fibonaccikiir(i)
                for i in range(1,elem+1):
                    print(Fibonacci(i),end=' ')
                print('\n')
            else:
                print('0-nál nagyobb számot adj meg!')
    elif valaszt == 4:
        n = input("Hanyadik fokot kéred? ")
        if szamell(n):
            n = int(n)
            if n > 0:
                print(f"\nA rekurzió kódja: \n{kiir_bin()}\n")
                for i in range(n + 1):  
                    print(Bkiir(n, i))  
                for i in range(n + 1):  
                    print(B(n, i), end=' ')  
                print("\n")
            else:
                print('0-nál nagyobb számot adj meg!')
    elif valaszt == 5:
        eu = input('Hányadik elemet szeretnéd? ')
        if szamell(eu):
            if int(eu) > 0:
                eu = int(eu)
                print(f"\nA rekurzió kódja: \n{kiir_eu()}")
                print(f"\nAz euler sorozat {eu}. eleme: {euler(eu)}\n")
            else:
                print('0-nál nagyobb számot adj meg!')
    elif valaszt == 6:
        kilepes = False
    else:
        print("A megadott menüpontok közül válassz egyet! ")