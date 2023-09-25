from instr import*
from second_win import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class FinalWin(QWidget):
    def __init__(self, ind, res):
        super().__init__()
        self.ind = ind
        self.res = res
        self.set_appear()# устанавливает внешний вид окна
        self.initUI() # графические элементы
        self.show() # старт
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.index = QLabel(txt_index+str(self.ind))
        self.txt_workheart = QLabel(txt_workheart+self.res)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.txt_workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)