# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\nvidia_tacotron_TTS_Layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 1, 0, 1, 1)
        self.WGModelCombo = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WGModelCombo.sizePolicy().hasHeightForWidth())
        self.WGModelCombo.setSizePolicy(sizePolicy)
        self.WGModelCombo.setObjectName("WGModelCombo")
        self.gridLayout_5.addWidget(self.WGModelCombo, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.TTModelCombo = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TTModelCombo.sizePolicy().hasHeightForWidth())
        self.TTModelCombo.setSizePolicy(sizePolicy)
        self.TTModelCombo.setObjectName("TTModelCombo")
        self.gridLayout_5.addWidget(self.TTModelCombo, 0, 2, 1, 1)
        self.LoadTTButton = QtWidgets.QToolButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadTTButton.sizePolicy().hasHeightForWidth())
        self.LoadTTButton.setSizePolicy(sizePolicy)
        self.LoadTTButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LoadTTButton.setObjectName("LoadTTButton")
        self.gridLayout_5.addWidget(self.LoadTTButton, 0, 3, 1, 1)
        self.LoadWGButton = QtWidgets.QToolButton(self.tab)
        self.LoadWGButton.setObjectName("LoadWGButton")
        self.gridLayout_5.addWidget(self.LoadWGButton, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.TTSTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.TTSTextEdit.setObjectName("TTSTextEdit")
        self.verticalLayout.addWidget(self.TTSTextEdit)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 1)
        self.progressBarLabel = QtWidgets.QLabel(self.tab)
        self.progressBarLabel.setObjectName("progressBarLabel")
        self.gridLayout_2.addWidget(self.progressBarLabel, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 0, 1, 1)
        self.TTSExportWavButton = QtWidgets.QPushButton(self.tab)
        self.TTSExportWavButton.setObjectName("TTSExportWavButton")
        self.gridLayout_4.addWidget(self.TTSExportWavButton, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        self.TTSDialogButton = QtWidgets.QPushButton(self.tab)
        self.TTSDialogButton.setObjectName("TTSDialogButton")
        self.gridLayout_4.addWidget(self.TTSDialogButton, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        self.TTSStopButton = QtWidgets.QPushButton(self.tab)
        self.TTSStopButton.setObjectName("TTSStopButton")
        self.gridLayout_4.addWidget(self.TTSStopButton, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.log_window1 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_window1.sizePolicy().hasHeightForWidth())
        self.log_window1.setSizePolicy(sizePolicy)
        self.log_window1.setMinimumSize(QtCore.QSize(0, 39))
        self.log_window1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.log_window1.setObjectName("log_window1")
        self.verticalLayout.addWidget(self.log_window1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.ChannelName = QtWidgets.QLineEdit(self.tab_2)
        self.ChannelName.setObjectName("ChannelName")
        self.gridLayout.addWidget(self.ChannelName, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.APIKeyLine = QtWidgets.QLineEdit(self.tab_2)
        self.APIKeyLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.APIKeyLine.setObjectName("APIKeyLine")
        self.gridLayout.addWidget(self.APIKeyLine, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.ClientStartBtn = QtWidgets.QPushButton(self.tab_2)
        self.ClientStartBtn.setObjectName("ClientStartBtn")
        self.horizontalLayout_2.addWidget(self.ClientStartBtn)
        self.ClientStopBtn = QtWidgets.QPushButton(self.tab_2)
        self.ClientStopBtn.setObjectName("ClientStopBtn")
        self.horizontalLayout_2.addWidget(self.ClientStopBtn, 0, QtCore.Qt.AlignRight)
        self.ClientSkipBtn = QtWidgets.QPushButton(self.tab_2)
        self.ClientSkipBtn.setObjectName("ClientSkipBtn")
        self.horizontalLayout_2.addWidget(self.ClientSkipBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.ClientAmountLine = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.ClientAmountLine.setObjectName("ClientAmountLine")
        self.verticalLayout_2.addWidget(self.ClientAmountLine)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.log_window2 = QtWidgets.QPlainTextEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_window2.sizePolicy().hasHeightForWidth())
        self.log_window2.setSizePolicy(sizePolicy)
        self.log_window2.setAutoFillBackground(False)
        self.log_window2.setObjectName("log_window2")
        self.verticalLayout_2.addWidget(self.log_window2)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.progressBar2 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar2.setProperty("value", 0)
        self.progressBar2.setTextVisible(True)
        self.progressBar2.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar2.setObjectName("progressBar2")
        self.gridLayout_6.addWidget(self.progressBar2, 0, 0, 1, 1)
        self.progressBar2Label = QtWidgets.QLabel(self.tab_2)
        self.progressBar2Label.setObjectName("progressBar2Label")
        self.gridLayout_6.addWidget(self.progressBar2Label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.OptLimitCpuBtn = QtWidgets.QCheckBox(self.groupBox)
        self.OptLimitCpuBtn.setMaximumSize(QtCore.QSize(67, 17))
        self.OptLimitCpuBtn.setObjectName("OptLimitCpuBtn")
        self.gridLayout_7.addWidget(self.OptLimitCpuBtn, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem6, 0, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setMaximumSize(QtCore.QSize(43, 16777215))
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 0, 2, 1, 1)
        self.OptLimitCpuCombo = QtWidgets.QComboBox(self.groupBox)
        self.OptLimitCpuCombo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OptLimitCpuCombo.sizePolicy().hasHeightForWidth())
        self.OptLimitCpuCombo.setSizePolicy(sizePolicy)
        self.OptLimitCpuCombo.setMaximumSize(QtCore.QSize(30, 20))
        self.OptLimitCpuCombo.setObjectName("OptLimitCpuCombo")
        self.gridLayout_7.addWidget(self.OptLimitCpuCombo, 0, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem7, 0, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.OptDonoNameAmountBtn = QtWidgets.QCheckBox(self.groupBox_2)
        self.OptDonoNameAmountBtn.setChecked(True)
        self.OptDonoNameAmountBtn.setObjectName("OptDonoNameAmountBtn")
        self.verticalLayout_5.addWidget(self.OptDonoNameAmountBtn)
        self.OptApproveDonoBtn = QtWidgets.QCheckBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OptApproveDonoBtn.sizePolicy().hasHeightForWidth())
        self.OptApproveDonoBtn.setSizePolicy(sizePolicy)
        self.OptApproveDonoBtn.setChecked(True)
        self.OptApproveDonoBtn.setObjectName("OptApproveDonoBtn")
        self.verticalLayout_5.addWidget(self.OptApproveDonoBtn)
        self.OptBlockNumberBtn = QtWidgets.QCheckBox(self.groupBox_2)
        self.OptBlockNumberBtn.setObjectName("OptBlockNumberBtn")
        self.verticalLayout_5.addWidget(self.OptBlockNumberBtn)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.statusbar = QtWidgets.QLabel(self.centralwidget)
        self.statusbar.setObjectName("statusbar")
        self.gridLayout_3.addWidget(self.statusbar, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.setWindowTitle("Tacotron2 + Waveglow GUI v0.3.1")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Waveglow Model:"))
        self.label_7.setText(_translate("MainWindow", "Tacotron 2 Model:"))
        self.LoadTTButton.setText(_translate("MainWindow", "Browse..."))
        self.LoadWGButton.setText(_translate("MainWindow", "Browse..."))
        self.label.setText(_translate("MainWindow", "GPU Mode (Requires CUDA)"))
        self.label_2.setText(_translate("MainWindow", "Enter Text to speech:"))
        self.progressBarLabel.setText(_translate("MainWindow", "TextLabel"))
        self.TTSExportWavButton.setText(_translate("MainWindow", "Export .wav"))
        self.TTSDialogButton.setText(_translate("MainWindow", "Start"))
        self.TTSStopButton.setText(_translate("MainWindow", "Stop"))
        self.log_window1.setText(_translate("MainWindow", "Begin by loading a voice model"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Text to Speech"))
        self.label_5.setText(_translate("MainWindow", "Channel name"))
        self.label_3.setText(_translate("MainWindow", "StreamElements JWT Token"))
        self.ClientStartBtn.setText(_translate("MainWindow", "Start"))
        self.ClientStopBtn.setText(_translate("MainWindow", "Stop"))
        self.ClientSkipBtn.setText(_translate("MainWindow", "Skip"))
        self.label_8.setText(_translate("MainWindow", "Minimum amount for TTS:"))
        self.label_4.setText(_translate("MainWindow", "Status:"))
        self.progressBar2Label.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "StreamElements"))
        self.groupBox.setTitle(_translate("MainWindow", "Pytorch"))
        self.OptLimitCpuBtn.setText(_translate("MainWindow", "Limit CPU"))
        self.label_10.setText(_translate("MainWindow", "Threads:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "StreamElement"))
        self.OptDonoNameAmountBtn.setText(_translate("MainWindow", "Read donor\'s name and amount"))
        self.OptApproveDonoBtn.setText(_translate("MainWindow", "Approved donations only"))
        self.OptBlockNumberBtn.setText(_translate("MainWindow", "Block large numbers (>8 digits)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Options"))
        self.statusbar.setText(_translate("MainWindow", "Ready"))
        self.label_6.setText(_translate("MainWindow", "v0.3.1"))
