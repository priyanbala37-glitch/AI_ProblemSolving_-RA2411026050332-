from flask import Flask, render_template, request, jsonify
import time
import math

app = Flask(__name__)

# ─────────────────────────────────────────────
#  Core game logic
# ─────────────────────────────────────────────

def check_winner(board):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # cols
        [0,4,8],[2,4,6]           # diags
    ]
    for line in wins:
        a,b,c = line
        if board[a] and board[a] == board[b] == board[c]:
            return board[a], line
    return None, None

def is_full(board):
    return all(cell != '' for cell in board)

def get_empty(board):
    return [i for i, cell in enumerate(board) if cell == '']

# ─────────────────────────────────────────────
#  Minimax (no pruning)
# ─────────────────────────────────────────────

nodes_minimax = 0

def minimax(board, is_maximizing, ai_player, human_player):
    global nodes_minimax
    nodes_minimax += 1

    winner, _ = check_winner(board)
    if winner == ai_player:
        return 10
    if winner == human_player:
        return -10
    if is_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in get_empty(board):
            board[i] = ai_player
            score = minimax(board, False, ai_player, human_player)
            board[i] = ''
            best = max(best, score)
        return best
    else:
        best = math.inf
        for i in get_empty(board):
            board[i] = human_player
            score = minimax(board, True, ai_player, human_player)
            board[i] = ''
            best = min(best, score)
        return best

def best_move_minimax(board, ai_player, human_player):
    global nodes_minimax
    nodes_minimax = 0
    best_score = -math.inf
    move = -1
    start = time.perf_counter()
    for i in get_empty(board):
        board[i] = ai_player
        score = minimax(board, False, ai_player, human_player)
        board[i] = ''
        if score > best_score:
            best_score = score
            move = i
    elapsed = (time.perf_counter() - start) * 1000
    return move, nodes_minimax, round(elapsed, 4)

# ─────────────────────────────────────────────
#  Alpha-Beta Pruning
# ─────────────────────────────────────────────

nodes_ab = 0

def alpha_beta(board, is_maximizing, ai_player, human_player, alpha, beta):
    global nodes_ab
    nodes_ab += 1

    winner, _ = check_winner(board)
    if winner == ai_player:
        return 10
    if winner == human_player:
        return -10
    if is_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in get_empty(board):
            board[i] = ai_player
            score = alpha_beta(board, False, ai_player, human_player, alpha, beta)
            board[i] = ''
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in get_empty(board):
            board[i] = human_player
            score = alpha_beta(board, True, ai_player, human_player, alpha, beta)
            board[i] = ''
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

def best_move_ab(board, ai_player, human_player):
    global nodes_ab
    nodes_ab = 0
    best_score = -math.inf
    move = -1
    start = time.perf_counter()
    for i in get_empty(board):
        board[i] = ai_player
        score = alpha_beta(board, False, ai_player, human_player, -math.inf, math.inf)
        board[i] = ''
        if score > best_score:
            best_score = score
            move = i
    elapsed = (time.perf_counter() - start) * 1000
    return move, nodes_ab, round(elapsed, 4)

# ─────────────────────────────────────────────
#  Routes
# ─────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ai_move', methods=['POST'])
def ai_move():
    data = request.json
    board        = data['board']
    ai_player    = data['ai_player']
    human_player = data['human_player']
    algorithm    = data.get('algorithm', 'alpha_beta')

    winner, win_line = check_winner(board)
    if winner or is_full(board):
        return jsonify({'move': -1, 'nodes': 0, 'time_ms': 0})

    if algorithm == 'minimax':
        move, nodes, t = best_move_minimax(board, ai_player, human_player)
    else:
        move, nodes, t = best_move_ab(board, ai_player, human_player)

    board[move] = ai_player
    winner, win_line = check_winner(board)
    draw = is_full(board) and not winner

    return jsonify({
        'move'    : move,
        'nodes'   : nodes,
        'time_ms' : t,
        'winner'  : winner,
        'win_line': win_line,
        'draw'    : draw
    })

@app.route('/compare', methods=['POST'])
def compare():
    data         = request.json
    board        = data['board']
    ai_player    = data['ai_player']
    human_player = data['human_player']

    b1 = board[:]
    move_mm, nodes_mm, t_mm = best_move_minimax(b1, ai_player, human_player)

    b2 = board[:]
    move_ab2, nodes_ab2, t_ab2 = best_move_ab(b2, ai_player, human_player)

    return jsonify({
        'minimax'   : {'move': move_mm,   'nodes': nodes_mm,   'time_ms': t_mm},
        'alpha_beta': {'move': move_ab2,  'nodes': nodes_ab2,  'time_ms': t_ab2}
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)