# AI Problem Solving — Problem 1: Interactive Tic-Tac-Toe AI

## Problem Description
A web-based Tic-Tac-Toe game where a human plays against an AI that never loses,
using Minimax and Alpha-Beta Pruning algorithms with real-time comparison.

## Folder Structure
Problem1_TicTacToe/
├── app.py
├── requirements.txt
└── templates/
    └── index.html

## Algorithms Used
- **Minimax** — explores every possible game state recursively
- **Alpha-Beta Pruning** — optimised Minimax that prunes ~97% of branches

## Execution Steps
pip install -r requirements.txt
cd Problem1_TicTacToe
python app.py
Open http://localhost:5000

## Sample Output
Algorithm  : α-β
Nodes      : 59
Time       : 0.31 ms

Minimax    : 549,945 nodes | 312.4 ms
Alpha-Beta :  18,297 nodes |  10.8 ms
α-β pruned 97% of nodes