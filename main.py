import hints
print("Welcome to the 3 Digits Lock Riddle")

jeden = []
dwa = []
trzy = []
cztery = []
piec = []

n = int(input("How many hints you have: "))

for i in range(n):
    print("Choose your hint:\n")
    print("1. One number is correct and well placed")
    print("2. One number is correct but wrongly placed")
    print("3. Two numbers are correct but wrongly placed")
    print("4. Nothing is correct")
    print("5. Two numbers are correct. One well placed and other wrongly placed")
    print("6. Two numbers are correct. Two well placed")
    z = int(input("Write 1-6: "))
    if z == 1:
        if i == 0:
            jeden = hints.OneCWP()
        elif i == 1:
            dwa = hints.OneCWP()
        elif i == 2:
            trzy = hints.OneCWP()
        elif i == 3:
            cztery = hints.OneCWP()
        elif i == 4:
            piec = hints.OneCWP()
    if z == 2:
        if i == 0:
            jeden = hints.OneCNWP()
        elif i == 1:
            dwa = hints.OneCNWP()
        elif i == 2:
            trzy = hints.OneCNWP()
        elif i == 3:
            cztery = hints.OneCNWP()
        elif i == 4:
            piec = hints.OneCNWP()
    if z == 3:
        if i == 0:
            jeden = hints.TwoCNWP()
        elif i == 1:
            dwa = hints.TwoCNWP()
        elif i == 2:
            trzy = hints.TwoCNWP()
        elif i == 3:
            cztery = hints.TwoCNWP()
        elif i == 4:
            piec = hints.TwoCNWP()
    if z == 4:
        if i == 0:
            jeden = hints.Nothing()
        elif i == 1:
            dwa = hints.Nothing()
        elif i == 2:
            trzy = hints.Nothing()
        elif i == 3:
            cztery = hints.Nothing()
        elif i == 4:
            piec = hints.Nothing()
    if z == 5:
        if i == 0:
            jeden = hints.TwoCOneWPOneNWP()
        elif i == 1:
            dwa = hints.TwoCOneWPOneNWP()
        elif i == 2:
            trzy = hints.TwoCOneWPOneNWP()
        elif i == 3:
            cztery = hints.TwoCOneWPOneNWP()
        elif i == 4:
            piec = hints.TwoCOneWPOneNWP()
    if z == 6:
        if i == 0:
            jeden = hints.TwoCTwoWP()
        elif i == 1:
            dwa = hints.TwoCTwoWP()
        elif i == 2:
            trzy = hints.TwoCTwoWP()
        elif i == 3:
            cztery = hints.TwoCTwoWP()
        elif i == 4:
            piec = hints.TwoCTwoWP()
hints.Solve(n,jeden,dwa,trzy,cztery,piec)
input()