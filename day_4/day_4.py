import random


def rock_paper_scissors():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    game_images = [rock, paper, scissors]
    print('welcome to Rock, Paper, Scissors')
    player_points = 0
    computer_points = 0
    computer = 0
    score = input('would you like to keep score?\n'
                  'If so Type YES \n'
                  'if not press any other key\n').upper()
    while True:
        player = int(input('What do you choose?\n'
                           'Type: \n'
                           '0 for Rock,\n'
                           '1 for Paper,\n'
                           '2 for Scissors,\n'
                           '3 to exit\n'))
        if player == 3:
            print("Thanks for playing")
            break
        if player in range(0, 4):
            print("you chose {}".format(game_images[player]))

            computer = random.randint(0, 2)
            print("Computer chose {}".format(game_images[computer]))

        if player == 0:  # player chooses rock
            if computer == 0:
                print('Tie')
            elif computer == 1:
                print("You Loose")
                computer_points += 1
            else:
                print("You Win")
                player_points += 1
        elif player == 1:  # players chooses paper
            if computer == 0:
                print("You Win")
                player_points += 1
            elif computer == 1:
                print("It's a Tie")
            else:
                print('You Loose')
                computer_points += 1
        elif player == 2: # player chooses scissors
            if computer == 0:
                print('You loose')
                computer_points += 1
            elif computer == 1:
                print("You Win")
                player_points += 1
            else:
                print("It's a Tie")
        else:
            print("Please try to enter a valid number ")
            rock_paper_scissors()
        if score == 'YES':
            print("PLAYER : {} \n"
                  "COMPUTER : {}".format(player_points, computer_points))


rock_paper_scissors()

