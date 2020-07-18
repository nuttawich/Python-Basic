# calculate grade 
"""
input:  student's score (int)
process: match score with condition
output: show grade (str)
"""

try:
    score = int(input("enter score: "))

    if score >= 80:
        print('A')
    elif score >= 70:
        print('B')
    elif score >= 60:
        print('C')
    elif score >= 50:
        print('D')
    else:
        print('F')

except Exception:
    print("must be integer")