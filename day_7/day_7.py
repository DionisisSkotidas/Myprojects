import random
# ========== Set up ==========
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = len(stages)
current_stage = -1
word_list = ['patates']
chosen_word = random.choice(word_list)
length = len (chosen_word)
print(chosen_word)  # todo: del later
display = []
for letter in chosen_word:
    display += '_'
print(display)

print(stages[current_stage])
while True:
    guess = input("Choose a Letter\n").lower()
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = guess
                length -= 1
        print(display)
        if length == 0:
            print("CONGRATULATIONS\n"
                  "You WON !!!")

    else:
        current_stage -= 1
        lives -= 1
        print(stages[current_stage])
        print('Wrong guess you have {} guesses left'.format(lives))
        if lives == 0:
            print("There are no more guesses\n"
                  "You Lost :(\n"
                  "The answer was: {}".format(chosen_word))
            break


