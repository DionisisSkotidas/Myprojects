print("welcome to the tip calculator.")
bill = float(input('what was the total bill? '))
people = float(input('how many people to split the bill? '))
tip = float(input('what percentage tip would you like to give?'))

pay = (bill + (bill * (tip/100))) / people

print('Each pearson should pay: {:0.2f}'.format(pay))

