from datetime import datetime

date = datetime.now().year
name = input('Whats your name? ')
age = int(input('age? '))
print(f"{name} your birth year is {date - age}")

