def creditCard(debt,annualInterestRate,monthlyPaymentRate):
    month = 1
    total = 0
    for i in range(12):
        print('Month: '+str(month))
        unpaidDebt = debt - monthlyPaymentRate * debt
        # print('Minimal monthly payment %.2f' %(monthlyPaymentRate * debt))
        interestRate = unpaidDebt * annualInterestRate/12
        total += monthlyPaymentRate * debt
        debt = unpaidDebt + interestRate
        month+=1
        print('Remaining balance: %.2f' %debt)
    print('Total paid: %.2f' %total)
# creditCard(5000,0.2,0.04)


# problem 2
def creditCard2(debt,annualInterestRate):
    monthlyPaymentRate = 0
    originalDebt = debt
    while debt > 0:
        debt = originalDebt
        monthlyPaymentRate += 0.01
        for i in range(12):
            unpaidDebt = debt - monthlyPaymentRate 
            interestRate = unpaidDebt * annualInterestRate/12
            debt = unpaidDebt + interestRate
    print('Remaining balance: %.2f' %debt)
    return 'Lowest payment %.2f' %(monthlyPaymentRate)
# print(creditCard(99999,0.2))


# problem 3 
def creditCard3(debt,annualInterestRate):
   monthlyInterest = annualInterestRate/12
   originalDebt = debt
   monthlyLower = debt/12
   monthlyUpper = (debt*(1+monthlyInterest)**12)/12
   while debt < -0.1 or debt > 0:
       monthlyPaymentRate = (monthlyLower+monthlyUpper)/2
       debt = originalDebt
       for i in range(12):
           unpaidDebt = debt - monthlyPaymentRate 
           interestRate = unpaidDebt * annualInterestRate/12
           debt = unpaidDebt + interestRate
       if debt > 0.01: 
           monthlyLower = monthlyPaymentRate
       elif debt < 0:
           monthlyUpper = monthlyPaymentRate
   print('Remaining balance: %.2f' %debt)
   return 'Lowest payment %.2f' %monthlyPaymentRate
print(creditCard3(999999,0.18))

