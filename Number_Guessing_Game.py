print("\nWelcome to the number guessing game!")
n = 18
t = 1
print("You have only 5 chances to guess.\n")
while t <= 5:
    g = int(input("Guess the hidden number:\n"))
    if g < n:
        print("Entered number is less than the hidden number\n""Try again!")
    elif g > n:
        print("Entered number is greater than the hidden number\n""Try again!")
    else:
        print("Congratulations, you've found the hidden number!\n")
        print(t,"no. of guesses taken to find the number!")
        break
    print(5 - t, "no. of guesses remaining!")
    t = t + 1
if t > 5:
    print("Game Over!")
