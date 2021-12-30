import random


runloop = True
while runloop:
    # sets answer to a random number between 1 and 100
    answer = random.randint(1, 100)
    guess = 0

    # code runs as long as guess is not equal to answer
    while guess != answer:
        valid = True
        while valid:
            try:
                guess = int(input('Guess an integer between 1 and 100\n'))
                # if guess is out of the integer range of [1, 100], keep asking for guess
                if guess > 100 or guess < 1:
                    print('Integer out of range, please reenter')
                    while guess > 100 or guess < 1:
                        guess = int(input('Guess an integer between 1 and 100\n'))
            # if string isn't an integer, will keep asking for guess
            except:
                print('Invalid integer, reenter')
            else:
                if guess != answer:
                    print('Try again!')
                    if guess < answer:
                        print('The answer is more than ', guess)
                    else:
                        print('The answer is less than', guess)
                else:
                    print(guess, ' is the correct answer')
                valid = False

    # asks if player wants to play again
    run_again = input('Play again? (yes/no)\n').lower()
    if run_again != 'yes':
        runloop = False