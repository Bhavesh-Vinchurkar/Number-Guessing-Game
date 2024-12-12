import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
correct_number=random.randint(1,100)
chances=0
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty=='easy':
    chances=10
else:
    chances=5

while chances!=0:
    guessed_number=int(input("Make a guess: "))
    if guessed_number==correct_number:
        print("You guessed it right")
        break
    else:
        chances-=1
        if chances==0:
            print("Used all attempts. You Lose.")
        else:
            if guessed_number>correct_number:
                print("Too High")
            else:
                print("Too Low")
            print("Guess Again")
            print(f"You have {chances} attempts remaining: ")