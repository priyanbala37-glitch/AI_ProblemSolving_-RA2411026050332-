# AI Problem Solving - RA2411026050332

Live Projects:
- Problem 1 - Tic-Tac-Toe AI: https://ai-problemsolving-ra2411026050332.onrender.com/
- Problem 6 - Sudoku CSP Solver: https://sudoku-csp-solver.onrender.com/

GitHub: https://github.com/priyanbala37-glitch/AI_ProblemSolving_-RA2411026050332-

---

## Problem 1: Interactive Tic-Tac-Toe AI

Live Demo: https://ai-problemsolving-ra2411026050332.onrender.com/

### Problem Description
A web-based Tic-Tac-Toe game where a human plays against an AI that never loses.
The AI uses two adversarial search algorithms and compares their performance in real time.

### Folder Structure
Problem1_TicTacToe/
|-- app.py
|-- requirements.txt
|-- templates/
    |-- index.html

### Algorithms Used
1. Minimax
   - Explores every possible game state recursively
   - Scores: +10 (AI wins), -10 (Human wins), 0 (Draw)
   - Worst case: 9! = 362,880 nodes on empty board

2. Alpha-Beta Pruning
   - Optimised version of Minimax
   - Prunes branches that cannot affect the final decision
   - Same accuracy as Minimax but 97% fewer nodes explored

### Execution Steps
    pip install -r requirements.txt
    cd Problem1_TicTacToe
    python app.py
    Open: http://localhost:5000

### Sample Output
    Algorithm  : Alpha-Beta
    Nodes      : 59
    Time       : 0.31 ms

    Minimax    : 549,945 nodes  |  312.4 ms
    Alpha-Beta :  18,297 nodes  |   10.8 ms
    Result     : Alpha-Beta pruned 97% of nodes

---

## Problem 6: Sudoku CSP Solver

Live Demo: https://sudoku-csp-solver.onrender.com/

### Problem Description
Interactive Sudoku game where the user solves puzzles validated by
a CSP (Constraint Satisfaction Problem) engine with backtracking
and MRV heuristic. Displays You Won or Try Again based on result.

### Folder Structure
Problem6_Sudoku/
|-- app.py
|-- requirements.txt
|-- templates/
    |-- index.html

### Algorithm Used
- CSP Backtracking with MRV (Minimum Remaining Values) heuristic
- Forward checking with domain filtering
- Constraints: row, column and 3x3 box uniqueness

### Execution Steps
    pip install -r requirements.txt
    cd Problem6_Sudoku
    python app.py
    Open: http://localhost:5001

### Sample Output
    Difficulty : Easy (35 cells removed)
    CSP solved using Backtracking + MRV heuristic
    Result     : You Won! Congratulations!

---

## Author
- Name: SRI BALA PRIYAN S
- Register Number: RA2411026050332
- dept./section: IInd AIML-E