2025-12-12 21:45

Status: Complete

Tags: 


# Higher or Lower

## Todo: Program Logic
> # Display two random personalities from the dictionary and ask user to choose one with higher number of followers  
#Compare the number of followers of the two personality  
#If user gets it right, score++, if wrong, wrong and display their score.  
#If they're right, choose a new user and compare them to the right user from the previous comparison,  
#keep looping till user gets one wrong.

## Code: Project Code

main.py
```
from random import choice  
from art import logo, vs  
from game_data import data  
  
# Display art  
print(logo)  
game_active = True  
score = 0  
  
def get_person():  
    # Get a personality's data from the database  
    return choice(data)  
  
# Generate 2 random persons  
person_A = get_person()  
person_B = get_person()  
  
# Make sure same person is picked twice  
if person_A == person_B:  
    person_B = get_person()  
  
# Compare the follower counts for the two personalities.  
# returns a list: [the letter for the personality with bigger follower count, the personality]  
def check_follower_count(person_1, person_2):  
    if person_1['follower_count'] > person_2['follower_count']:  
        return ['A', person_1]  
    else:  
        return ['B', person_2]  
  
# Ask user which personality has more followers  
def user_choice():  
    print(f"Compare A: {person_A['name']}, {person_A['description']}, from {person_A['country']}")  
    print(vs)  
    print(f"Against B: {person_B['name']}, {person_B['description']}, from {person_B['country']}")  
    a_or_b = input("Who has more followers? Type 'A' or 'B': ")  
  
    return a_or_b  
  
# Play game  
while game_active:  
    follower_count = check_follower_count(person_A, person_B)  
    chose = user_choice()  
    if chose == follower_count[0]:  
        score += 1  
        print(f"You're right! Current score: {score}")  
        person_A = follower_count[1]  
        person_B = get_person()  
    else:  
        print(f"Sorry, that's wrong. Final score: {score}")  
        game_active = False
```


art.py
```
logo = r"""  
    __  ___       __   / / / (_)___ _/ /_  ___  _____  
  / /_/ / / __ `/ __ \/ _ \/ ___/ / __  / / /_/ / / / /  __/ /    /_/ ///_/\__, /_/ /_/\___/_/       
   / /  /____/_      _____  _____  
  / /   / __ \ | /| / / _ \/ ___/ / /___/ /_/ / |/ |/ /  __/ /    /_____/\____/|__/|__/\___/_/     """  
  
vs = r"""  
 _    __    | |  / /____  
| | / / ___/  
| |/ (__  ) |___/____(_)  
"""
```

game_data.py
```
data = [  
    {  
        'name': 'Instagram',  
        'follower_count': 346,  
        'description': 'Social media platform',  
        'country': 'United States'  
    },  
    {  
        'name': 'Cristiano Ronaldo',  
        'follower_count': 215,  
        'description': 'Footballer',  
        'country': 'Portugal'  
    },  
    {  
        'name': 'Ariana Grande',  
        'follower_count': 183,  
        'description': 'Musician and actress',  
        'country': 'United States'  
    },  
    {  
        'name': 'Dwayne Johnson',  
        'follower_count': 181,  
        'description': 'Actor and professional wrestler',  
        'country': 'United States'  
    },  
    {  
        'name': 'Selena Gomez',  
        'follower_count': 174,  
        'description': 'Musician and actress',  
        'country': 'United States'  
    },  
    {  
        'name': 'Kylie Jenner',  
        'follower_count': 172,  
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',  
        'country': 'United States'  
    },  
    {  
        'name': 'Kim Kardashian',  
        'follower_count': 167,  
        'description': 'Reality TV personality and businesswoman',  
        'country': 'United States'  
    },  
    {  
        'name': 'Lionel Messi',  
        'follower_count': 149,  
        'description': 'Footballer',  
        'country': 'Argentina'  
    },  
    {  
        'name': 'Beyoncé',  
        'follower_count': 145,  
        'description': 'Musician',  
        'country': 'United States'  
    },  
    {  
        'name': 'Neymar',  
        'follower_count': 138,  
        'description': 'Footballer',  
        'country': 'Brasil'  
    },  
    {  
        'name': 'National Geographic',  
        'follower_count': 135,  
        'description': 'Magazine',  
        'country': 'United States'  
    },  
    {  
        'name': 'Justin Bieber',  
        'follower_count': 133,  
        'description': 'Musician',  
        'country': 'Canada'  
    },  
    {  
        'name': 'Taylor Swift',  
        'follower_count': 131,  
        'description': 'Musician',  
        'country': 'United States'  
    },  
    {  
        'name': 'Kendall Jenner',  
        'follower_count': 127,  
        'description': 'Reality TV personality and Model',  
        'country': 'United States'  
    },  
    {  
        'name': 'Jennifer Lopez',  
        'follower_count': 119,  
        'description': 'Musician and actress',  
        'country': 'United States'  
    },  
    {  
        'name': 'Nicki Minaj',  
        'follower_count': 113,  
        'description': 'Musician',  
        'country': 'Trinidad and Tobago'  
    },  
    {  
        'name': 'Nike',  
        'follower_count': 109,  
        'description': 'Sportswear multinational',  
        'country': 'United States'  
    },  
    {  
        'name': 'Khloé Kardashian',  
        'follower_count': 108,  
        'description': 'Reality TV personality and businesswoman',  
        'country': 'United States'  
    },  
    {  
        'name': 'Miley Cyrus',  
        'follower_count': 107,  
        'description': 'Musician and actress',  
        'country': 'United States'  
    },  
    {  
        'name': 'Katy Perry',  
        'follower_count': 94,  
        'description': 'Musician',  
        'country': 'United States'  
    },  
    {  
        'name': 'Kourtney Kardashian',  
        'follower_count': 90,  
        'description': 'Reality TV personality',  
        'country': 'United States'  
    },  
    {  
        'name': 'Kevin Hart',  
        'follower_count': 89,  
        'description': 'Comedian and actor',  
        'country': 'United States'  
    },  
    {  
        'name': 'Ellen DeGeneres',  
        'follower_count': 87,  
        'description': 'Comedian',  
        'country': 'United States'  
    },  
    {  
        'name': 'Real Madrid CF',  
        'follower_count': 86,  
        'description': 'Football club',  
        'country': 'Spain'  
    },  
    {  
        'name': 'FC Barcelona',  
        'follower_count': 85,  
        'description': 'Football club',  
        'country': 'Spain'  
    },  
    {  
        'name': 'Rihanna',  
        'follower_count': 81,  
        'description': 'Musician and businesswoman',  
        'country': 'Barbados'  
    },  
    {  
        'name': 'Demi Lovato',  
        'follower_count': 80,  
        'description': 'Musician and actress',  
        'country': 'United States'  
    },  
    {  
        'name': "Victoria's Secret",  
        'follower_count': 69,  
        'description': 'Lingerie brand',  
        'country': 'United States'  
    },  
    {  
        'name': 'Zendaya',  
        'follower_count': 68,  
        'description': 'Actress and musician',  
        'country': 'United States'  
    },  
    {  
        'name': 'Shakira',  
        'follower_count': 66,  
        'description': 'Musician',  
        'country': 'Colombia'  
    },  
    {  
        'name': 'Drake',  
        'follower_count': 65,  
        'description': 'Musician',  
        'country': 'Canada'  
    },  
    {  
        'name': 'Chris Brown',  
        'follower_count': 64,  
        'description': 'Musician',  
        'country': 'United States'  
    },  
    {  
        'name': 'LeBron James',  
        'follower_count': 63,  
        'description': 'Basketball player',  
        'country': 'United States'  
    },  
    {  
        'name': 'Vin Diesel',  
        'follower_count': 62,  
        'description': 'Actor',  
        'country': 'United States'  
    },  
    {  
        'name': 'Cardi B',  
        'follower_count': 67,  
        'description': 'Musician',  
        'country': 'United States'  
    },  
    {  
        'name': 'David Beckham',  
        'follower_count': 82,  
        'description': 'Footballer',  
        'country': 'United Kingdom'  
    },  
    {  
        'name': 'Billie Eilish',  
        'follower_count': 61,  
        'description': 'Musician',  
        'country': 'United States'  
    },  
    {  
        'name': 'Justin Timberlake',  
        'follower_count': 59,  
        'description': 'Musician and actor',  
        'country': 'United States'  
    },  
    {  
        'name': 'UEFA Champions League',  
        'follower_count': 58,  
        'description': 'Club football competition',  
        'country': 'Europe'  
    },  
    {  
        'name': 'NASA',  
        'follower_count': 56,  
        'description': 'Space agency',  
        'country': 'United States'  
    },  
    {  
        'name': 'Emma Watson',  
        'follower_count': 56,  
        'description': 'Actress',  
        'country': 'United Kingdom'  
    },  
    {  
        'name': 'Shawn Mendes',  
        'follower_count': 57,  
        'description': 'Musician',  
        'country': 'Canada'  
    },  
    {  
        'name': 'Virat Kohli',  
        'follower_count': 55,  
        'description': 'Cricketer',  
        'country': 'India'  
    },  
    {  
        'name': 'Gigi Hadid',  
        'follower_count': 54,  
        'description': 'Model',  
        'country': 'United States'  
    },  
    {  
        'name': 'Priyanka Chopra Jonas',  
        'follower_count': 53,  
        'description': 'Actress and musician',  
        'country': 'India'  
    },  
    {  
        'name': '9GAG',  
        'follower_count': 52,  
        'description': 'Social media platform',  
        'country': 'China'  
    },  
    {  
        'name': 'Ronaldinho',  
        'follower_count': 51,  
        'description': 'Footballer',  
        'country': 'Brasil'  
    },  
    {  
        'name': 'Maluma',  
        'follower_count': 50,  
        'description': 'Musician',  
        'country': 'Colombia'  
    },  
    {  
        'name': 'Camila Cabello',  
        'follower_count': 49,  
        'description': 'Musician',  
        'country': 'Cuba'  
    },  
    {  
        'name': 'NBA',  
        'follower_count': 47,  
        'description': 'Club Basketball Competition',  
        'country': 'United States'  
    }  
]
```

## References

