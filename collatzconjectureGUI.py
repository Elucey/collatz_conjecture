from termcolor import *
from colorama import init
init()

print "This tests any number for the Collatz Conjecture. Set your console window width to 200."    
while 1 == 1:
    n = int(raw_input("Number to begin with: "))
    x = 0
    spc = ""
    rev = False
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            x = x + 1
            b = str(x)
            c = str(n)
            cprint(spc + "#" + b + " : " + c, "green")
        else:
            n = 3 * n + 1
            x = x + 1
            b = str(x)
            c = str(n)
            if len(spc) > 1 and (len(spc)+len(b)+len(c)+4) < 197 and rev == False:
                spc = spc + " "
                cprint(spc + "#" + b + " : " + c, "yellow")
            elif (len(spc)+len(b)+len(c)+4) >= 197:
                rev = True
                spc = spc[2:]
                cprint(spc + "#" + b + " : " + c, "yellow")
            elif rev == True and len(spc) > 0:
                spc = spc[2:]
                cprint(spc + "#" + b + " : " + c, "yellow")
            elif rev == True and len(spc) == 0:
                rev = False
                spc = spc + " "
                cprint(spc + "#" + b + " : " + c, "yellow")
            else:
                rev = False
                spc = spc + " "
                cprint(spc + "#" + b + " : " + c, "yellow")
