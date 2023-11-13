from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
import pandas as pd


class Ui_ExcelPreview(object):
    def setupUi(self, ExcelPreview):
        ExcelPreview.setObjectName("ExcelPreview")
        ExcelPreview.resize(600, 400)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ExcelPreview)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(ExcelPreview)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)

        self.tableWidget.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setVerticalScrollBarPolicy(False)
        self.tableWidget.setHorizontalScrollBarPolicy(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        excel_file = '_dane/dane.xlsx'
        df = pd.read_excel(excel_file)
        df_bez_nr = df.drop("Zlecenie", axis=1)
        
        self.tableWidget.setRowCount(df_bez_nr.shape[0])
        self.tableWidget.setColumnCount(df_bez_nr.shape[1])

        for i in range(df_bez_nr.shape[0]):
            for j in range(df_bez_nr.shape[1]):
                item = QTableWidgetItem(str(df_bez_nr.iat[i,j]))
                self.tableWidget.setItem(i,j,item)

        for i in range(self.tableWidget.rowCount()):
            item = QTableWidgetItem(str(df["Zlecenie"].iloc[i]))
            self.tableWidget.setVerticalHeaderItem(i, item)

        self.tableWidget.setHorizontalHeaderLabels(df_bez_nr.columns.tolist())
        

        self.retranslateUi(ExcelPreview)
        QtCore.QMetaObject.connectSlotsByName(ExcelPreview)

    def retranslateUi(self, ExcelPreview):
        _translate = QtCore.QCoreApplication.translate
        ExcelPreview.setWindowTitle(_translate("ExcelPreview", "Podgląd Excela"))