# Form implementation generated from reading ui file 'applications_page.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_applications_page_MainWindow(object):
    def setupUi(self, applications_page_MainWindow):
        applications_page_MainWindow.setObjectName("applications_page_MainWindow")
        applications_page_MainWindow.resize(1220, 735)
        applications_page_MainWindow.setMinimumSize(QtCore.QSize(1220, 735))
        applications_page_MainWindow.setMaximumSize(QtCore.QSize(1220, 735))
        self.centralwidget = QtWidgets.QWidget(parent=applications_page_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.frame.setMinimumSize(QtCore.QSize(1200, 700))
        self.frame.setMaximumSize(QtCore.QSize(1200, 700))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.Search_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Search_pushButton.setGeometry(QtCore.QRect(9, 164, 111, 41))
        self.Search_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Search_pushButton.setObjectName("Search_pushButton")
        self.Meetings_with_unassigned_mentor_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Meetings_with_unassigned_mentor_pushButton.setGeometry(QtCore.QRect(9, 283, 311, 41))
        self.Meetings_with_unassigned_mentor_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Meetings_with_unassigned_mentor_pushButton.setObjectName("Meetings_with_unassigned_mentor_pushButton")
        self.Meetings_with_assigned_mentor_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Meetings_with_assigned_mentor_pushButton.setGeometry(QtCore.QRect(9, 223, 231, 41))
        self.Meetings_with_assigned_mentor_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Meetings_with_assigned_mentor_pushButton.setObjectName("Meetings_with_assigned_mentor_pushButton")
        self.Different_records_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Different_records_pushButton.setGeometry(QtCore.QRect(700, 280, 221, 41))
        self.Different_records_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Different_records_pushButton.setObjectName("Different_records_pushButton")
        self.All_applications_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.All_applications_pushButton.setGeometry(QtCore.QRect(970, 220, 221, 101))
        self.All_applications_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.All_applications_pushButton.setObjectName("All_applications_pushButton")
        self.Filtered_Applications_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Filtered_Applications_pushButton.setGeometry(QtCore.QRect(440, 280, 231, 41))
        self.Filtered_Applications_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Filtered_Applications_pushButton.setObjectName("Filtered_Applications_pushButton")
        self.Former_VIT_Check_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Former_VIT_Check_pushButton.setGeometry(QtCore.QRect(440, 220, 231, 41))
        self.Former_VIT_Check_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Former_VIT_Check_pushButton.setObjectName("Former_VIT_Check_pushButton")
        self.Multiple_records_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Multiple_records_pushButton.setGeometry(QtCore.QRect(700, 220, 221, 41))
        self.Multiple_records_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Multiple_records_pushButton.setObjectName("Multiple_records_pushButton")
        self.Preferences_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Preferences_pushButton.setGeometry(QtCore.QRect(440, 330, 171, 41))
        self.Preferences_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Preferences_pushButton.setObjectName("Preferences_pushButton")
        self.Exit_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Exit_pushButton.setGeometry(QtCore.QRect(1020, 330, 171, 41))
        self.Exit_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Exit_pushButton.setObjectName("Exit_pushButton")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(440, 170, 751, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(520, 50, 161, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 370, 1181, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.Werhere = QtWidgets.QLabel(parent=self.frame)
        self.Werhere.setGeometry(QtCore.QRect(9, 3, 441, 131))
        self.Werhere.setText("")
        self.Werhere.setPixmap(QtGui.QPixmap("werhere_image.png"))
        self.Werhere.setObjectName("Werhere")
        self.Werhere_2 = QtWidgets.QLabel(parent=self.frame)
        self.Werhere_2.setGeometry(QtCore.QRect(750, 0, 441, 131))
        self.Werhere_2.setText("")
        self.Werhere_2.setPixmap(QtGui.QPixmap("werhere_image.png"))
        self.Werhere_2.setObjectName("Werhere_2")
        applications_page_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=applications_page_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1220, 43))
        self.menubar.setObjectName("menubar")
        applications_page_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=applications_page_MainWindow)
        self.statusbar.setObjectName("statusbar")
        applications_page_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(applications_page_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(applications_page_MainWindow)

#Push Button

        self.Exit_pushButton.clicked.connect(self.Exit_clicked)
        self.Preferences_pushButton.clicked.connect(self.Preferences_clicked)
        self.Former_VIT_Check_pushButton.clicked.connect(self.Former_VIT_Check_clicked)
        self.Filtered_Applications_pushButton.clicked.connect(self.Filtered_Applications_clicked)
        self.Multiple_records_pushButton.clicked.connect(self.Multiple_records_clicked)
        self.All_applications_pushButton.clicked.connect(self.All_applications_clicked)
        self.Meetings_with_assigned_mentor_pushButton.clicked.connect(self.Meetings_with_assigned_mentor_clicked)
        self.Meetings_with_unassigned_mentor_pushButton.clicked.connect(self.Meetings_with_unassigned_mentor_clicked)
        self.Search_pushButton.clicked.connect(self.Search_clicked)

    def retranslateUi(self, applications_page_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        applications_page_MainWindow.setWindowTitle(_translate("applications_page_MainWindow", "Applications"))
        self.Search_pushButton.setText(_translate("applications_page_MainWindow", "Search"))
        self.Meetings_with_unassigned_mentor_pushButton.setText(_translate("applications_page_MainWindow", "Meetings with unassigned mentor"))
        self.Meetings_with_assigned_mentor_pushButton.setText(_translate("applications_page_MainWindow", "Meetings with assigned mentor"))
        self.Different_records_pushButton.setText(_translate("applications_page_MainWindow", "Different records"))
        self.All_applications_pushButton.setText(_translate("applications_page_MainWindow", "All applications"))
        self.Filtered_Applications_pushButton.setText(_translate("applications_page_MainWindow", "Filtered applications"))
        self.Former_VIT_Check_pushButton.setText(_translate("applications_page_MainWindow", "Former VIT Check"))
        self.Multiple_records_pushButton.setText(_translate("applications_page_MainWindow", "Multiple records"))
        self.Preferences_pushButton.setText(_translate("applications_page_MainWindow", "Preferences"))
        self.Exit_pushButton.setText(_translate("applications_page_MainWindow", "EXIT"))
        self.lineEdit_2.setText(_translate("applications_page_MainWindow", "          APPLICATIONS"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("applications_page_MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("applications_page_MainWindow", "Name-Surname"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("applications_page_MainWindow", "Mail"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("applications_page_MainWindow", "Telephone"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("applications_page_MainWindow", "Post Code"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("applications_page_MainWindow", "City"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("applications_page_MainWindow", "Current Status"))

     #Transitions and explainations

    def Exit_clicked(self):
        from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
        QApplication.instance().quit()   

    def Preferences_clicked(self):
        from preference_admin_menu import Ui_admin_pref_men_MainWindow
        self.MainWindow= QtWidgets.QMainWindow()
        self.ui =Ui_admin_pref_men_MainWindow()
        self.ui.setupUi(applications_page_MainWindow) 
        
    def Former_VIT_Check_clicked(self):
        print("-------Now you are looking at Former_VIT_Check")
    def Filtered_Applications_clicked(self):
        print("-------Now you are looking at Filtered_Applications")
    def All_applications_clicked(self):
        print("-------Now you are looking at All_applications")   
    def Multiple_records_clicked(self):
        print("-------Now you are looking at Multiple_records")
    def Meetings_with_assigned_mentor_clicked(self):
        print("-------Now you are looking at Meetings_with_assigned_mentor")
    def Meetings_with_unassigned_mentor_clicked(self):
        print("-------Now you are looking at Meetings_with_unassigned_mentor")
    def Search_clicked(self):
        print("-------Now you are looking at Search")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    applications_page_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_applications_page_MainWindow()
    ui.setupUi(applications_page_MainWindow)
    applications_page_MainWindow.show()
    sys.exit(app.exec())