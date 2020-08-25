"""
find square root without math.sqrt (brute force algorithm)

"""
# a = int(input("Input number for sqrt: "))
a = 47

i = 1
d1 = 0.1
d2 = 0.01
d3 = 0.001
d4 = 0.0001
counter = 0

while True:
    counter += 1
    if (i**2 == a):
        break
    elif (i**2 > a):
        i -= 1
        while True:
            counter += 1
            if (i+d1)**2 > a:
                d1 = d1 - 0.1
                while True:
                    counter += 1
                    if (i+d1+d2)**2 > a:
                        d2 = d2 - 0.01
                        while True:
                            counter += 1
                            if (i+d1+d2+d3)**2 > a:
                                d3 = d3 - 0.001
                                while True:
                                    counter += 1
                                    if (i+d1+d2+d3+d4)**2 > a:
                                        d4 = d4 - 0.0001
                                        break
                                    d4 += 0.0001
                                break
                            d3 += 0.001
                        break
                    d2 += 0.01
                break
            d1 += 0.1
        break
    i += 1

if (i**2 == a):
    print("The square root of {} is {}".format(a,i))
    print("counter =", counter)
else:
    print("The square root of {} is {}".format(a,i+d1+d2+d3+d4))
    print("counter =", counter)