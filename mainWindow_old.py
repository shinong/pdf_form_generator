# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pdf as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(590, 60, 112, 23))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(lambda:self.onClicked(self.radioButton))       #added func
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(470, 60, 112, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(lambda:self.onClicked(self.radioButton_2))   #added func
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(560, 240, 110, 26))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 240, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 160, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 200, 67, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(560, 150, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(560, 200, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 330, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonClicked)             #added func
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 90, 151, 421))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setTabletTracking(True)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 200, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.plusOneButton)           #added func
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 60, 91, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 250, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.repeatButton)            #added func
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 100, 61, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(560, 100, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSave_file = QtWidgets.QAction(MainWindow)
        self.actionSave_file.setObjectName("actionSave_file")
        self.actionPreference = QtWidgets.QAction(MainWindow)
        self.actionPreference.setObjectName("actionPreference")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreference)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lab Assistant_Shinong"))
        self.radioButton.setText(_translate("MainWindow", "JRun"))
        self.radioButton_2.setText(_translate("MainWindow", "PRun"))
        self.label.setText(_translate("MainWindow", "Start Time"))
        self.label_2.setText(_translate("MainWindow", "E Index"))
        self.label_3.setText(_translate("MainWindow", "P Index"))
        self.pushButton.setText(_translate("MainWindow", "PDF Gen"))
        self.pushButton_2.setText(_translate("MainWindow", "Plus one"))
        self.label_4.setText(_translate("MainWindow", "Input Talbe"))
        self.pushButton_3.setText(_translate("MainWindow", "Repeat"))
        self.label_5.setText(_translate("MainWindow", "Run #"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Open Folder"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionSave_file.setText(_translate("MainWindow", "Save file"))
        self.actionPreference.setText(_translate("MainWindow", "Preference"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def onClicked(self,b):
        if b.text() == 'PRun':
            self.PStatus = True
        elif b.text() == 'JRun':
            self.PStatus = False
        else:
            print ("Error")
        

    def buttonClicked(self):
        if self.PStatus == True:
            print('Prun')
            #print(self.lineEdit_3.text())           #Run number
            #print(self.lineEdit.text())             #EBKG
            #print(self.lineEdit_2.text())           #SPIKE
            #print(self.dateEdit.text())             #start date
            #print(self.table2Csv(20))               #inputtable
            runNum = str(self.lineEdit_3.text())
            E = int(self.lineEdit.text())
            SPK = int(self.lineEdit_2.text())
            sampleP_list = self.table2Csv(20)
            path = 'listGen{}.csv'.format(runNum)
            print(pd.listPGen(E,SPK,sampleP_list))
            pd.csvWriter(path,pd.listPGen(E,SPK,sampleP_list))
            pd.pdfGen(runNum,pd.listPGen(E,SPK,sampleP_list),pd.timeCal(self.dateEdit.text()))
    
        elif self.PStatus == False:
            print('JRun')
            runNum = str(self.lineEdit_3.text())
            E = int(self.lineEdit.text())
            SPK = int(self.lineEdit_2.text())
            sampleP_list = self.table2Csv(19)
            path = 'listGen{}.csv'.format(runNum)
            print(pd.listJGen(E,SPK,sampleP_list))
            pd.csvWriter(path,pd.listJGen(E,SPK,sampleP_list))
            pd.pdfGen(runNum,pd.listJGen(E,SPK,sampleP_list),pd.timeCal(self.dateEdit.text()))
        else:
            print('Error')

    def plusOneButton(self):
        temp = self.tableWidget.currentItem()
        index = self.tableWidget.currentRow()
        new_cell = int(temp.text())+1
        self.tableWidget.setItem(index+1,0, QtWidgets.QTableWidgetItem(str(new_cell)))
        self.tableWidget.setCurrentCell(index+1,0)
    
    def repeatButton(self):
        temp = self.tableWidget.currentItem()
        index = self.tableWidget.currentRow()
        new_cell = temp.text() + '-R'
        self.tableWidget.setItem(index+1,0, QtWidgets.QTableWidgetItem(new_cell))
        self.tableWidget.setCurrentCell(index+1,0)

    def table2Csv(self,len):
        temp_list = []
        for i in range(len):
            if self.tableWidget.item(i,0).text():
                temp_list.append(self.tableWidget.item(i,0).text())
        return temp_list


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

