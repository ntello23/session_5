
name = input('What is yous name? ')

while True:
    try:
        age2 = int(input(f'How old are you {name}? '))
        print(f'{name}, you were born in {2024 - age2}')
        break
    except ValueError:
        print('You must input an integer for age, lets try again')