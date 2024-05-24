numberOfShare = 20000
perShareNefore= 40.00
percRate = 0.03
shareAfter = 42.75

commision1 = numberOfShare *perShareNefore *percRate
commision2 = percRate* shareAfter*numberOfShare

print('the amount of money Joe paid for the stock is $', numberOfShare*perShareNefore, sep= '')
print('the amount of commision Joe paid his broker when he bought the stock is $', numberOfShare*perShareNefore*percRate, sep='')
print('the amount that Joe sold the stock for is $', numberOfShare*shareAfter, sep='')
print('the amount of commision Joe paid his broker when he sold the stock is $', numberOfShare*shareAfter*percRate, sep='')


