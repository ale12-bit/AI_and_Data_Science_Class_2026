name=input('Hello, and welcome, what is your name? ')
age=int(input('Date of Birth;'))
age=(2026-age)
if age>=18:
    print(f'your are welcome to our site {name} your are {age} years old')
else:
    print(f'your are not eligible to our site {name} your are {age} years old')
