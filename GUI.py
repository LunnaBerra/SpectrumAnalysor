# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Datahanterings_GUITwVxos.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################x
#
import csv
import os
import sys
from time import sleep


from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg


# import Test
import Test



class Ui_MainWindow(object):
    app = QApplication(sys.argv)
    abort_test = False
    stopOnDeviation = True
    saveDeviatedSamples = True
    timeType = "ms"
    freqCenterType = "Hz"
    freqCenter = 0
    freqSpanType = "Hz"
    freqSpan = 0
    ampLowType = "dBm"
    ampLow = 0
    ampHighType = "dBm"
    ampHigh = 0
    onlyInt = QIntValidator()
    endTime = 0

    def __init__(self):
        win = QMainWindow()
        win.setObjectName("MainWindow")
        self.setupUi(win)
        win.show()
        sys.exit(self.app.exec_())

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1135, 864)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-1, -1, 1101, 811))

        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.frame_3 = QFrame(self.gridLayoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.plotDisplay = pg.PlotWidget(self.frame_3)
        self.plotDisplay.setObjectName(u"plotDisplay")
        self.plotDisplay.setGeometry(QRect(0, 10, 541, 391))
        self.plotDisplay.setLabel('bottom', "Frequency")
        self.plotDisplay.setLabel('left', "dBm")
        self.plotDisplay.setLabel('top', "Frequency Spectrum")

        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame = QFrame(self.gridLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.welcomeText = QPlainTextEdit(self.frame)
        self.welcomeText.setObjectName(u"welcomeText")
        self.welcomeText.setGeometry(QRect(-5, 10, 551, 391))
        self.welcomeText.setReadOnly(True)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.gridLayoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.valuesDisplay = QTableWidget(self.frame_4)
        self.valuesDisplay.setObjectName(u"valuesDisplay")
        self.valuesDisplay.setGeometry(QRect(0, 0, 541, 401))
        self.valuesDisplay.setColumnCount(2)
        self.valuesDisplay.setRowCount(1)
        self.valuesDisplay.setItem(0, 0, QTableWidgetItem("Frequency (Hz)"))
        self.valuesDisplay.setItem(0, 1, QTableWidgetItem("Amplitude (dBm)"))

        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.gridLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.freqCenterInput = QLineEdit(self.frame_2)
        self.freqCenterInput.setObjectName(u"freqCenterInput")
        self.freqCenterInput.setGeometry(QRect(0, 30, 281, 22))
        self.freqCenterInput.setValidator(self.onlyInt)

        self.freqSpanInput = QLineEdit(self.frame_2)
        self.freqSpanInput.setObjectName(u"freqSpanInput")
        self.freqSpanInput.setGeometry(QRect(0, 50, 281, 22))
        self.freqSpanInput.setValidator(self.onlyInt)

        self.lowAmpInput = QLineEdit(self.frame_2)
        self.lowAmpInput.setObjectName(u"lowAmpInput")
        self.lowAmpInput.setGeometry(QRect(0, 70, 281, 22))
        self.lowAmpInput.setValidator(self.onlyInt)

        self.highAmpInput = QLineEdit(self.frame_2)
        self.highAmpInput.setObjectName(u"highAmpInput")
        self.highAmpInput.setGeometry(QRect(0, 90, 281, 22))
        self.highAmpInput.setValidator(self.onlyInt)

        self.freqSize1 = QComboBox(self.frame_2)
        self.freqSize1.addItem("Hz")
        self.freqSize1.addItem("KHz")
        self.freqSize1.addItem("MHz")
        self.freqSize1.addItem("GHz")
        self.freqSize1.setObjectName(u"freqSize1")
        self.freqSize1.setGeometry(QRect(280, 30, 261, 22))
        self.freqSize1.currentIndexChanged.connect(self.freq_type_changed_1)

        self.freqSize2 = QComboBox(self.frame_2)
        self.freqSize2.addItem("Hz")
        self.freqSize2.addItem("KHz")
        self.freqSize2.addItem("MHz")
        self.freqSize2.addItem("GHz")
        self.freqSize2.setObjectName(u"freqSize2")
        self.freqSize2.setGeometry(QRect(280, 50, 261, 22))
        self.freqSize2.currentIndexChanged.connect(self.freq_type_changed_2)

        self.ampSize1 = QComboBox(self.frame_2)
        self.ampSize1.addItem("dBm")
        self.ampSize1.addItem("V")
        self.ampSize1.setObjectName(u"ampSize1")
        self.ampSize1.setGeometry(QRect(280, 70, 261, 22))
        self.ampSize1.currentIndexChanged.connect(self.amp_type_changed_1)

        self.ampSize2 = QComboBox(self.frame_2)
        self.ampSize2.addItem("dBm")
        self.ampSize2.addItem("V")
        self.ampSize2.setObjectName(u"ampSize2")
        self.ampSize2.setGeometry(QRect(280, 90, 261, 22))
        self.ampSize2.currentIndexChanged.connect(self.amp_type_changed_2)

        self.freqAmpSettingsTitle = QTextBrowser(self.frame_2)
        self.freqAmpSettingsTitle.setObjectName(u"freqAmpSettingsTitle")
        self.freqAmpSettingsTitle.setGeometry(QRect(0, 0, 541, 31))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush1 = QBrush(QColor(0, 0, 0, 128))
        brush1.setStyle(Qt.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
        # endif
        brush2 = QBrush(QColor(9, 9, 9, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
        # endif
        self.freqAmpSettingsTitle.setPalette(palette)
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.freqAmpSettingsTitle.setFont(font)
        self.freqAmpSettingsTitle.setAutoFillBackground(False)
        self.freqAmpSettingsTitle.setPlaceholderText(u"")

        self.testingSettingsTitle = QTextBrowser(self.frame_2)
        self.testingSettingsTitle.setObjectName(u"testingSettingsTitle")
        self.testingSettingsTitle.setGeometry(QRect(0, 130, 541, 31))
        self.testingSettingsTitle.setFont(font)
        self.testingSettingsTitle.setAutoFillBackground(False)
        self.testingSettingsTitle.setPlaceholderText(u"Testing Settings")

        self.testTimeInput = QLineEdit(self.frame_2)
        self.testTimeInput.setObjectName(u"testTimeInput")
        self.testTimeInput.setGeometry(QRect(0, 160, 281, 22))
        self.testTimeInput.setValidator(self.onlyInt)

        self.timeSize = QComboBox(self.frame_2)
        self.timeSize.addItem("ms")
        self.timeSize.addItem("s")
        self.timeSize.addItem("min")
        self.timeSize.setObjectName(u"timeSize")
        self.timeSize.setGeometry(QRect(280, 160, 261, 22))
        self.timeSize.currentIndexChanged.connect(self.time_type_changed)

        self.stopOnDeviationLabel = QLineEdit(self.frame_2)
        self.stopOnDeviationLabel.setObjectName(u"stopOnDeviationLabel")
        self.stopOnDeviationLabel.setGeometry(QRect(0, 180, 281, 22))
        self.stopOnDeviationLabel.setReadOnly(True)

        self.yesNo1 = QComboBox(self.frame_2)
        self.yesNo1.addItem("Yes")
        self.yesNo1.addItem("No")
        self.yesNo1.setObjectName(u"yesNo1")
        self.yesNo1.setGeometry(QRect(280, 180, 261, 22))
        self.yesNo1.currentIndexChanged.connect(self.yes_no_1_changed)

        self.yesNo2 = QComboBox(self.frame_2)
        self.yesNo2.addItem("Yes")
        self.yesNo2.addItem("No")
        self.yesNo2.setObjectName(u"yesNo2")
        self.yesNo2.setGeometry(QRect(280, 200, 261, 22))
        self.yesNo2.currentIndexChanged.connect(self.yes_no_2_changed)

        self.saveDeviatedSamplesLabel = QLineEdit(self.frame_2)
        self.saveDeviatedSamplesLabel.setObjectName(u"saveDeviatedSamplesLabel")
        self.saveDeviatedSamplesLabel.setGeometry(QRect(0, 200, 281, 22))
        self.saveDeviatedSamplesLabel.setReadOnly(True)

        self.startTestButton = QPushButton(self.frame_2)
        self.startTestButton.setObjectName(u"startTestButton")
        self.startTestButton.setGeometry(QRect(450, 340, 93, 61))
        self.startTestButton.clicked.connect(self.pressed_start_test)

        self.abortTestButton = QPushButton(self.frame_2)
        self.abortTestButton.setObjectName(u"abortTestButton")
        self.abortTestButton.setGeometry(QRect(360, 340, 93, 61))
        self.abortTestButton.clicked.connect(self.pressed_abort_test)

        self.plotButton = QPushButton(self.frame_2)
        self.plotButton.setObjectName(u"plotButton")
        self.plotButton.setGeometry(QRect(270, 340, 93, 61))
        self.plotButton.clicked.connect(self.pressed_plot)

        self.plotSettingsTitle = QTextBrowser(self.frame_2)
        self.plotSettingsTitle.setObjectName(u"plotSettingsTitle")
        self.plotSettingsTitle.setGeometry(QRect(0, 240, 541, 31))
        self.plotSettingsTitle.setFont(font)
        self.plotSettingsTitle.setAutoFillBackground(False)
        self.plotSettingsTitle.setPlaceholderText(u"")

        self.selectedPlotFile = QLineEdit(self.frame_2)
        self.selectedPlotFile.setObjectName(u"selectedPlotFile")
        self.selectedPlotFile.setGeometry(QRect(0, 270, 541, 22))
        self.selectedPlotFile.setReadOnly(True)

        self.selectPlotFileButton = QPushButton(self.frame_2)
        self.selectPlotFileButton.setObjectName(u"selectPlotFileButton")
        self.selectPlotFileButton.setGeometry(QRect(520, 270, 21, 21))
        self.selectPlotFileButton.clicked.connect(self.get_file_name)

        self.clearPlotButton = QPushButton(self.frame_2)
        self.clearPlotButton.setObjectName(u"clearPlotButton")
        self.clearPlotButton.setGeometry(QRect(180, 340, 93, 61))
        self.clearPlotButton.clicked.connect(self.pressed_clear_plot)

        self.exitProgramButton = QPushButton(self.frame_2)
        self.exitProgramButton.setObjectName(u"exitProgramButton")
        self.exitProgramButton.setGeometry(QRect(0, 340, 93, 61))
        self.exitProgramButton.clicked.connect(self.pressed_exit)

        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1135, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def get_file_name(self):

        file_filter = 'Data file (*.csv)'
        response = QFileDialog.getOpenFileName(
            caption='Select a CSV file',
            directory=os.getcwd(),
            filter=file_filter
        )
        self.selectedPlotFile.setText(response[0])

    def update_status(self, message):
        self.welcomeText.appendPlainText(message)

    def clear_status(self):
        self.welcomeText.clear()

    def pressed_exit(self):
        self.update_status("The core temperature has reached critical levels. Please RUN FOR YOUR LIFE!!!!")
        self.app.quit()

    def pressed_start_test(self):
        self.clear_status()
        self.update_status("Commencing test sequence...")
        self.typeAdjustment()
        self.update_status("Type adjustment completed...")
        Test.testing(self.saveDeviatedSamples, self.endTime, self.freqCenter, self.freqSpan, self.stopOnDeviation,
                     self.abort_test, self.ampHigh, self.ampLow)
        if self.abort_test == False:
            self.update_status("Test sequence completed...")
        else:
            self.update_status("Test aborted...")
        self.abort_test = False

    def typeAdjustment(self):

        if len(self.testTimeInput.text()) == 0:
            self.endTime = 0
        elif self.timeType == "ms":
            self.endTime = float(self.testTimeInput.text()) / 1000
        elif self.timeType == "s":
            self.endTime = float(self.testTimeInput.text())
        elif self.timeType == "min":
            self.endTime = float(self.testTimeInput.text()) * 60

        if len(self.freqCenterInput.text()) == 0:
            self.freqCenter = 0
        elif self.freqCenterType == "Hz":
            self.freqCenter = float(self.freqCenterInput.text()) * 1
        elif self.freqCenterType == "KHz":
            self.freqCenter = float(self.freqCenterInput.text()) * 1000
        elif self.freqCenterType == "MHz":
            self.freqCenter = float(self.freqCenterInput.text()) * 1000 * 1000
        elif self.freqCenterType == "GHz":
            self.freqCenter = float(self.freqCenterInput.text()) * 1000 * 1000 * 1000

        if len(self.freqSpanInput.text()) == 0:
            self.freqSpan = 0
        elif self.freqSpanType == "Hz":
            self.freqSpan = float(self.freqSpanInput.text()) * 1
        elif self.freqSpanType == "KHz":
            self.freqSpan = float(self.freqSpanInput.text()) * 1000
        elif self.freqSpanType == "MHz":
            self.freqSpan = float(self.freqSpanInput.text()) * 1000 * 1000
        elif self.freqSpanType == "GHz":
            self.freqSpan = float(self.freqSpanInput.text()) * 1000 * 1000 * 1000

        if len(self.lowAmpInput.text()) == 0:
            self.ampLow = 0
        elif self.ampLowType == "dBm":
            self.ampLow = float(self.lowAmpInput.text())
        elif self.ampLowType == "V":
            self.ampLow = float(self.lowAmpInput.text())

        if len(self.highAmpInput.text()) == 0:
            self.ampHigh = 0
        elif self.ampHighType == "dBm":
            self.ampHigh = float(self.highAmpInput.text())
        elif self.ampHighType == "V":
            self.ampHigh = float(self.highAmpInput.text())

    def pressed_abort_test(self):
        self.abort_test = True

    def pressed_clear_plot(self):
        self.update_status("Plot cleared...")
        self.plotDisplay.clear()
        self.valuesDisplay.clear()
        self.valuesDisplay.setColumnCount(2)
        self.valuesDisplay.setRowCount(1)
        self.valuesDisplay.setItem(0, 0, QTableWidgetItem("Frequency (Hz)"))
        self.valuesDisplay.setItem(0, 1, QTableWidgetItem("Amplitude (dBm)"))

    def pressed_plot(self):
        self.clear_status()
        self.pressed_clear_plot()
        if len(self.selectPlotFileButton.text()) == 0:
            return
        fileDirectory = self.selectedPlotFile.text()
        print(fileDirectory)
        file = open(fileDirectory)
        csvreader = csv.reader(file)
        header = next(csvreader)
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
        file.close()

        freq = []
        amp = []
        self.valuesDisplay.setRowCount(len(rows) + 1)
        z = 1
        for x in rows:
            k = 0
            for i in x:
                if k == 0:
                    freq.append(float(i))
                    self.valuesDisplay.setItem(z, 0, QTableWidgetItem(i))
                elif k == 1:
                    amp.append(float(i))
                    self.valuesDisplay.setItem(z, 1, QTableWidgetItem(i))
                k = k + 1
            z = z + 1
        print(freq)
        print(amp)

        # plot data: x, y values
        self.plotDisplay.plot(freq, amp)
        self.update_status("Plot completed...")

    def yes_no_1_changed(self):
        if self.yesNo1.currentText() == "No":
            self.stopOnDeviation = False
        else:
            self.stopOnDeviation = True

    def yes_no_2_changed(self):
        if self.yesNo2.currentText() == "No":
            self.saveDeviatedSamples = False
        else:
            self.saveDeviatedSamples = True

    def time_type_changed(self):
        self.timeType = self.timeSize.currentText()

    def freq_type_changed_1(self):
        self.freqCenterType = self.freqSize1.currentText()

    def freq_type_changed_2(self):
        self.freqSpanType = self.freqSize2.currentText()

    def amp_type_changed_1(self):
        self.ampLowType = self.ampSize1.currentText()

    def amp_type_changed_2(self):
        self.ampHighType = self.ampSize2.currentText()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.welcomeText.setPlainText(QCoreApplication.translate("MainWindow", u" Welcome!\n"
                                                                                     " This is the operations GUI for the detection of GNSS tracers. The goal with the product is\n"
                                                                                     " to use antennas to detect the trackers that can be used to find people with protected\n"
                                                                                     " identities. This technology can hopefully be of use when protecting those in unfortunate\n"
                                                                                     " circumstances.\n"
                                                                                     " We hope that you will find the software easy to use.\n"
                                                                                     "\n"
                                                                                     " Prerequisites:\n"
                                                                                     " Spectrum Analyser FCP 1*00 from Rhode and Schwartz\n"
                                                                                     " An antenna setup connected to the spectrum analyser\n"
                                                                                     "\n"
                                                                                     " Thank you for using our product,\n"
                                                                                     " Regards,\n"
                                                                                     " The team behind GPSFinder",
                                                                       None))
        self.freqCenterInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Frequency Center", None))
        self.freqSpanInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Frequency Span", None))
        self.lowAmpInput.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Lower Amplitude Deviation", None))
        self.highAmpInput.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Upper Amplitude Deviation", None))
        self.freqSize1.setItemText(0, QCoreApplication.translate("MainWindow", u"Hz", None))
        self.freqSize1.setItemText(1, QCoreApplication.translate("MainWindow", u"KHz", None))
        self.freqSize1.setItemText(2, QCoreApplication.translate("MainWindow", u"MHz", None))
        self.freqSize1.setItemText(3, QCoreApplication.translate("MainWindow", u"GHz", None))

        self.freqSize2.setItemText(0, QCoreApplication.translate("MainWindow", u"Hz", None))
        self.freqSize2.setItemText(1, QCoreApplication.translate("MainWindow", u"KHz", None))
        self.freqSize2.setItemText(2, QCoreApplication.translate("MainWindow", u"MHz", None))
        self.freqSize2.setItemText(3, QCoreApplication.translate("MainWindow", u"GHz", None))

        self.ampSize1.setItemText(0, QCoreApplication.translate("MainWindow", u"dBm", None))
        self.ampSize1.setItemText(1, QCoreApplication.translate("MainWindow", u"V", None))

        self.ampSize2.setItemText(0, QCoreApplication.translate("MainWindow", u"dBm", None))
        self.ampSize2.setItemText(1, QCoreApplication.translate("MainWindow", u"V", None))

        self.freqAmpSettingsTitle.setDocumentTitle("")
        self.freqAmpSettingsTitle.setMarkdown(
            QCoreApplication.translate("MainWindow", u"**_Frequency and Amplitude Settings**_\n"
                                                     "\n"
                                                     "", None))
        self.testingSettingsTitle.setDocumentTitle("")
        self.testingSettingsTitle.setMarkdown(QCoreApplication.translate("MainWindow", u"**_Testing Settings**_\n"
                                                                                       "\n"
                                                                                       "", None))
        self.testTimeInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Test Time", None))
        self.timeSize.setItemText(0, QCoreApplication.translate("MainWindow", u"ms", None))
        self.timeSize.setItemText(1, QCoreApplication.translate("MainWindow", u"s", None))
        self.timeSize.setItemText(2, QCoreApplication.translate("MainWindow", u"min", None))

        self.stopOnDeviationLabel.setText(QCoreApplication.translate("MainWindow", u"Stop on Deviation:", None))
        self.stopOnDeviationLabel.setPlaceholderText("")
        self.yesNo1.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.yesNo1.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.yesNo2.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.yesNo2.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.saveDeviatedSamplesLabel.setText(QCoreApplication.translate("MainWindow", u"Save Deviated Samples:", None))
        self.saveDeviatedSamplesLabel.setPlaceholderText("")
        self.startTestButton.setText(QCoreApplication.translate("MainWindow", u"Start Test", None))
        self.abortTestButton.setText(QCoreApplication.translate("MainWindow", u"Abort Test", None))
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.plotSettingsTitle.setDocumentTitle("")
        self.plotSettingsTitle.setMarkdown(QCoreApplication.translate("MainWindow", u"**_Plot Settings**_\n"
                                                                                    "\n"
                                                                                    "", None))
        self.selectedPlotFile.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Plotted file", None))
        self.selectPlotFileButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.clearPlotButton.setText(QCoreApplication.translate("MainWindow", u"Clear Plot", None))
        self.exitProgramButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi
