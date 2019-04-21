import random
def guessNumber(guessCount) :
    secretNumber = random.randint(1,20)
    print('You will guess number between 1 and 20')
    for i in range(guessCount) :
        print('Enter your guess number:')
        guess = int(input())
        if(guess < secretNumber) :
            print('Your number is lower')
        elif(guess > secretNumber) :
            print('Your number is larger')
        else :
            break

    if(guess == secretNumber) :
        print('Guess success, the number is ' + str(guess))
    else :
        print('Guess fail, the correct number is ' + str(secretNumber))

# guessNumber(5)

def collatz(number) :
    if number % 2 ==0 :
        ret = number // 2
        print('even number convert to ' + str(ret))
        return ret
    else :
        ret = 3 * number + 1
        print('odd number convert to ' + str(ret))
        return ret

def testCollatz() :
    print('Enter a integer:')
    num = int(input())
    num = collatz(num)
    tryCount = 1
    while num != 1 :
        num = collatz(num)
        tryCount = tryCount + 1

    print('Final result is 1! Try count is ' + str(tryCount))
    
testCollatz()
