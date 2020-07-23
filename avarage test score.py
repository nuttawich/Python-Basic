# calculate average score input number of test
# use append store score in list
# avoid input wrong number by using while loop, if and try&except 
"""
input:  1. number of test
        2. score of each test
output: average score

"""

def calScore():
    while True:
        try:
            n = int(input("Please input number of test: "))
            if type(n) == int:
                break

        except Exception:
            print("wrong input!")
    
    score_list = []

    for i in range(n):
        print("score {}".format(i+1))
        score_list.append(float(input()))

    score_avg = sum(score_list)/n
    print("average score: {:.2f}".format(score_avg))

if __name__ == "__main__":
    calScore()   