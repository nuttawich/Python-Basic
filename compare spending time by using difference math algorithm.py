"""
compare spending time by using 2 difference math algorithm
1^2 + 2^2 + 3^2 + ... + n^2

1. simple sum of power two
2. advanced math formula: (n(n+1)(2n+1))/6

"""

import time

def sumExpoPower2_V1(n):
    start = time.time()

    sumP2_V1 = 0
    for i in range(n+1):
        sumP2_V1 += i**2
    
    print("Method 1")
    print("Answer: {}".format(sumP2_V1))
    print("time (ms): {:.3f}\n".format((time.time()-start)*1000))

def sumExpoPower2_V2(n):
    start = time.time()

    sumP2_V2 = int((n*(n+1)*(2*n+1))/6)

    print("Method 2")
    print("Answer: {}".format(sumP2_V2))
    print("time (ms): {:.3f}".format((time.time()-start)*1000))

if __name__ == "__main__":
    try:
        # n = int(input("input no.: "))
        n = 6479
        print("n: ",n)

        sumExpoPower2_V1(n)
        sumExpoPower2_V2(n)

    except Exception:
        print("please input number")
