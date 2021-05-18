#welcome to this program message
print("Welcome to this program to figure out your interest rate")
#prompt user to enter annualized interest rate and initial investment amount
int_rate= float(input('Enter the annualized interest rate in percentage: '))
initial_investment= float(input('Enter the initial investment amount: '))

#set bal_amt equal to initial_investment
bal_amt = initial_investment

#define year=0
year = 0

#define while loop as the condition bal_amt less than doubled initial investment
while bal_amt<2*initial_investment:
        #update bal_amt and the year
        bal_amt=bal_amt + (bal_amt*(int_rate/100))
        year+=1

#print the year
print('The number of years it takes an investment to double is ', year)
