# 🎯 Hangman Game — Python Console Edition

<div align="center">

> **A fully-featured, console-based Hangman game built in Python — with difficulty levels, hints, and a live score tracker!**

</div>

---

## 📖 Project Overview

**Hangman Game** is a classic word-guessing game implemented entirely in Python. The player tries to guess a hidden word one letter at a time before running out of chances. This project goes beyond the basics — it features **3 difficulty levels**, a **hint system**, a **dynamic score tracker**, and smart logic to keep the game fair and fun.

Whether you're a beginner looking to learn Python fundamentals or someone who wants a fun CLI game to play, this project has something for you!

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎮 **3 Difficulty Levels** | Easy, Medium, and Hard — each with unique word sets and chance counts |
| 🎲 **Random Word Selection** | Words are randomly picked using Python's `random` module |
| 💡 **Hint System** | Type `HINT` to reveal a hidden letter (costs 10 score points) |
| 🏆 **Score System** | Dynamic scoring for correct guesses, wrong guesses, hints, and winning |
| 👁️ **Pre-revealed Letters** | Some letters are visible at the start to make the game approachable |
| 🚫 **Repeat Guard** | Prevents the player from guessing the same letter twice |
| 🏁 **Win / Game Over Logic** | Clear win and lose conditions with final score display |

---

## 🎮 Gameplay Explanation

1. **Choose a difficulty level** — Easy, Medium, or Hard
2. A **random word** is selected from the corresponding word set
3. The word is displayed as underscores `_ _ _ _`, with a few letters **pre-revealed**
4. Each turn, you either:
   - **Type a letter** to guess it
   - **Type `HINT`** to reveal one hidden letter (costs points)
5. Correct guesses reveal the letter in the word ✅
6. Wrong guesses reduce your remaining chances ❌
7. The game ends when:
   - ✅ You guess the entire word — **You Win!**
   - ❌ You run out of chances — **Game Over!**

---

## 🎚️ Difficulty Levels

| Difficulty | Chances | Word Complexity | Pre-revealed Letters |
|:---:|:---:|:---:|:---:|
| 🟢 **Easy** | 7 | Short, common words | More letters shown |
| 🟡 **Medium** | 5 | Moderate vocabulary | Some letters shown |
| 🔴 **Hard** | 3 | Long or tricky words | Fewer letters shown |

---

## 🏆 Scoring System

| Action | Score Change |
|:---:|:---:|
| ✅ Correct letter guess | `+10` points |
| ❌ Wrong letter guess | `-5` points |
| 💡 Using a hint | `-10` points |
| 🎉 Winning the game | `+50` bonus points |

> 💬 **Tip:** Try to win without hints for the highest possible score!

---

## 🚀 Installation & How to Run

### Prerequisites

Make sure you have **Python 3** installed on your machine.

```bash
python --version
# Should output: Python 3.x.x
```

### Step 1 — Clone the Repository

```bash
https://github.com/vaishviagrawal06/Hangman-Game.git
```

### Step 2 — Navigate to the Project Folder

```bash
cd hangman-game
```

### Step 3 — Run the Game

```bash
python hangman.py
```

> ✅ No external libraries required — only Python's built-in `random` module is used!

---

## 🗂️ Code Structure & Logic Explanation

```
hangman-game/
│
├── hangman.py          # Main game file — all logic lives here
└── README.md           # Project documentation
```

### 🔧 Core Logic Breakdown

```
hangman.py
│
├── 📦 Word Banks
│   ├── easy_words[]      → Short words (e.g., "cat", "sun", "dog")
│   ├── medium_words[]    → Mid-length words (e.g., "planet", "rocket")
│   └── hard_words[]      → Complex words (e.g., "mysterious", "algorithm")
│
├── ⚙️ Game Setup
│   ├── select_difficulty()     → Prompts user and returns word list + chances
│   ├── random.choice()         → Picks a random word from the selected list
│   └── reveal_random_letters() → Pre-reveals a few letters for the player
│
├── 🔄 Game Loop
│   ├── display_word()          → Shows current guessed state (e.g., _ a _ _ _ n)
│   ├── get_player_input()      → Handles letter input or "HINT" command
│   ├── check_guess()           → Validates guess and updates game state
│   └── update_score()          → Applies score changes based on action
│
└── 🏁 End Conditions
    ├── check_win()             → Returns True if all letters are revealed
    └── check_loss()            → Returns True if chances reach 0
```

---

## 🖥️ Example Gameplay Output

```
========================================
        🎯 WELCOME TO HANGMAN GAME
========================================

Select Difficulty:
  [1] 🟢 Easy   (7 chances)
  [2] 🟡 Medium (5 chances)
  [3] 🔴 Hard   (3 chances)

Enter choice: 2

🔤 Word: _ _ a _ e _
❤️  Chances left: 5  |  🏆 Score: 0

Enter a letter (or HINT): t

✅ Nice! 't' is in the word.

🔤 Word: _ _ a _ e t
❤️  Chances left: 5  |  🏆 Score: 10

Enter a letter (or HINT): HINT

💡 Hint used! Revealing a letter... (-10 points)

🔤 Word: p _ a _ e t
❤️  Chances left: 5  |  🏆 Score: 0

Enter a letter (or HINT): l

✅ Nice! 'l' is in the word.

🔤 Word: p l a _ e t
❤️  Chances left: 5  |  🏆 Score: 10

Enter a letter (or HINT): n

✅ Nice! 'n' is in the word.

🔤 Word: p l a n e t
🎉 You Win! The word was: PLANET
🏆 Final Score: 60  (includes +50 win bonus!)
========================================
```

---

## 🔮 Future Improvements

- [ ] 🖼️ Add ASCII art for the hangman figure (visually show remaining chances)
- [ ] 📂 Add multiple word categories (Animals, Countries, Movies, etc.)
- [ ] 💾 Add a high-score leaderboard saved to a `.txt` or `.json` file
- [ ] 🌐 Build a GUI version using `tkinter` or `pygame`
- [ ] ⏱️ Add a timer to increase the challenge
- [ ] 🔠 Support multi-word phrases as hidden answers
- [ ] 🌍 Add multi-language word support

---
<!-- 
## 📚 Learning Outcomes

By building and exploring this project, you will learn:

- ✅ How to use **Python lists** to store and manage word banks
- ✅ Working with the **`random` module** (`random.choice`, `random.sample`)
- ✅ Writing clean **game loops** using `while` statements
- ✅ Handling **user input validation** and edge cases
- ✅ Implementing a **scoring system** with conditional logic
- ✅ Structuring a Python project into logical **functions**
- ✅ Using **string manipulation** to display partially revealed words
- ✅ Understanding **win/lose conditions** in game logic

--- -->

## 👤 Author

<div align="center">

**Made with ❤️ by [Vaishvi Agrawal]**

[![GitHub](https://img.shields.io/badge/GitHub-vaishviagrawal06-181717?style=for-the-badge&logo=github)](https://github.com/vaishviagrawal06)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/vaishvi-agrawal-792407331/)

</div>

---

<div align="center">

⭐ **If you enjoyed this project, please give it a star!** ⭐

*Happy Coding & Happy Guessing! 🎯*

</div>
