print('Welcome to the BMI Calculator. Please use metric units')
height = input('What is your height in m? ')
weight = input('What is your weight in kg? ')

bmi = float(weight) / (float(height) ** 2)

print('Your BMI is: ' + str(bmi))
