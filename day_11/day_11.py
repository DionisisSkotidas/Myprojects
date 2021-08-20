import random

cards = {
    'Ace': 11,
    # '2': 2,
    # '3': 3,
    # '4': 4,
    '5': 5,
    # '6': 6,
    # '7': 7,
    # '8': 8,
    # '9': 9,
    # '10': 10,
    # 'Jack': 10,
    # 'Queen': 10,
    # 'King': 10
}

player_hand = []
player_score = 0


computer_hand = []
computer_score = 0

counter = False


def deal(who_hand, who_score):
    global counter
    if who_score < 21:
        cards['Ace'] = 11
    else:
        cards['Ace'] = 1
    card, value = random.choice(list(cards.items()))
    who_hand.append(card)
    new_score = who_score + value
    if not counter:
        if 'Ace' in who_hand:
            new_score -= 10
            counter = True
    return new_score


def win(name):
    print(f'{name} Wins')


def intro(who, hand, score):
    print(f'{who }'
          f'Hand : {hand}\n'
          f'\t\t\t Score: {score}')
    print()


#  ====== START OF THE GAME ======
for i in range(2):
    player_score = deal(player_hand, player_score)
    computer_score = deal(computer_hand, computer_score)

intro('player', player_hand, player_score)
intro("Dealer", computer_hand, computer_score)


# ====== PLAYER'S TURN ======
turn = 'PLAYER'
game = True
while game:
    if turn == 'PLAYER':
        another_one = input('DJ KHALID?\n'
                            'If so type y : \n'
                            'If not so type no : \n').lower()
        if another_one == 'y':
            player_score = deal(player_hand, player_score)
            intro('player', player_hand, player_score)
            if player_score > 21:
                print("Sory m8 you got one to far")
                win('computer')
                game = False
        elif another_one == 'no':
            turn = 'COMPUTER'
        else:
            print('Please give me a valid answer')

# ====== COMPUTER'S TURN ======
    if turn == 'COMPUTER':
        while computer_score < 17:
            computer_score = deal(computer_hand, computer_score)
            intro("Dealer", computer_hand, computer_score)
            if computer_score > 21:
                win('player')
                game = False
                break
            if computer_score > 17:
                game = False


# ====== END ======
if 21 > player_score > computer_score:
    win('Player')
elif player_score == computer_score:
    print('Draw')
elif 21 > computer_score > player_score:
    win('Dealer')
