from flask import Flask, jsonify, request, abort, render_template, flash, redirect, url_for
from .backend.logic import make_move, random_string, prepare_board
import sys
app = Flask(__name__)

board=[]
users=[]
moves=[]
turn=0
letters = []

@app.route('/')
def student():
    global letters,users,board,turn,moves
    letters=['a','a','a','a','a','a','a','a','a','e','e','e','e','e','e','e','e','e','e','e','e','i','i','i','i','i','i','i','i','i','o','o','o','o','o','o','o','o',
        'n','n','n','n','n','n','r','r','r','r','r','r','t','t','t','t','t','t','l','l','l','l','s','s','s','s','u','u','u','u','d','d','d','d','g','g','g','b','b','c','c','m','m','p','p','f',
        'f','h','h','v','v','w','w','y','y','k','j','x','q','z']
    users.clear()
    user_letters, letters = random_string(letters,'')
    users.append((len(users),0,user_letters))
    user_letters, letters = random_string(letters,'')
    users.append((len(users),0,user_letters))   
    board.clear()
    moves.clear()
    turn=0
    board=prepare_board()
    return redirect(url_for('game_view'))

@app.route('/game/view',methods=['GET'])
def game_view():
    last_moves=[]
    if(len(moves)>=10):
        last_moves = moves[0:10].copy()
    elif(len(moves)==0):
        last_moves = []
    else:
        last_moves = moves.copy()
    return render_template("game.html", board = board, users=users, turn=turn, letters_quantity=len(letters), moves=last_moves)    

@app.route('/game/move',methods = ['POST'])
def move():
    global users,turn,board, letters
    info = request.form
    move=info['move']
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

    return render_template("start.html") 
    #return redirect(url_for('game_view'))

@app.route('/game/user', methods = ['POST'])
def add_user():
    global letters
    user_letters, letters = random_string(letters,'')
    users.append((len(users),0,user_letters))
    return redirect(url_for('game_view'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)