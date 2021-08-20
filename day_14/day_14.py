import random

# ====== DICTIONARY FOR THE GAME ======
#   THE ENTRIES FOR THE DICTIONARY WILL CONTAIN :
#         1) THE NAME OF THE PERSON
#         2) THAT PERSON'S FOLLOWER COUNT(in millions)
#         3) WHAT HE DOES
#         4) AND THE COUNTRY THAT HE ORIGINATES

data = [
    {
        'name': "Kendall Jenner",
        'follower_count': "156",
        'description': "Victoria Secret Runaway Model",
        'country': "USA"
    },
    {
        'name': "Justin Bieber",
        'follower_count': "168",
        'description': "Pop star",
        'country': "Canada"
    },
    {
        'name': "Beyoncé",
        'follower_count': "170",
        'description': "Pop Star",
        'country': "Houston Texas"
    },
    {
        'name': "Lionel Messi",
        'follower_count': "193",
        'description': "Football player",
        'country': "Argentina"
    },
    {
        'name': "Kim Kardashian",
        'follower_count': "211",
        'description': "Instagram influencer",
        'country': "Los Angeles, California"
    },
    {
        'name': "Selena Gomez",
        'follower_count': "218",
        'description': "Pop Star",
        'country': "Grand Prairie, Texas"
    },
    {
        'name': "Kylie Jenner",
        'follower_count': "222",
        'description': "Instagram influencer",
        'country': "Los Angeles, California"
    },
    {
        'name': "Dwayne 'The Rock' Johnson",
        'follower_count': "225",
        'description': "Actor, Bodybuilder",
        'country': "Hayward, California"
    },
    {
        'name': "Ariana Grande",
        'follower_count': "228",
        'description': "Pop Star",
        'country': "Boca Raton, Florida"
    },
    {
        'name': "Cristiano Ronaldo",
        'follower_count': "272",
        'description': "Football player",
        'country': "Portugal"
    }
]

#  ====== ASCII ART ======
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


# ====== FUNCTIONS ======
def choose_celebrity(agenda):
    data_dict = random.choice(agenda)
    celebrity = data_dict.get('name')
    followers = data_dict.get('follower_count')
    job = data_dict.get('description')
    country = data_dict.get('country')
    agenda.remove(data_dict)
    print(f'{celebrity} : {job} from {country}\n')
    return celebrity, followers


def most_followers(c_1, f_1, c_2, f_2):
    if f_1 > f_2:
        return 1, c_1, f_1

    if f_2 > f_1:
        return 2, c_2, f_2


def choosing_phase(w_c=None, w_f=None):
    global score
    if not w_c:
        celebrity_1, celeb_1_follow = choose_celebrity(data)
    else:
        celebrity_1, celeb_1_follow = w_c, w_f
    celebrity_2, celeb_2_follow = choose_celebrity(data)
    evaluation, win_c, win_f = most_followers(celebrity_1, celeb_1_follow, celebrity_2, celeb_2_follow)
    player = int(input('Who dou you think has the most followers?\n'
                       f'Type 1 for {celebrity_1}\n'
                       f'or \n'
                       f'Type 2 for {celebrity_2}\n'))
    while len(data) > 0:
        if player == evaluation:
            print('nice')
            score += 1
            choosing_phase(win_c, win_f)
            print(score)
        else:
            print('SoRry m8 you lost')
            print(f'Score : {score}')
    print("The Game is now over!\n"
          "Did you have Fun?")
    print(score)


# ====== GREETING ======
score = 0
print(logo)
greeting_message = 'Hello dear player and welcome to my humble game\n' \
                   'The rules are simple:\n' \
                   'I give you two celebrities.\n' \
                   'Then you will have to choose which one has more followers on Instagram\n' \
                   'If you get it right you move on to the next one if you loose you loose.\n' \
                   'HAVE FUN\n'
print(greeting_message)

choosing_phase()
