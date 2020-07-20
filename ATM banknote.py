# calculate each number of banknote from ATM
"""
input:  money you want to withdraw
process: use modulo find result
output: amount of each banknote
"""

# m = int(input("enter money"))
m = 12900

if m%100 != 0:
    print('key new value')    
else:
    b1000 = int(m/1000)
    mafter1000 = m%1000
    
    b500 = int(mafter1000/500)
    mafter500 = mafter1000%500
    
    b100 = int(mafter500/100)
    mafter100 = mafter500%100
    
print('bank1000', str(b1000))
print('bank_500', str(b500))
print('bank_100', str(b100))
