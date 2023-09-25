from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import *
#from PyQt5.QtWidgets import (QCoreApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)
#line_name = QLineEdit('')
from instr import*
from final_win import*
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()# устанавливает внешний вид окна
        self.initUI() # графические элементы
        self.connects() # связи между элементами
        self.show() # старт
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)
        self.text_name = QLabel(txt_name)
        self.txt_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
        self.text_timer=QLabel('00:00:00')
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer1)
        self.btn_test2.clicked.connect(self.timer2)
        self.btn_test3.clicked.connect(self.timer3)
    def timer1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 255,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
            self.timer.stop()
            
    def timer2Event(self):
        global time
        time = time.addSecs(-1.5)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 255,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
            self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0,0)")
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def next_click(self):
        self.hide()
        
        ind = (4*(int(self.line_test1.text())+int(self.line_test2.text())+int(self.line_test3.text()))-200)/10
        vos = int(self.line_age.text())
        if vos>=15:
            if ind>=15:
                res = "Низкий"
            elif ind>=11 and ind<15:
                res = "Удовлетворительный"
            elif ind>=6 and ind<11:
                res = "Средний"
            elif ind>=0.5 and inf<6:
                res = "Выше среднего"
            elif ind<0.5:
                res = "Высокий" 
        elif vos==13 or vos==14:
            if ind>=16.5:
                res = "Низкий"
            elif ind>=12.5 and ind<16.5:
                res = "Удовлетворительный"
            elif ind>=7.5 and ind<12.5:
                res = "Средний"
            elif ind>=2 and inf<7.5:
                res = "Выше среднего"
            elif ind<2:
                res = "Высокий"
        elif vos==11 or vos==12:
            if ind>=18:
                res = "Низкий"
            elif ind>=14 and ind<18:
                res = "Удовлетворительный"
            elif ind>=9 and ind<14:
                res = "Средний"
            elif ind>=3.5 and inf<9:
                res = "Выше среднего"
            elif ind<3.5:
                res = "Высокий"
        elif vos==9 or vos==10:
            if ind>=19.5:
                res = "Низкий"
            elif ind>=15.5 and ind<19.5:
                res = "Удовлетворительный"
            elif ind>=10.5 and ind<11.5:
                res = "Средний"
            elif ind>=5 and inf<10.5:
                res = "Выше среднего"
            elif ind<5:
                res = "Высокий"
        elif vos==7 or vos==8:
            if ind>=21:
                res = "Низкий"
            elif ind>=17 and ind<21:
                res = "Удовлетворительный"
            elif ind>=12 and ind<17:
                res = "Средний"
            elif ind>=6.5 and inf<12:
                res = "Выше среднего"
            elif ind<6.5:
                res = "Высокий"
        self.tw = FinalWin(ind,res)
