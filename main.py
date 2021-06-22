
from PyQt5 import QtCore, QtGui, QtWidgets
import mainWindow as gui
from PyQt5.QtWidgets import QLineEdit,QDialog,QDialogButtonBox,QFormLayout
import pdf as pd

class mainWindow(QtWidgets.QMainWindow,gui.Ui_MainWindow):
    def __init__(self):
        super(mainWindow,self).__init__()
        self.setupUi(self)

        #all customized funcs insert here
        self.radioButton.toggled.connect(lambda:self.onClicked(self.radioButton))       #radio button
        self.radioButton_2.toggled.connect(lambda:self.onClicked(self.radioButton_2))   #radio buttom
        self.pushButton.clicked.connect(self.buttonClicked)             #pdfGen buttom
        self.pushButton_2.clicked.connect(self.plusOneButton)           #plusOne buttom
        self.pushButton_3.clicked.connect(self.repeatButton)            #repeat buttom
    
    #selecting PRun or JRun
    def onClicked(self,b):
        if b.text() == 'PRun':
            self.PStatus = True
        elif b.text() == 'JRun':
            self.PStatus = False
        else:
            print ("Error")

    #pdfGen event
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
            path = '../E3H/PRun/Run {}.xlsx'.format(runNum)           #path for the data correction excel
            path_w = '../weightRecord/data/{}.csv'.format(runNum)     #path for weight recording csv
            #path = 'listGen{}.csv'.format(runNum)
            print(pd.listGen(E,SPK,sampleP_list))
            dpm = pd.dpmCal(self.calendarWidget.selectedDate().year(),self.calendarWidget.selectedDate().month())
            print(dpm)
            pd.csvWriter("P",path,pd.listGen(E,SPK,sampleP_list),runNum,dpm)
            pd.weightCsvWriter(path_w,pd.listGen(E,SPK,sampleP_list))
            pd.pdfGen(runNum,pd.listGen(E,SPK,sampleP_list),self.dateCal(),dpm)
            
    
        elif self.PStatus == False:
            print('JRun')
            runNum = str(self.lineEdit_3.text())
            E = int(self.lineEdit.text())
            SPK = int(self.lineEdit_2.text())
            sampleP_list = self.table2Csv(20)
            path = '../E3H/JRun/Run {}.xlsx'.format(runNum)
            path_w = '../weightRecord/data/{}.csv'.format(runNum)     #path for weight recording csv
            #path = 'listGen{}.csv'.format(runNum)
            print(pd.listGen(E,SPK,sampleP_list))
            dpm = pd.dpmCal(self.calendarWidget.selectedDate().year(),self.calendarWidget.selectedDate().month())
            pd.csvWriter("J",path,pd.listGen(E,SPK,sampleP_list),runNum,dpm)
            pd.weightCsvWriter(path_w,pd.listGen(E,SPK,sampleP_list))
            pd.pdfGen(runNum,pd.listGen(E,SPK,sampleP_list),self.dateCal(),dpm) 
        else:
            print('Error')

    #startDate and endDate
    def dateCal(self):
        date_start = self.calendarWidget.selectedDate()
        date_end = date_start.addDays(5)
        return [date_start.toString(),date_end.toString()]

    #plusOne button event
    def plusOneButton(self):
        temp = self.tableWidget.currentItem()
        index = self.tableWidget.currentRow()
        if index <19:
            new_cell = int(temp.text().split('-')[0])+1
            self.tableWidget.setItem(index+1,0, QtWidgets.QTableWidgetItem(str(new_cell)))
            self.tableWidget.setCurrentCell(index+1,0)
        else:
            print('out of limit!')
    
    #repeat button event
    def repeatButton(self):
        temp = self.tableWidget.currentItem()
        index = self.tableWidget.currentRow()
        new_cell = temp.text() + '-R'
        self.tableWidget.setItem(index+1,0, QtWidgets.QTableWidgetItem(new_cell))
        self.tableWidget.setCurrentCell(index+1,0)

    #transfer input table to csv format
    def table2Csv(self,len):
        temp_list = []
        for i in range(len):
            if self.tableWidget.item(i,0).text():
                temp_list.append(self.tableWidget.item(i,0).text())
        return temp_list


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = mainWindow()
    w.show()
    sys.exit(app.exec_())
