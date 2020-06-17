from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFrame
from PyQt5 import QtGui
import sys
import time


class ScrabbleUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrabble Optimizer")
        self.setFixedSize(700, 960)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self.fieldsLayout = QGridLayout()
        self.init_color_fields()
        self.create_display()
        self.create_buttons()
        self.create_labels()
        self.create_fields()

    def create_display(self):
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignCenter)
        self.display.setFixedHeight(35)
        self.display.setFixedWidth(200)
        self.display.setAlignment(Qt.AlignRight)
        self.generalLayout.addWidget(self.display)

    def create_buttons(self):
        self.btn = QPushButton('Calculate!')
        self.btn.setFixedHeight(35)
        self.btn.setFixedWidth(200)
        self.generalLayout.addWidget(self.btn)
        self.btn_reset = QPushButton('Reset')
        self.btn_reset.setFixedHeight(35)
        self.btn_reset.setFixedWidth(200)
        self.generalLayout.addWidget(self.btn_reset)
        self.btn_dict = QPushButton('Load dictionary first')
        self.btn_dict.setFixedHeight(35)
        self.btn_dict.setFixedWidth(200)
        self.generalLayout.addWidget(self.btn_dict)

    def create_labels(self):
        self.result_lbl = QLabel('')
        self.result_lbl.setFixedHeight(30)
        self.result_lbl.setFixedWidth(300)
        self.generalLayout.addWidget(self.result_lbl)
        self.other_result_lbl = QLabel('')
        self.other_result_lbl.setFixedHeight(30)
        self.other_result_lbl.setFixedWidth(670)
        self.generalLayout.addWidget(self.other_result_lbl)
        self.letter_remaining_lbl = QLabel('')
        self.letter_remaining_lbl.setFixedHeight(30)
        self.letter_remaining_lbl.setFixedWidth(670)
        self.generalLayout.addWidget(self.letter_remaining_lbl)

    def load_board_from_file(self):
        f = open("optimizer/resources/board.csv", "r")
        bb = [line.strip().lower() for line in f]
        self.board_from_file = []
        #konwersja csv na listy stringow
        for x in range(len(bb)):
            line = bb[x].split(";")
            upper_line = [y.upper() for y in line] 
            self.board_from_file.append(upper_line)

    def create_fields(self):
        self.fields = {} 
        self.load_board_from_file()
        self.set_board(self.board_from_file)

    def set_fields(self):
        for x in range(len(self._board)):
            for y in range(len(self._board[x])):
                self.fields[str(x)+';'+str(y)]=(x, y)
                
        for id, pos in self.fields.items():
            _id = id.split(';')
            label = QLabel(str(self._board[int(_id[0])][int(_id[1])]))
            label.setFrameStyle(QFrame.Panel | QFrame.Raised)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-weight: bold; color: rgb(10, 10, 10); font-size: 18;background-color : " + self.coloring_field(id))
            label.setUpdatesEnabled(True)
            label.setFont(QtGui.QFont("Cambria", 22 , QtGui.QFont.Black))
            self.fields[id] = label
            self.fields[id].setFixedSize(40, 40)
            self.fieldsLayout.addWidget(self.fields[id], pos[0], pos[1])
        self.generalLayout.addLayout(self.fieldsLayout)


    def init_color_fields(self):
        self.color_dic={}
        size = 15
        for x in range (size):
            for y in range (size):
                key = str(x)+';'+str(y)
                self.color_dic[key]=self.get_color(key)

    def get_color(self,key):
        _key = key.split(";")
        x = int(_key[0])
        y = int(_key[1])
        colour='black'
        if((x==y) or (int(x+y)==14)):
            colour ='rgb(255, 153, 255)'
        else:
            colour = 'rgb(230, 230, 230)'
        if(((x==0 or x==14) and (y==0 or y==7 or y==14)) or (x==7 and (y==0 or y==14))):
            colour ='red'
        if(((x==5 or x==9) and (y==1 or y==5 or y==9 or y==13)) or ((x==1 or x==13) and (y==5 or y==9))):
            colour ='rgb(0, 101, 255)'
        if(((x==0 or x==7 or x==14) and (y==3 or y==11)) or ((x==3 or x==11) and (y==0 or y==7 or y==14))
            or((x==2 or x==6 or x==8 or x==12) and (y==6 or y==8)) or((y==2 or y==6 or y==8 or y==12) and (x==6 or x==8))):
            colour ='rgb(102, 204, 255)'
        if(x==7 and y==7):
            colour ='green'

        return colour

    def coloring_field(self, key):
        return self.color_dic.get(key)

    def get_letters(self):
        return self.display.text()

    def set_board(self,board):
        self._board=[]
        self._board.clear()
        for x in range(len(board)):
            upper_line = [y.upper() for y in board[x]] 
            self._board.append(upper_line)
        self.set_fields()
        
    def get_board(self):
        return self._board