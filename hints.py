import itertools

liczby = "0123456789"

kombinacje = set(itertools.product(liczby, repeat=3))


def OneCWP():
    print("One number is correct and well placed")
    a = input("First digit: ")
    b = input("Second digit: ")
    c = input("Third digit: ")
    jeden = set()

    for i in kombinacje:
        if i[0] == a and c not in i and b not in i:
            jeden.add(i)
        if i[1] == b and c not in i and a not in i:
            jeden.add(i)
        if i[2] == c and a not in i and b not in i:
            jeden.add(i)
    return jeden

def OneCNWP():
    print("One number is correct but wrongly placed")
    d = input("First digit: ")
    e = input("Second digit: ")
    f = input("Third digit: ")
    dwa = set()

    for i in kombinacje:
        if i[1] == d and e not in i and f not in i or i[2] == d and e not in i and f not in i:
            dwa.add(i)
        if i[0] == e and d not in i and f not in i or i[2] == e and d not in i and f not in i:
            dwa.add(i)
        if i[0] == f and e not in i and d not in i or i[1] == f and e not in i and d not in i:
            dwa.add(i)
    return dwa
def TwoCNWP():
    print("Two numbers are correct but wrongly placed")
    g = input("First digit: ")
    h = input("Second digit: ")
    ii = input("Third digit: ")
    trzy = set()

    for i in kombinacje:
        if i[0] != g and i[1] != h and ii not in i and g in i and h in i:
            trzy.add(i)
        if i[0] != g and i[2] != ii and h not in i and g in i and ii in i:
            trzy.add(i)
        if i[2] != ii and i[1] != h and g not in i and ii in i and h in i:
            trzy.add(i)
    return trzy
def TwoCOneWPOneNWP():
    print("Two numbers are correct. One well placed and other wrongly placed")
    x = input("First digit: ")
    y = input("Second digit: ")
    z = input("Third digit: ")
    special = set()
    for i in kombinacje:
        if i[0] == x and y in i and z not in i or i[0] == x and z in i and y not in i:
            special.add(i)
        if i[1] == y and x in i and z not in i or i[1] == y and z in i and x not in i:
            special.add(i)
        if i[2] == z and x in i and y not in i or i[2] == z and y in i and x not in i:
            special.add(i)
    return special
def TwoCTwoWP():
    print("Two numbers are correct. Two well placed")
    x = input("First digit: ")
    y = input("Second digit: ")
    z = input("Third digit: ")
    corr = set()
    for i in kombinacje:
        if i[0] == x and i[1] == y or i[0] == x and i[2] == z or i[1] == y and i[2] == z:
            corr.add(i)
    return corr
def Nothing():
    print("Nothing is correct")
    j = input("First digit: ")
    k = input("Second digit: ")
    l = input("Third digit: ")
    cztery = set()

    for i in kombinacje:
        if j not in i and k not in i and l not in i:
            cztery.add(i)
    return cztery

def Solve(hints,jeden,dwa,trzy,cztery,piec):
    if hints == 1:
        print("cant solve it, too hard!")
    if hints >= 2:
        jedenDwaWspolna = jeden & dwa

    if hints == 2:
        print("Number is: ")
        for i in jedenDwaWspolna:
            for j in i:
                print(j, sep=' ', end="")
            print(' ')
    if hints >=3:
        jdTrzyWspolna = jedenDwaWspolna & trzy
    if hints == 3:
        print("Number is: ")
        for i in jdTrzyWspolna:
            for j in i:
                print(j, sep=' ', end="")
            print(' ')
    if hints >= 4:
        jdtCzteryWspolna = jdTrzyWspolna & cztery
    if hints == 4:
        print("Number is: ")
        for i in jdtCzteryWspolna:
            for j in i:
                print(j, sep=' ', end="")
            print(' ')
    if hints >= 5:
        jdtcPiecWspolna = jdtCzteryWspolna & piec

    if hints == 5:
        print("Number is: ")
        for i in jdtcPiecWspolna:
            for j in i:
                print(j, sep=' ', end="")
            print(' ')
