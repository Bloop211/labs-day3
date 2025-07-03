while True:
    from random import randint
    random_number = randint(1, 100)
    guess = input("Guess a number between 1 and 100: ")
    guess = int(guess)
    guesses = 1
    print(random_number)

    while guess != random_number:
        if guess < random_number:
            print("Too low!")
            guesses += 1
        elif guess > random_number:
            print("Too high!")
            guesses += 1
        guess = input("Guess again: ")
        guess = int(guess)
    if guess == random_number:
        print(f"You guessed the number in {guesses} guesses!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            best_score = guesses
            if best_score < best_score:
                best_score = guesses
            print(f"Your best score is {best_score}")
            continue
        else:
            best_score = guesses
            if best_score < best_score:
                best_score = guesses
            print(f"Your best score is {best_score}")
            break
    

    
        