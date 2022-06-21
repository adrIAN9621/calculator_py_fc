# start
# This fc adds two numbers
def add(x, y):
    return x + y


# This fc subtract two numbers
def subtract(x, y):
    return x - y


# This fc multiply two number
def multiply(x, y):
    return x * y


# This fc devide two numbers
def divede(x, y):
    return x / y


print('Slect operation')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Devide')

while True:
    # take user input
    choice = input('Enter choice(1/2/3/4):')

    # Print the choices
    if choice == '1':
        print('Your choice is +')

    if choice == '2':
        print('Your choice is - ')

    if choice == '3':
        print('Your choice is * ')

    if choice == '4':
        print('Your choice is / ')

    # Input the numbers
    if choice in ('1', '2', '3', '4'):
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
    # Add operation
        if choice == '1':
            print('Your choice is +')
            print(num1, '+', num2, '=', add(num1, num2))
    # Subtract operation
        if choice == '2':
            print(num1, '-', num2, '=', subtract(num1, num2))
    # Multiply operation
        if choice == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))
    # Devide operation
        if choice == '4':
            print(num1, '/', num2, '=', divede(num1, num2))

        # While to continue or break
        next_one = input('Let s do next calculation')
        if next_one == ' no':
            break
