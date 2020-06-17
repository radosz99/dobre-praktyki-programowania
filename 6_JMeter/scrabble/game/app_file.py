from flask import Flask, jsonify, request, abort, render_template, flash, redirect, url_for
from .backend.logic import make_move, random_string, prepare_board, save_game_log_to_file, get_game_log_from_file
import sys,json
import threading
	
lock = threading.Lock()
lock_view = threading.Lock()

app = Flask(__name__)


@app.route('/')
def student():
    return redirect(url_for('game_view'))

@app.route('/game/view',methods=['GET'])
def game_view():
    #lock_view.acquire()
    #lock.acquire()
    board, users, moves, turn, letters = get_game_log_from_file()
    #lock.release()

    last_moves=[]
    if(len(moves)>=10):
        last_moves = moves[0:10].copy()
    elif(len(moves)==0):
        last_moves = []
    else:
        last_moves = moves.copy()
    #lock_view.release()
    return render_template("game.html", board = board, users=users, turn=turn, letters_quantity=len(letters), moves=last_moves)    

@app.route('/game/move',methods = ['POST'])
def move():
    #lock.acquire()
    move=str(request.form.get("move"))
    board, users, moves, turn, letters = get_game_log_from_file()
    board, points, letters_not_used, word = make_move(move=move, board=board, user_letters=users[turn][2].upper())
    moves.insert(0,(turn, word, points))
    new_letters, letters = random_string(letters, letters_not_used)
    user = (users[turn][0], users[turn][1]+points, new_letters)
    users = list(filter(lambda x: x[0] != turn, users))
    users.append(user)
    users.sort(key=lambda tup: tup[0])

    if(turn<len(users)-1):
        turn = turn+1
    else:
        turn=0

    save_game_log_to_file(board=board, letters=letters, users=users, turn=turn,moves=moves)
    #lock.release()
    #return redirect(url_for('game_view'))
    return render_template("start.html") 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)