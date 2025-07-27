# 🧠 Quiz App

A terminal-based Python quiz application that lets users test their knowledge through multiple-choice questions. The game tracks the user’s score, measures the time taken to complete the quiz, and stores the results in a local leaderboard file.

---

## 🚀 Features

- Multiple-choice questions loaded dynamically from a JSON file  
- Questions appear in random order for each game session  
- Score tracking with percentage calculation  
- Timer to measure total time taken by each user  
- Option to save user’s name, score, and time  
- Leaderboard stored locally in JSON and sorted by score  
- Visual feedback using ✅ for correct and ❌ for incorrect answers  
- Game ends instantly upon a wrong answer  
- Case-insensitive input handling (A/B/C/D or a/b/c/d)  
- Clean, formatted terminal output for better UX  
- Basic input validation to prevent crashes from invalid input  

---

## ⚙️ How to Run

Make sure Python 3 is installed on your system. Then run the app with:

```bash
python3 quiz_app/main.py
quiz_app/
├── main.py              # Core logic for the quiz flow and UI
├── leaderboard.py       # Leaderboard functions (save, load, sort)
├── questions.json       # Stores quiz questions and multiple-choice options
├── leaderboard.json     # Stores saved scores, names, and time data
