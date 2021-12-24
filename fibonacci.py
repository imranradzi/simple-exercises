

def is_fibonacci():
    # will keep asking user to enter a valid integer
    while True:
        try:
            number1 = input('input an integer\n')
            number2 = int(number1)
        except:
            print('invalid number, enter again')
        else:
            break

    # initialises a list of the first two fibonacci numbers
    fibonacci = [1, 1]

    # if number entered is 1, we don't perform the loop, if it is, perform the loop
    # since 1 is a fibonacci number
    if number2 == 1:
        loop = False
    else:
        loop = True

    # loop that finds fibonacci numbers up to the greatest number equal to or greater
    # than the number entered
    while loop:
        x = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(x)
        if fibonacci[-1] >= number2:
            break

    if fibonacci[-1] == number2:
        print(number1, " is a Fibonacci number")
    else:
        print(number1, " is not a Fibonacci number")


# loops is_fibonacci until user doesn't want to enter any numbers
while True:
    is_fibonacci()
    ask = input('Would you like to enter another number? (yes/no)\n').lower()
    if ask != 'yes':
        break
