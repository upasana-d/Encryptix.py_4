import random

def play():
    game = ['rock', 'paper', 'scissors']
    computer = random.choice(game)
    return computer

def get_user_choice():
    while True:
        user = input("Enter you choice (ROCK, PAPER, SCISSORS):\n").lower()
        if user in ['rock', 'paper', 'scissors']:
            return user
        else:
            print("Invalid input. Please choose among Rock, Paper or Scissors.")

def winner(user,computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "Yayyy!!! You win!!!"
    else:
        return "Oops! You lost.Try again!!"


def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = play()
        print(f"Computer Choice : {computer_choice}")

        result = winner(user_choice, computer_choice)
        print(result)

        if "Yayyy!!! You win!!!" in result:
            user_score += 1
        elif "Oops! You lost.Try again!!" in result:
            computer_score += 1


        print(f"""-----------------SCORE------------------
              YOU : {user_score}
              COMPUTER : {computer_score}""")
        

        play_again = input("Do you want to play again> (Y/N) : ").lower()

        if play_again != 'y':
            break

    print("""------------------------THANK YOU FOR PLAYING---------------------
          ____________HOPE YOU ENJOYED THE GAME____________""")
    

if  __name__ == "__main__":
    main()



