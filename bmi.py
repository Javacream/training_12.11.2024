
name = input('Bitte Name eingeben: ')
weight = input('Bitte Körpergewicht eingeben: ')
height = input('Bitte Körpergroße eingeben: ')


print(f'Type of weight is: {type(weight)}')

weight = float(weight)
height = int(height)
bmi = weight/ (height*height)*100*100

print(f"Die Person namens {name} hat einen BMI von {bmi}")