from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 560)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(560, 0, 20, 581))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_back = QtWidgets.QLabel(self.centralwidget)
        self.label_back.setGeometry(QtCore.QRect(570, 0, 361, 581))
        self.label_back.setStyleSheet("background-image: url(img/b1.jpg);\n")
        self.label_back.setText("")
        self.label_back.setObjectName("label_back")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(580, 240, 336, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_o = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_o.setFont(font)
        self.label_o.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_o.setObjectName("label_o")
        self.horizontalLayout_2.addWidget(self.label_o)
        spacerItem = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.comboBox_o = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_o.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_o.setFont(font)
        self.comboBox_o.setStyleSheet("QComboBox {\n"
                                      "    background-image: url(img/b1.jpg);\n"
                                      "    border: 3px solid rgb(40,40,240);\n"
                                      "    color: rgb(240,240,240);\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "    background-image: url(img/b1.jpg);\n"
                                      "    color: rgb(240,240,240);\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::drop-down {\n"
                                      "    border-image:url(img/aa.png);\n"
                                      "    border: 3px solid rgb(40,40,40);\n"
                                      " }")
        self.comboBox_o.setObjectName("comboBox_o")
        self.comboBox_o.addItem("")
        self.comboBox_o.addItem("")
        self.comboBox_o.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_o)
        self.btn_newGame = QtWidgets.QPushButton(self.centralwidget)
        self.btn_newGame.setGeometry(QtCore.QRect(670, 380, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_newGame.setFont(font)
        self.btn_newGame.setStyleSheet("QPushButton {\n"
                                       "    background-image: url(img/b1.jpg);\n"
                                       "    background-color: rgb(142, 176, 174);\n"
                                       "    color: rgb(240,240,240);\n"
                                       "}")
        self.btn_newGame.setObjectName("btn_newGame")
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(890, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet("QPushButton {\n"
                                        "    background-image: url(img/b1.jpg);\n"
                                        "    background-color: rgb(142, 176, 174);\n"
                                        "    color: rgb(200,50,50);\n"
                                        "}")
        self.btn_close.setObjectName("pushButton_2")
        self.btn_minimize = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minimize.setGeometry(QtCore.QRect(860, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minimize.setFont(font)
        self.btn_minimize.setStyleSheet("QPushButton {\n"
                                        "    background-image: url(img/b1.jpg);\n"
                                        "    background-color: rgb(142, 176, 174);\n"
                                        "    color: rgb(240,240,240);\n"
                                        "}")
        self.btn_minimize.setObjectName("pushButton_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -1, 571, 582))
        self.frame.setStyleSheet("background-image: url(img/b1.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 541, 523))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.p4 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.p4.setFont(font)
        self.p4.setStyleSheet("background-color: rgb(142, 176, 174);\n"
                              "color: rgb(230, 230, 230);\n"
                              "\n")
        self.p4.setObjectName("p4")
        self.gridLayout.addWidget(self.p4, 1, 1, 1, 1)
        self.p5 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.p5.setFont(font)
        self.p5.setStyleSheet("background-color: rgb(142, 176, 174);\n"
                              "color: rgb(230, 230, 230);\n"
                              "\n")
        self.p5.setObjectName("p5")
        self.gridLayout.addWidget(self.p5, 1, 2, 1, 1)
        self.p3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.p3.setFont(font)
        self.p3.setStyleSheet("background-color: rgb(142, 176, 174);\n"
                              "color: rgb(230, 230, 230);\n"
                              "\n")
        self.p3.setObjectName("p3")
        self.gridLayout.addWidget(self.p3, 1, 0, 1, 1)
        self.p6 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.p6.setFont(font)
        self.p6.setStyleSheet("background-color: rgb(142, 176, 174);\n"
                              "color: rgb(230, 230, 230);\n"
                              "\n")
        self.p6.setObjectName("p6")
        self.gridLayout.addWidget(self.p6, 2, 0, 1, 1)
        self.p8 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.p8.setFont(font)
        self.p8.setStyleSheet("background-color: rgb(142, 176, 174);\n"
                              "color: rgb(230, 230, 230);\n"
                              "\n")
        self.p8.setObjectName("p8")
        self.gridLayout.addWidget(self.p8, 2, 2, 1, 1)
        self.p2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.p2.setFont(font)
        self.p2.setStyleSheet("background-color: rgb(142, 176, 174);\n"
                              "color: rgb(230, 230, 230);\n"
                              "\n")
        self.p2.setObjectName("p2")
        self.gridLayout.addWidget(self.p2, 0, 2, 1, 1)
        self.p0 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.p0.setFont(font)
        self.p0.setStyleSheet("background-color: rgb(142, 176, 174);\n"
                              "color: rgb(230, 230, 230);\n")
        self.p0.setObjectName("p0")
        self.gridLayout.addWidget(self.p0, 0, 0, 1, 1)
        self.p1 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.p1.setFont(font)
        self.p1.setStyleSheet("background-color: rgb(142, 176, 174);\n"
                              "color: rgb(230, 230, 230);\n"
                              "\n")
        self.p1.setObjectName("p1")
        self.gridLayout.addWidget(self.p1, 0, 1, 1, 1)
        self.p7 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.p7.setFont(font)
        self.p7.setStyleSheet("background-color: rgb(142, 176, 174);\n"
                              "color: rgb(230, 230, 230);\n"
                              "\n")
        self.p7.setObjectName("p7")
        self.gridLayout.addWidget(self.p7, 2, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(553, 0, 31, 571))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(580, 450, 321, 39))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(100, 220, 100);")
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(580, 100, 336, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_x = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_x.setFont(font)
        self.label_x.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_x.setObjectName("label_x")
        self.horizontalLayout.addWidget(self.label_x)
        spacerItem1 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.comboBox_x = QtWidgets.QComboBox(self.widget)
        self.comboBox_x.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_x.setFont(font)
        self.comboBox_x.setStyleSheet("QComboBox {\n"
                                      "    background-image: url(img/b1.jpg);\n"
                                      "    border: 3px solid rgb(40,40,240);\n"
                                      "    color: rgb(240,240,240);\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "    background-image: url(img/b1.jpg);\n"
                                      "    color: rgb(240,240,240);\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::drop-down {\n"
                                      "    border-image:url(img/aa.png);\n"
                                      "    border: 3px solid rgb(40,40,40);\n"
                                      " }")
        self.comboBox_x.setObjectName("comboBox_x")
        self.comboBox_x.addItem("")
        self.comboBox_x.addItem("")
        self.comboBox_x.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_x)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_o.setText(_translate("MainWindow", "PLAYER [O]"))
        self.comboBox_o.setItemText(0, _translate("MainWindow", "Human"))
        self.comboBox_o.setItemText(1, _translate("MainWindow", "Easy AI"))
        self.comboBox_o.setItemText(2, _translate("MainWindow", "Hard AI"))
        self.btn_newGame.setText(_translate("MainWindow", "New Game"))
        self.btn_close.setText(_translate("MainWindow", "X"))
        self.btn_minimize.setText(_translate("MainWindow", "_"))
        self.p4.setText(_translate("MainWindow", "?"))
        self.p5.setText(_translate("MainWindow", "?"))
        self.p3.setText(_translate("MainWindow", "?"))
        self.p6.setText(_translate("MainWindow", "?"))
        self.p8.setText(_translate("MainWindow", "?"))
        self.p2.setText(_translate("MainWindow", "?"))
        self.p0.setText(_translate("MainWindow", "?"))
        self.p1.setText(_translate("MainWindow", "?"))
        self.p7.setText(_translate("MainWindow", "?"))
        self.label_x.setText(_translate("MainWindow", "PLAYER [X]"))
        self.comboBox_x.setItemText(0, _translate("MainWindow", "Human"))
        self.comboBox_x.setItemText(1, _translate("MainWindow", "Easy AI"))
        self.comboBox_x.setItemText(2, _translate("MainWindow", "Hard AI"))
