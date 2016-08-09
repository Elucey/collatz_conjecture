print "This tests any number for the Collatz Conjecture."    
while 1 == 1:
    n=int(raw_input("Number to begin with: "))
    x = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            x = x + 1
            b = str(x)
            c = str(n)
            print "#" + b + " : " + c
        else:
            n = 3*n+1
            x = x + 1
            b = str(x)
            c = str(n)
            print "#" + b + " : " + c
    
