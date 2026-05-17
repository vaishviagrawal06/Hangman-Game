import random

print("Welcom to Hangman Game!")

# difficulty level choose karna hai

print("\n choose difficulty level!")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("ENTER CHOICE (1/2/3): ")

if choice=="1":
     words = ["cat", "dog", "bat", "sun"]
     chances = 8
elif choice == "2":
     words = ["python", "coding", "laptop"]
     chances = 6
    
elif choice=="3":
    words = ["developer", "algorithm", "javascript"]
    chances = 4

else:
    print("Invalid choice! Medium selected.")
    words = ["python", "coding", "laptop"]
    chances = 6
    
# random word choose
secret_word = random.choice(words)

# letters = list(secret_word)
# random.shuffle(letters)

# print("\nHint Letters:", " ".join(letters))

# letters ki jagah underscore lagana 
guessed_word=["_"]*len(secret_word)

guessed_letters = []

score=0

while chances>0:
    print("\nWord:"," ".join(guessed_word))
    print("chances left: ",chances)
    print("score: ",score)
    
    guess=input("enter a letter: ").lower() 
    #lower: Return a copy of the string converted to lowercase.
    if guess in guessed_letters:
        print("Already guessed!")
        continue
    
    guessed_letters.append(guess)
    
    if guess in secret_word:
        print("\n ✅Correct Guess!")
        
        score +=10
        
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i]=guess 
                
    else:
        print("\n ❌Wrong guess")
        chances -=1
        score-=5
        
    if "_" not in guessed_word:
        print("\n🎉Congratulations! You Won")
        print("Word was: ",secret_word)
        
        score+=50
        
        print("Final score: ",score)
        break
    

if "_" in guessed_word:
    print("😔Game over!")
    print("Correct word was: ",secret_word)
    print("Your Final Score: ",score)
    
    

    