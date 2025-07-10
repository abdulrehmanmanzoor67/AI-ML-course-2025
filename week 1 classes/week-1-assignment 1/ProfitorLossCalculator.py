# input from user

cost_price = float(input('Enter the cost price: '))
selling_price = float(input('Enter the selling price: '))


# compare and calculate

if selling_price > cost_price:
    profit= selling_price - cost_price
    print ('profit of Rs: ', profit)

elif selling_price < cost_price:
    loss = cost_price - selling_price
    print ('loss of Rs: ', loss)

else:
    print('No profit No loss')