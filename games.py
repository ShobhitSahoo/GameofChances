import random

money = int(input('Enter your available balance->'))
# 3


def bet():
    user_input = int(
        input('Enter the amount you want too bet within your available balance->'))
    if(user_input > money):
        bet()
    else:
        return user_input


print('Available balance is ${}'.format(money))
# 3
bet_amt = bet()

print('The entered bet amount is ${}'.format(bet_amt))
print('The balance left with you is ${}'.format(money-bet_amt))
# ----------------------------------------------------------------


def left_amt(amt):
    print("Your balance after playing ${}".format(amt))


'''    if amt <= 0:
        print('You have no balance left to play')
    else:
        print('The available bet balance is ${}'.format(amt))
'''
# ------------------------------------------------------------------


def rand(l, h):
    result = random.randint(l, h)
    return result

# Game 1=================================================================


def flipping_a_coin():
    print("Lets flip a coin")
    user_value = input("Enter your choice(Heads or Tails)->")
    user_value = user_value.title()
    print('Your guessed-->', user_value)
    result = rand(1, 2)
    if(user_value == "Heads" and result == 1)or (user_value == "Tails" and result == 0):
        fbet = 100
        print("You won ${}".format(fbet))
        return fbet

    else:
        fbet = 100
        print("You lost ${}".format(100))
        return fbet

# Game 2-> 4444444444444444444444444444444444444444444444444444444444444444444444444


def roll_two_die():
    print('----------------------------------------------')
    print()
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
        print()
        return dbet
    elif (guess == "Odd") and total % 2 == 0:
        dbet = 200
        print("You won ${}".format())
        print('----------------------------------------------')
        print()
        return dbet
    else:
        dbet = -200
        print("You lost ${}".format(200))
        print('----------------------------------------------')
        print()
        return dbet

# Game 3->$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def play_cards():
    print('----------------------------------------------')
    print()
    print("Lets play a game of Crds")
    mine = rand(1, 10)
    theirs = rand(1, 10)
    if mine > theirs:
        pbet = 250
        print("You won {}".format(250))
        print("------------------------------------------")
        return pbet
    elif mine < theirs:
        pbet = -250
        print("You lost {}".format(250))
        return pbet

    else:
        print("It was a tie!")
        print("------------------")
        return 0

# Game 5->^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


def roulette():
    print('----------------------------------------------')
    print()
    print("Lets play Roulette")
    guess = input("Enter your choice(Even or Odd)->")
    guess = guess.title()
    result = rand(0, 37)
    if result == 37:
        print("The wheel landed on 00")
    else:
        print("The wheel landed on {}".format(result))
    if guess == "Even" and result % 2 == 0 and result != 0:
        pbet = bet_amt*35
        print("{} is an even number.".format(result))
        print("You won {} $".format(pbet))
        print('----------------------------------------------')
        return pbet
    elif guess == "Odd" and result % 2 != 0 and result != 37:
        pbet = bet_amt*35
        print("{} is an odd number.".format(result))
        print("You won {} $".format(pbet))
        print('----------------------------------------------')
        return pbet
    else:
        pbet = bet_amt-300
        print("You lost ${} ".format(300))
        print('----------------------------------------------')
        return pbet
# 888888888888888888888888888888888888888888888888888888888888888888888


bal = 0


def games(user_input):

    if user_input == 1:
        f = flipping_a_coin()
        bet_amt += f
        user_input = int(input("Enter your choice--->"))
        games(user_input)
    elif user_input == 2:
        r = roll_two_die()
        bet_amt += r
        user_input = int(input("Enter your choice--->"))
        games(user_input)
    elif user_input == 3:
        p = play_cards()
        bet_amt += p
        user_input = int(input("Enter your choice--->"))
        games(user_input)
    elif user_input == 4:
        ro = roulette()
        bet_amt += ro
        user_input = int(input("Enter your choice--->"))
        games(user_input)
    elif user_input == 0:
        print('Thank you for playing!!!!')
        print(bet_amt)

    else:
        user = int(input('Enter a valid choice-->'))
        games(user)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def user_choice_message():
    message = '''
    The list of games are :
    1.Flipping a coin
    2.Roll two die
    3.Roulette
    4.Play Cards
    '''
    print(message)

    user_input = int(input("Enter your choice--->"))
    games(user_input)


user_choice_message()
