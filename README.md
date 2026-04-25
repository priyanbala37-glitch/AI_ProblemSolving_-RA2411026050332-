# AI Problem Solving — Problem 1: Interactive Tic-Tac-Toe AI

🔗 **Live Demo:** https://ai-problemsolving-ra2411026050332.onrender.com/  
📁 **GitHub:** https://github.com/priyanbala37-glitch/AI_ProblemSolving_-RA2411026050332-

---

## Problem Description
A web-based Tic-Tac-Toe game where a human plays against an AI that **never loses**.
The AI uses two adversarial search algorithms and compares their performance in real time.

---

## Folder Structure
AI_ProblemSolving_-RA2411026050332-/
│
├── README.md
├── .gitignore
│
└── Problem1_TicTacToe/
├── app.py
├── requirements.txt
└── templates/
└── index.html
---

## Algorithms Used

### 1. Minimax
- Explores **every possible game state** recursively
- Scores: +10 (AI wins), -10 (Human wins), 0 (Draw)
- Worst case: 9! = 362,880 nodes on empty board
- Guarantees optimal play but slow on early moves

### 2. Alpha-Beta Pruning
- Optimised version of Minimax
- Maintains α (best for maximiser) and β (best for minimiser)
- Prunes branches that cannot affect the final decision
- Same accuracy as Minimax but ~97% fewer nodes explored

---

## Execution Steps

### Run Locally
```bash
# Step 1 - Install dependencies
pip install -r requirements.txt

# Step 2 - Navigate to project folder
cd Problem1_TicTacToe

# Step 3 - Start the server
python app.py

# Step 4 - Open in browser
http://127.0.0.1:5000

### Or visit the Live Demo directly:
https://ai-problemsolving-ra2411026050332.onrender.com/

## Sample Output

### Single AI Move (Alpha-Beta)
Algorithm  : α-β
Nodes      : 59
Time       : 0.31 ms
### Algorithm Comparison (empty board)
Minimax    : 549,945 nodes  |  312.4 ms
Alpha-Beta :  18,297 nodes  |   10.8 ms
Result     : α-β pruned 97% of nodes (531,648 states saved)

---

## Features
- 🎮 Interactive web-based game board
- 🧠 AI never loses (perfect play guaranteed)
- ⚡ Switch between Minimax and Alpha-Beta live
- 📊 Real-time stats — nodes explored and time taken
- 🔄 Compare both algorithms side by side
- 🏆 Score tracker for Human vs AI

---

## Author
- **Name:** SRI BALA PRIYAN S
- **Register Number:** RA2411026050332