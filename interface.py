from EnzoUi import Ui_UIAssistant
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTime , QDate , QTimer
from PyQt5.uic import loadUiType
from Functionalities import *

class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        enzo_fun()

StartExec = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gui = Ui_UIAssistant()
        self.gui.setupUi(self)
        self.startTask()
        self.gui.Start_button.clicked.connect(self.startTask)
        self.gui.STop_button.clicked.connect(self.close)

    def startTask(self):

        self.gui.label1 = QtGui.QMovie("C://CODING//c cpp//python programs//AI assistant//project templates//VoiceReg-20231010T154334Z-001//VoiceReg//__02-____.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("C://CODING//c cpp//python programs//AI assistant//project templates//ExtraGui-20231010T181648Z-001//ExtraGui//background_gif_2.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)

        StartExec.start()

    def showTimeLive(self):
        t_ime = QTime.currentTime()
        time = t_ime.toString()
        d_ate = QDate.currentDate()
        date = d_ate.toString()
        label_time = "Time : "+ time
        label_date = "Date : "+ date

        self.gui.Text_time.setText(label_time)
        self.gui.Text_date.setText(label_date)        

