import math
question = """What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
"""
answer = input(question)
if answer == "n":
    loan_principal = int(input('Enter the loan principal:'))
    monthly_payment = int(input('Enter the monthly payment:'))
    loan_interest = float(input('Enter the loan interest:'))
    
    i = loan_interest / (12 * 100)
    n = math.log((monthly_payment / (monthly_payment - i * loan_principal)), 1 + i)
    months = math.ceil(n)
    years = math.floor(months / 12)
    months = months - years * 12
    if years > 0 and months > 0:
        print(f"It will take {years} years and {months} months to repay this loan!")
    elif years > 0 and months == 0:
        print(f"It will take {years} years" if years > 1 else "It will take {years} year")
    else:
        print(f"It will take {months} months")    
elif answer == "a":
    loan_principal = int(input('Enter the loan principal:'))
    periods = int(input('Enter the number of periods:')) 
    loan_interest = float(input('Enter the loan interest:'))
    
    i = loan_interest / (12 * 100)
    n = periods
    annuity = loan_principal * (i * math.pow(1 + i, n)) / (math.pow(1+i,n)-1)
    print(f"Your monthly payment = {math.ceil(annuity)}!")
elif answer == "p":
    annuity_payment = float(input('Enter the annuity payment:'))
    n = int(input('Enter the number of periods:')) 
    loan_interest = float(input('Enter the loan interest:'))
    
    i = loan_interest / (12 * 100)
    
    principal = annuity_payment / ((i *(math.pow(1+i, n))) / (math.pow(1+i,n)-1))
    print(f"Your loan principal = {round(principal)} !")
