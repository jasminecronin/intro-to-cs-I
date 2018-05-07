#This program calculates the final amount of money in an account that is
#accruing compound interest. The number of years to compound over is 
#taken as a user input while all other values are pret=determined.

#The principal amount in the account
P = 10000
#The number of times the interest compounds in a year
n = 12
#The interest rate
r = 0.08

#Number of years taken as user input
t = int(input("Enter the number of years the interest will be compunded for: "))

#The formula for the final amount in the account
total = P*((1+(r/n))**(n*t))

#Print statement will format the output, rounding to the nearest cent.
print("The final amount of money in the account is $%8.2f" % (total))
