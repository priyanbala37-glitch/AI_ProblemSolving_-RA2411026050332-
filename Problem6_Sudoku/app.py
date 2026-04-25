# Author: SRI BALA PRIYAN S
# Register Number: RA2411026050332
# Problem 6: Sudoku Solver using CSP

from flask import Flask, render_template, request, jsonify
import random
import copy
import os

app = Flask(__name__)

# ─────────────────────────────────────────────
#  CSP Core Logic
# ─────────────────────────────────────────────

def is_valid(board, row, col, num):
    # Row constraint
    if num in board[row]:
        return False
    # Column constraint
    if num in [board[r][col] for r in range(9)]:
        return False
    # 3x3 subgrid constraint
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == num:
                return False
    return True

def get_domain(board, row, col):
    if board[row][col] != 0:
        return []
    return [num for num in range(1, 10) if is_valid(board, row, col, num)]

def get_unassigned(board):
    """MRV Heuristic - pick cell with fewest valid options."""
    min_domain = 10
    best = None
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                domain = get_domain(board, r, c)
                if len(domain) < min_domain:
                    min_domain = len(domain)
                    best = (r, c, domain)
                    if min_domain == 1:
                        return best
    return best

def solve_csp(board):
    """CSP Backtracking with MRV heuristic and forward checking."""
    cell = get_unassigned(board)
    if cell is None:
        return True
    row, col, domain = cell
    for num in domain:
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_csp(board):
                return True
            board[row][col] = 0
    return False

def check_constraints(board):
    for r in range(9):
        row_vals = [board[r][c] for c in range(9) if board[r][c] != 0]
        if len(row_vals) != len(set(row_vals)):
            return False, f"Row {r+1} has duplicate values"
    for c in range(9):
        col_vals = [board[r][c] for r in range(9) if board[r][c] != 0]
        if len(col_vals) != len(set(col_vals)):
            return False, f"Column {c+1} has duplicate values"
    for br in range(3):
        for bc in range(3):
            box_vals = []
            for r in range(br*3, br*3+3):
                for c in range(bc*3, bc*3+3):
                    if board[r][c] != 0:
                        box_vals.append(board[r][c])
            if len(box_vals) != len(set(box_vals)):
                return False, f"3x3 box ({br+1},{bc+1}) has duplicates"
    return True, "OK"

# ─────────────────────────────────────────────
#  Puzzle Generator
# ─────────────────────────────────────────────

def generate_puzzle(difficulty='easy'):
    board = [[0]*9 for _ in range(9)]
    for box in range(3):
        nums = random.sample(range(1, 10), 9)
        for i in range(3):
            for j in range(3):
                board[box*3+i][box*3+j] = nums[i*3+j]
    solve_csp(board)
    solution = copy.deepcopy(board)
    removes = {'easy': 35, 'medium': 45, 'hard': 55}
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    for r, c in cells[:removes.get(difficulty, 35)]:
        board[r][c] = 0
    return board, solution

# ─────────────────────────────────────────────
#  Routes
# ─────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_puzzle', methods=['POST'])
def new_puzzle():
    difficulty = request.json.get('difficulty', 'easy')
    puzzle, solution = generate_puzzle(difficulty)
    return jsonify({'puzzle': puzzle, 'solution': solution})

@app.route('/solve', methods=['POST'])
def solve():
    board = request.json.get('board')
    board_copy = copy.deepcopy(board)
    if solve_csp(board_copy):
        return jsonify({'solved': True, 'board': board_copy})
    return jsonify({'solved': False})

@app.route('/validate', methods=['POST'])
def validate():
    user_board = request.json.get('user_board')
    solution   = request.json.get('solution')
    complete = all(user_board[r][c] != 0 for r in range(9) for c in range(9))
    if not complete:
        return jsonify({'status': 'incomplete', 'message': 'Puzzle is not complete yet!'})
    valid, msg = check_constraints(user_board)
    if not valid:
        return jsonify({'status': 'wrong', 'message': f'Constraint violated: {msg}'})
    if user_board == solution:
        return jsonify({'status': 'won', 'message': 'You Won! Congratulations!'})
    return jsonify({'status': 'wrong', 'message': 'Try Again! Some values are incorrect.'})

@app.route('/hint', methods=['POST'])
def hint():
    user_board = request.json.get('user_board')
    solution   = request.json.get('solution')
    original   = request.json.get('original')
    empties = [(r, c) for r in range(9) for c in range(9)
               if user_board[r][c] == 0 and original[r][c] == 0]
    if not empties:
        return jsonify({'hint': None})
    r, c = random.choice(empties)
    return jsonify({'hint': {'row': r, 'col': c, 'value': solution[r][c]}})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=False, host='0.0.0.0', port=port)