import random

money = int(input('Enter your available balance->'))

# Write your game of chance functions here

# Enter the amount to bet

################################################


def bet(user):

    if(user > money):
        print('Sorry your bet amount has exceeded the available balance! Please enter a valid amount!')
        user = int(
            input('Please enter bet amount within ${}'.format(money)+' ->'))
        return user
    else:
        return user

######################################################


def chk_left_amt(amt):
    if amt <= 0:
        print("No sufficient amount left to play")
    else:
        return amt

#####################################################
# def amount(amt):

##############################################


def rand(lower, upper):
    result = random.randint(lower, upper)
    return result

###################################################


def play_cards():
    print('----------------------------------------------')
    print()
    print("Lets play a game of Crds")
    mine = rand(1, 10)
    theirs = rand(1, 10)
    if mine > theirs:
        print("You won {}")
        print("------------------------------------------")
    elif mine < theirs:
        print("You lost {}")
    else:
        print("It was a tie!")
        print("------------------")
        return 0

##############################################


def roulette():
    print('----------------------------------------------')
    print()
    print("Lets play Roulette")
    result = rand(0, 37)
    guess = input("Enter your choice(Even or Odd)->")
    guess = guess.title()
    if result == 37:
        print("The wheel landed on 00")
    else:
        print("The wheel landed on {}".format(result))
    if guess == "Even" and result % 2 == 0 and result != 0:
        print("{} is an even number.".format(result))
        print("You won {} $")
        print('----------------------------------------------')

    elif guess == "Odd" and result % 2 != 0 and result != 37:
        print("{} is an odd number.".format(result))
        print("You won {} $")
        print('----------------------------------------------')
    else:
        print("You lost ${} ")
        print('----------------------------------------------')
#################################################################


def roll_two_die(amt):
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
        print("You won ${}".format(amt))
        print('----------------------------------------------')
        print()
    elif (guess == "Odd") and total % 2 == 0:
        print("You won ${}".format(amt))
        print('----------------------------------------------')
        print()
    else:
        print("You lost ${}".format(-amt))
        print('----------------------------------------------')
        print()

#####################################################################


def flipping_a_coin():
    user = int(input('Please enter bet amount within ${}'.format(money)+' ->'))
    user = bet(user)
    left_amt = money-user
    # print("The value of bet is ", user)
    print("Bet balance: ${}".format(user))
    print("Available balance: ${}".format(left_amt))
    print('-----------------------------------------------')
    print("Lets flip a coin")
    user_value = input("Enter your choice(Heads or Tails)")
    print('Your guessed-->', user_value)
    result = rand(1, 2)
    if(user_value == "Heads" and result == 1)or (user_value == "Tails" and result == 0):
        print("You won ${}".format(user))
    else:
        print("You lost ${}".format(-user))
    left = chk_left_amt(left_amt)
    roll_two_die(left)


# ---------------------------------------------------------
# Call your game of chance functions here
flipping_a_coin()
