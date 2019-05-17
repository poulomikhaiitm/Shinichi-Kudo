#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.
Q = int(input('Enter the quantity purchased'))
T=  100*Q         #Total price of products purchased by user
if T >1000:
        print('Will get discount of 10%')
else:
        print('no discount')
    
