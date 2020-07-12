import random
from time import sleep

money = int(input('Enter your available balance->'))
# 3
bet_amt = 0

def bet():
    user_input = int(input('Enter the amount you want too bet within your available balance->'))
    if(user_input > money):
        bet()
    else:
        return user_input

print('Available balance is ${}'.format(money))

bet_amt = bet()

print('The entered bet amount is ${}'.format(bet_amt))
print('The balance left with you is ${}'.format(money-bet_amt))
# ----------------------------------------------------------------

def left_amt():
    global money
    money += bet_amt
    print("Finally You have ", money)
''' if amt <= 0:
        print('You have no balance left to play')
    else:
        print('The available bet balance is ${}'.format(amt))
'''
# ------------------------------------------------------------------

def updateBal(amt, updation):
    # If lost then subtract the amt from bet_amt
    # If won then add the amt from bet_amt
    global bet_amt
    if updation == '+':
        bet_amt += amt;
    elif updation == '-':
        bet_amt -= amt;
    print("Currently your Bet Amount is ", bet_amt)
    print('\n')


def rand(l, h):
    result = random.randint(l, h)
    return result
"""1 for Heads 
2 for Tails"""

# Game 1=================================================================

def flipping_a_coin():
    print("Lets flip a coin")
    user_value = input("Enter your choice(Heads or Tails)->")
    user_value = user_value.title()
    print('You guessed-->', user_value)
    result = rand(1, 2)
    if(user_value == "Heads" and result == 1) or (user_value == "Tails" and result == 2):
        fbet = 100
        print("You won ${}".format(fbet))
        #return fbet
        updateBal(fbet, '+')

    else:
        fbet = 100
        print("You lost ${}".format(fbet))
        updateBal(fbet, '-')
        #return fbet

# Game 2-> 4444444444444444444444444444444444444444444444444444444444444444444444444

def roll_two_die():
    print('----------------------------------------------')
    print('Lets play Cho-Han!')
    dice1 = rand(1, 6)
    dice2 = rand(1, 6)
    total = dice1+dice2
    print("The sum of the two dice", total)
    guess = input("Enter your guess (Even or Odd)->")
    guess = guess.title()
    if (guess == "Even") and total % 2 == 0:
        dbet = 200
        print("You won ${}".format(dbet))
        print('----------------------------------------------')
        updateBal(dbet, '+')

    elif (guess == "Odd") and total % 2 != 0:
        dbet = 200
        print("You won ${}".format(dbet))
        print('----------------------------------------------')
        updateBal(dbet, '+')

    else:
        dbet = 200
        print("You lost ${}".format(200))
        print('----------------------------------------------')
        updateBal(dbet, '-')

# Game 3->$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def play_cards():
    print('----------------------------------------------')
    print("Lets play a game of Cards")
    mine = rand(1, 10)
    sleep(1)
    theirs = rand(1, 10)
    sleep(1)
    if mine > theirs:
        pbet = 250
        print("You won {}".format(250))
        print("Your card was " + str(mine) + ". Their card was "+ str(theirs))
        print("------------------------------------------")
        updateBal(pbet, '+')
    elif mine < theirs:
        pbet = 250
        print("You lost {}".format(250))
        print("Your card was " + str(mine) + ". Their card was "+ str(theirs))
        print("------------------------------------------")
        updateBal(pbet, '-')

    else:
        print("It was a tie!")
        print("-------------------------------------------")

# Game 4->^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def roulette():
    print('----------------------------------------------')
    print("Lets play Roulette")
    guess = input("Enter your choice(Even or Odd)->")
    guess = guess.title()
    result = rand(0, 37)

    if result == 37:
        print("The wheel landed on 00")
    else:
        print("The wheel landed on {}".format(result))

    if guess == "Even" and result % 2 == 0 and result != 0:
        rbet = bet_amt * 3
        print("{} is an even number.".format(result))
        print("You won {} $".format(rbet))
        print('----------------------------------------------')
        updateBal(rbet, '+')

    elif guess == "Odd" and result % 2 != 0 and result != 37:
        rbet = bet_amt * 3
        print("{} is an odd number.".format(result))
        print("You won {} $".format(rbet))
        print('----------------------------------------------')
        updateBal(rbet, '+')

    else:
        rbet = bet_amt-300
        print("You lost ${} ".format(rbet))
        print('----------------------------------------------')
        updateBal(rbet, '-')
# 888888888888888888888888888888888888888888888888888888888888888888888

bal = 0

def games(user_input):

    if user_input == 1:
        flipping_a_coin()
        user_input = int(input("Enter your choice--->"))
        games(user_input)

    elif user_input == 2:
        roll_two_die()
        user_input = int(input("Enter your choice--->"))
        games(user_input)

    elif user_input == 3:
        play_cards()
        user_input = int(input("Enter your choice--->"))
        games(user_input)

    elif user_input == 4:
        roulette()
        user_input = int(input("Enter your choice--->"))
        games(user_input)

    elif user_input == 0:
        print('Thank you for playing!!!!')
        left_amt()

    else:
        user = int(input('Enter a valid choice-->'))
        games(user)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def user_choice_message():
    message = '''
    The list of games are :
    0.TO exit the game
    1.Flipping a coin
    2.Roll two die
    3.Play Cards
    4.Roulette
    '''
    print(message)

    user_input = int(input("Enter your choice--->"))
    games(user_input)

user_choice_message()

