import random

# create the lists
symbols = '! @ # $ % ^ & * ( )  - _ = + '
letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
password_list = []

numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 10
letters_list = letters.split()   # 26
symbols_list = symbols.split()  # 10

# ========= Password details =========

nr_letters = int(input('How many letters would you like to be in your password?\n'))
nr_symbols = int(input("How many symbols?\n"))
nr_numbers = int(input("How many numbers\n"))

# ========= Letters =========
for i in range(random.randint(0, 8)):
    ran_index = random.randint(0, 25)
    caps = random.randint(0, 1)
    if caps:
        password_list.append(letters_list[ran_index].upper())
    else:
        password_list.append(letters_list[ran_index])

# ========= Symbols  =========
for j in range(random.randint(0, 8)):
    ran_index = random.randint(0, 7)
    password_list.append(symbols_list[ran_index])

# ========= Numbers =========
for k in range(random.randint(0, 8)):
    ran_index = random.randint(0, 9)
    password_list.append(str(numbers_list[ran_index]))

print(password_list)
password = ''

for p in range(len(password_list)):
    index = len(password_list)
    ran_index = random.randint(0, index-1)
    password += password_list[ran_index]
    password_list.pop(ran_index)

print(password)