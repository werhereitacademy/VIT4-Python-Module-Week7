# Form implementation generated from reading ui file 'mentor_menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 605)
        MainWindow.setMinimumSize(QtCore.QSize(820, 605))
        MainWindow.setStyleSheet("QMainWindow{\n"
" \n"
"    background-color: rgb(240, 240, 240);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.mainFrame.setMinimumSize(QtCore.QSize(500, 300))
        font = QtGui.QFont()
        font.setBold(False)
        self.mainFrame.setFont(font)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frameLeft = QtWidgets.QFrame(parent=self.mainFrame)
        self.frameLeft.setMinimumSize(QtCore.QSize(250, 500))
        self.frameLeft.setStyleSheet("")
        self.frameLeft.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameLeft.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameLeft.setObjectName("frameLeft")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frameLeft)
        self.verticalLayout_4.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frameTopLeft = QtWidgets.QFrame(parent=self.frameLeft)
        self.frameTopLeft.setMinimumSize(QtCore.QSize(0, 150))
        self.frameTopLeft.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameTopLeft.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameTopLeft.setObjectName("frameTopLeft")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frameTopLeft)
        self.verticalLayout_5.setContentsMargins(-1, 15, 0, 0)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelLogo = QtWidgets.QLabel(parent=self.frameTopLeft)
        self.labelLogo.setMinimumSize(QtCore.QSize(221, 61))
        self.labelLogo.setMaximumSize(QtCore.QSize(221, 61))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("logoPhoto.png"))
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setObjectName("labelLogo")
        self.verticalLayout_5.addWidget(self.labelLogo)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.pushButtonBackMainPage = QtWidgets.QPushButton(parent=self.frameTopLeft)
        self.pushButtonBackMainPage.setMinimumSize(QtCore.QSize(101, 31))
        self.pushButtonBackMainPage.setMaximumSize(QtCore.QSize(101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButtonBackMainPage.setFont(font)
        self.pushButtonBackMainPage.setStyleSheet("QPushButton{\n"
"background-color: rgb(65, 77, 77);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" \n"
" background-color: rgb(90, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
" background-color: white;\n"
" color: rgb(65, 77, 77);\n"
" border: 1px solid black;\n"
"}")
        self.pushButtonBackMainPage.setObjectName("pushButtonBackMainPage")
        self.verticalLayout_5.addWidget(self.pushButtonBackMainPage)
        self.verticalLayout_4.addWidget(self.frameTopLeft)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.frameMenu = QtWidgets.QFrame(parent=self.frameLeft)
        self.frameMenu.setMinimumSize(QtCore.QSize(221, 330))
        self.frameMenu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameMenu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameMenu.setObjectName("frameMenu")
        self.pushButtonAllMeetings = QtWidgets.QPushButton(parent=self.frameMenu)
        self.pushButtonAllMeetings.setGeometry(QtCore.QRect(10, 60, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.pushButtonAllMeetings.setFont(font)
        self.pushButtonAllMeetings.setStyleSheet("QPushButton{\n"
"background-color: rgb(65, 77, 77);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" \n"
" background-color: rgb(90, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
" background-color: white;\n"
" color: rgb(65, 77, 77);\n"
" border: 1px solid black;\n"
"}")
        self.pushButtonAllMeetings.setObjectName("pushButtonAllMeetings")
        self.verticalLayout_4.addWidget(self.frameMenu)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.frameLeftBottom = QtWidgets.QFrame(parent=self.frameLeft)
        self.frameLeftBottom.setMinimumSize(QtCore.QSize(0, 45))
        self.frameLeftBottom.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameLeftBottom.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameLeftBottom.setObjectName("frameLeftBottom")
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.frameLeftBottom)
        self.pushButtonExit.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.pushButtonExit.setMinimumSize(QtCore.QSize(101, 31))
        self.pushButtonExit.setMaximumSize(QtCore.QSize(101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButtonExit.setFont(font)
        self.pushButtonExit.setStyleSheet("QPushButton{\n"
" background-color: rgb(148, 0, 0);\n"
" color: rgb(255, 255, 255);\n"
" border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: rgba(157, 9, 19,200);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: white;\n"
"  color: rgb(170, 0, 0);\n"
"  border: 1px solid black;\n"
"}\n"
"\n"
"")
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.verticalLayout_4.addWidget(self.frameLeftBottom)
        self.horizontalLayout_2.addWidget(self.frameLeft)
        self.frameRight = QtWidgets.QFrame(parent=self.mainFrame)
        self.frameRight.setMinimumSize(QtCore.QSize(300, 300))
        self.frameRight.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameRight.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameRight.setObjectName("frameRight")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameRight)
        self.verticalLayout.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameTopRight = QtWidgets.QFrame(parent=self.frameRight)
        self.frameTopRight.setMinimumSize(QtCore.QSize(0, 100))
        self.frameTopRight.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frameTopRight.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameTopRight.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameTopRight.setObjectName("frameTopRight")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameTopRight)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelHeader = QtWidgets.QLabel(parent=self.frameTopRight)
        self.labelHeader.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.labelHeader.setFont(font)
        self.labelHeader.setStyleSheet("letter-spacing: 0.1em;\n"
"color: rgb(70, 70, 70);")
        self.labelHeader.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelHeader.setObjectName("labelHeader")
        self.verticalLayout_3.addWidget(self.labelHeader)
        self.frameSearch = QtWidgets.QFrame(parent=self.frameTopRight)
        self.frameSearch.setMinimumSize(QtCore.QSize(500, 50))
        self.frameSearch.setMaximumSize(QtCore.QSize(1000, 50))
        self.frameSearch.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameSearch.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameSearch.setObjectName("frameSearch")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameSearch)
        self.horizontalLayout.setContentsMargins(30, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.lineEditSearch = QtWidgets.QLineEdit(parent=self.frameSearch)
        self.lineEditSearch.setMinimumSize(QtCore.QSize(400, 30))
        self.lineEditSearch.setMaximumSize(QtCore.QSize(600, 30))
        self.lineEditSearch.setStyleSheet("QLineEdit {\n"
" background-color: white;\n"
" border-bottom-left-radius: 10px;\n"
" border-top-left-radius: 10px;\n"
" padding-left: 10px;\n"
" border: 1px solid gray;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border-color: black;\n"
"}")
        self.lineEditSearch.setText("")
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.horizontalLayout.addWidget(self.lineEditSearch)
        self.pushButtonSearch = QtWidgets.QPushButton(parent=self.frameSearch)
        self.pushButtonSearch.setMinimumSize(QtCore.QSize(65, 30))
        self.pushButtonSearch.setMaximumSize(QtCore.QSize(65, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonSearch.setFont(font)
        self.pushButtonSearch.setStyleSheet("QPushButton {\n"
"background-color: rgb(65, 77, 77);\n"
"color: rgb(255, 255, 255);\n"
" border-bottom-right-radius: 10px;\n"
" border-top-right-radius: 10px;\n"
" padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" \n"
" background-color: rgb(90, 100, 100);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
" background-color: white;\n"
" color: rgb(65, 77, 77);\n"
" border: 1px solid black;\n"
"}")
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.horizontalLayout.addWidget(self.pushButtonSearch)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout_3.addWidget(self.frameSearch)
        self.frame_6 = QtWidgets.QFrame(parent=self.frameTopRight)
        self.frame_6.setMinimumSize(QtCore.QSize(500, 40))
        self.frame_6.setMaximumSize(QtCore.QSize(1000, 40))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setContentsMargins(32, 5, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.comboBox = QtWidgets.QComboBox(parent=self.frame_6)
        self.comboBox.setMinimumSize(QtCore.QSize(470, 30))
        self.comboBox.setStyleSheet("QComboBox {\n"
" background-color: white;\n"
" border-bottom-left-radius: 10px;\n"
" border-top-left-radius: 10px;\n"
" padding-left: 10px;\n"
" border: 1px solid gray;\n"
"\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"border-color: black;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frameTopRight)
        self.tableWidgetCandidates = QtWidgets.QTableWidget(parent=self.frameRight)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.tableWidgetCandidates.setFont(font)
        self.tableWidgetCandidates.setObjectName("tableWidgetCandidates")
        self.tableWidgetCandidates.setColumnCount(6)
        self.tableWidgetCandidates.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidgetCandidates.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidgetCandidates.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidgetCandidates.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidgetCandidates.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidgetCandidates.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidgetCandidates.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tableWidgetCandidates)
        self.horizontalLayout_2.addWidget(self.frameRight)
        self.verticalLayout_2.addWidget(self.mainFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonBackMainPage.setText(_translate("MainWindow", "<  Main Page"))
        self.pushButtonAllMeetings.setText(_translate("MainWindow", "All Meetings"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))
        self.labelHeader.setText(_translate("MainWindow", "MENTOR MEETINGS"))
        self.pushButtonSearch.setText(_translate("MainWindow", "Search"))
        self.comboBox.setItemText(0, _translate("MainWindow", "VIT Projesinin Tamamina Katilmasi Uygun Olur"))
        self.comboBox.setItemText(1, _translate("MainWindow", "VIT Projesinin ilk IT Egitimi Alanina Yonlendirilmesi Uygun Olur"))
        self.comboBox.setItemText(2, _translate("MainWindow", "VIT Projesinin INgilizce Egitim Alanini Yonlendirilmesi Uygun Olur"))
        self.comboBox.setItemText(3, _translate("MainWindow", "VIT Projesi Kapsaminda..."))
        item = self.tableWidgetCandidates.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Meeting Date"))
        item = self.tableWidgetCandidates.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Candidate Name"))
        item = self.tableWidgetCandidates.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mentor"))
        item = self.tableWidgetCandidates.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IT Knowledge"))
        item = self.tableWidgetCandidates.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Availability"))
        item = self.tableWidgetCandidates.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Comments"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
