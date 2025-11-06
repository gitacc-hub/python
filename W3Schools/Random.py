#Using random function
import random
"""
low=1
high=101
number=random.randint(low,high)
print(number)
"""

"""
options=("Rock","Papers","Scissors")
option=random.choice(options)
print(option)
"""

"""
dice=[1,2,3,4,5,6]
random.shuffle(dice)
print(dice)
"""





"""
1. random.random()

➡️ Returns a random float between 0.0 and 1.0
Use when you just need a simple random decimal.

random.random()  
# → 0.37444887175646646  
"""

"""
2. random.randint(a, b)

➡️ Returns a random integer between a and b (inclusive).
Perfect for dice rolls, random IDs, or picking an index.

random.randint(1, 6)  
# → 4
"""

"""
3. random.choice(seq)

➡️ Picks one random element from a list, tuple, or string.
Used when selecting a random item.

random.choice(['red', 'green', 'blue'])  
# → 'green'
"""

"""
4. random.choices(population, k=1)

➡️ Picks multiple random elements with replacement.
Useful when you can pick the same element more than once.

random.choices(['A', 'B', 'C'], k=5)  
# → ['B', 'A', 'C', 'C', 'A']
"""

"""
5. random.sample(population, k)

➡️ Picks k unique random elements (no duplicates).
Great for random teams or lottery draws.

random.sample(range(10), 3)  
# → [7, 2, 9]
"""

"""
6. random.shuffle(x)

➡️ Shuffles a list in place (changes its order randomly).
Perfect for shuffling cards or lists.

cards = ['A', 'K', 'Q', 'J']
random.shuffle(cards)
# → ['J', 'Q', 'A', 'K']
"""

"""
7. random.uniform(a, b)

➡️ Returns a random float between a and b.
Use when you need a random continuous value in a range.

random.uniform(10, 20)  
# → 14.872
"""

"""
8. random.randrange(start, stop, step)

➡️ Picks a random number from a range, like range(), but random.

random.randrange(0, 100, 10)
# → 30
"""

"""
9. random.seed(a=None)

➡️ Initializes the random number generator.
Use this when you want repeatable random results (for testing).

random.seed(42)
print(random.random())  # always the same output
"""



#Exerscise with random
"""
lowest_num=1
highest_num=101
answer=random.randint(lowest_num,highest_num)
guesses=0
is_running=True

print("Python number guessing game")
print(f"Select number between {lowest_num} and {highest_num}:")

while is_running:
    guess=input("Enter your guess: ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1

        if guess>highest_num or guess<lowest_num:
            print(f"{guess} is out of range.")
            print(f"Enter a number between {lowest_num} and {highest_num}")
        elif guess>answer:
            print(f"{guess} is too high.")
        elif guess<answer:
            print(f"{guess} is too low.")
        else:
            print(f"{guess} is correct.You took {guesses} trials to get it right.")
            is_running=False

    else:
        print(f"{guess} is invalid.")
        print(f"Enter a number between {lowest_num} and {highest_num}")
"""

#Rock paper Scissor Game

"""
options=("Rock","Paper","Scissors")
playing=True

while playing:
    player=None
    Computer=random.choice(options)
    while player not in options:
        player=input("Enter your choice: (Rock,Paper,Scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {Computer}")

    if player==Computer:
        print("Its a tie.")
    elif player=="Rock" and Computer=="Scissors":
        print("You win")
    elif player=="Paper" and Computer=="Rock":
        print("You win") 
    elif player=="Scissors" and Computer=="Paper":
        print("You win")   
    else:
        print("You lose")
    
    if not input("Play again (y/n): ").lower()=="y":
        playing=False
    
print("Thanks for playing")
"""

#● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art={
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│ ●       │",
       "│         │",
       "│       ● │",
       "└─────────┘"),
    3:("┌─────────┐",
       "│ ●       │",
       "│    ●    │",
       "│       ● │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└─────────┘")
    
}
dice=[]
total=0
num_dice=int(input("How many dice? "))

for die in range(num_dice):
    dice.append(random.randint(1,6))
print(dice)