#Welcome message
def welcome():
    print("Welcome to this program")
#Function for discount on cable
def discount(qty):
    if qty<100:
        discount=.87
    elif qty>100 and qty<250:
        discount=0.80
    elif qty>=250 and qty<500:
        discount=0.70
    else:discount=0.50
    return discount
#function for calculating the cost
def cost(qty,discount):
    amount=qty*discount
    return amount
#main program
#calling welcome message
welcome()
#reading the quantity of fiber optic cable needed
qty=int(input("Enter the quantity of fiber optic needed in feet:"))
#calling the function to find out the discount
d=discount(qty)
#displaying the companys name
print("Shades Shop")
#displaying the order quanity and price
print("Quantity ordered:",qty)
print("Discount:" , d)
#calling the function to calculate the total cost
print("Total:$",cost(qty,d))