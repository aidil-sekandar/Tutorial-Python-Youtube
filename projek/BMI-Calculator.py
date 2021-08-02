height = float(input('Enter your height in cm: '))
weight = float(input('Enter your weight in kg: '))

bmi = round((weight / (height/100)**2),2)
print('Your BMI is' ,bmi)
