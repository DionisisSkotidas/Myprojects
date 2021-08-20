import random

print('Ello mate')

number = 0
lives = 0
while lives == 0:
    difficulty = input('Choose a difficulty. Type "easy" or "normal" or "hard"').lower()
    if difficulty == "easy":
        lives = 10
        number = random.randint(0, 50)
    elif difficulty == "normal":
        lives = 5
        number = random.randint(0, 50)
    elif difficulty == 'hard':
        lives = 5
        number = random.randint(0, 100)
    else:
        print('please choose on of the difficulty levels displayed')

print(lives)
print(number)
guess = int(input('Make a guess :'))

while guess != number and lives > 0:
    if guess > number + 10:
        print('Your guess was too high')
        lives -= 1
    elif guess > number:
        print('Your guess was too high')
        lives -= 1
    elif guess < number - 10:
        print("Your guess was too low")
        lives -= 1
    elif guess < number:
        print("Your guess was low ")
        lives -= 1
    guess = int(input('Make a guess :'))

if guess == number:
    print("Congratulations you found it")
else:
    print("I'm sorry you didn't find it \n"
          "Maybe next time")