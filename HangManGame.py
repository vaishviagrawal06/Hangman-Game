import random

print("🎮 Welcome to the Hangman Game!")

# level select karo
print("Select level of the game!")
print("1.Easy")
print("2.Medium")
print("3.Hard")

choice = input("Enter the LEVEL(1,2,3):-")

if choice not in ["1", "2", "3"]:
    choice = "2"

if choice == "1":
    word = [
        "chair","house","phone",
        "school","table","cat",
        "dog","bat","sun","pen","book",
        "fish","milk","tree","apple",
    ]

    chances = 7


elif choice == "2":
    word = [
        "program","science","college","student","language",
        "football","database","website","laptop",
    ]

    chances = 5


elif choice == "3":
    word = [
        "intelligence","communication","responsibility","architecture",
        "mathematics","environment","information","application",
    ]

    chances = 3

# random word choose karna hai
secret_word = random.choice(word)

# letters ki jagah underscore lagana haii
guessed_word = ["_"] * len(secret_word)
# letter store hoga
guessed_letter = []
# score is initialized by 0
score = 0


# random letters visible kar rahe hai
visible_letters = random.randint(1, len(secret_word) // 2)

random_index = random.sample(range(len(secret_word)), visible_letters)

for i in random_index:
    guessed_word[i] = secret_word[i]


# game loop
while chances > 0:
    print("\nWord:", " ".join(guessed_word))
    print("Chances left:", chances)
    print("Score:", score)

    print("Enter 'HINT' to get a letter hint (-5 points).")
    guess = input("Enter a letter: ").lower()
    
    # HINT SYSTEM
    if guess == "hint":
        
        if score<10:
            print("⚠️ You don't have enough score to use hint! ")
            continue

        hidden_index = []

        for i in range(len(secret_word)):
            if guessed_word[i] == "_":
                hidden_index.append(i)

        if hidden_index:

            reveal = random.choice(hidden_index)

            guessed_word[reveal] = secret_word[reveal]

            score = max(score - 5, 0)
            
            # ✅ Win condition after hint
            if "_" not in guessed_word:
                 print("\n🎉 Congratulations! You Won 🎉")
                 print("Word was:", secret_word)
            
                 score += 50
                 print("Final score:", score)
                 break


        continue

    # Already guessed check
    if guess in guessed_letter:
        print("🌟 Already guessed!")
        continue

    guessed_letter.append(guess)

    # Correct Guess
    if guess in secret_word:

        print("✅ Correct Guess!")
        score += 10

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess

    # Wrong Guess
    else:
        print("❌ Wrong Guess...score -5!")
        

        chances -= 1
        # score = max(score - 5, 0)
        score -= 5
        print("Score: ",score)

    # WIN CONDITION
    if "_" not in guessed_word:
        print("\n🎉 Congratulations!You Won🎉")
        print("Word was:", secret_word)


        score += 50
        print("Final score: ",score)
        break


if chances == 0:
    print("😔Game Over!")
    print("Original word was: ", secret_word)
    print("Final score: ", score)