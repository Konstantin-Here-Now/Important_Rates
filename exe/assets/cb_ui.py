# Form implementation generated from reading ui file 'cb_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/cb_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 800))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: rgb(29, 29, 29);\n"
                                         "font: 16pt \"Times New Roman\";")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_rate_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.main_rate_widget.setStyleSheet("background-color: rgb(60, 60, 60);\n"
                                            "border-radius: 20px;\n"
                                            "font: bold;")
        self.main_rate_widget.setObjectName("main_rate_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_rate_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.constant_label_0 = QtWidgets.QLabel(parent=self.main_rate_widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.constant_label_0.setFont(font)
        self.constant_label_0.setAutoFillBackground(False)
        self.constant_label_0.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius: 20px;")
        self.constant_label_0.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.constant_label_0.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.constant_label_0.setLineWidth(1)
        self.constant_label_0.setMidLineWidth(0)
        self.constant_label_0.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.constant_label_0.setObjectName("constant_label_0")
        self.horizontalLayout.addWidget(self.constant_label_0)
        self.main_rate = QtWidgets.QLabel(parent=self.main_rate_widget)
        self.main_rate.setAutoFillBackground(False)
        self.main_rate.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius: 20px;")
        self.main_rate.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.main_rate.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.main_rate.setLineWidth(1)
        self.main_rate.setMidLineWidth(0)
        self.main_rate.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.main_rate.setObjectName("main_rate")
        self.horizontalLayout.addWidget(self.main_rate)
        self.verticalLayout_2.addWidget(self.main_rate_widget)
        self.other_rates_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.other_rates_widget.setStyleSheet("background-color: rgb(60, 60, 60);\n"
                                              "border-radius: 20px;")
        self.other_rates_widget.setObjectName("other_rates_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.other_rates_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.column_1 = QtWidgets.QVBoxLayout()
        self.column_1.setObjectName("column_1")
        self.constant_label_1 = QtWidgets.QLabel(parent=self.other_rates_widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.constant_label_1.setFont(font)
        self.constant_label_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius: 20px;\n"
                                            "font: bold;")
        self.constant_label_1.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.constant_label_1.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.constant_label_1.setLineWidth(1)
        self.constant_label_1.setMidLineWidth(0)
        self.constant_label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.constant_label_1.setObjectName("constant_label_1")
        self.column_1.addWidget(self.constant_label_1)
        self.constant_label_2 = QtWidgets.QLabel(parent=self.other_rates_widget)
        self.constant_label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(211, 211, 211);\n"
                                            "border-radius: 20px;")
        self.constant_label_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.constant_label_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.constant_label_2.setLineWidth(1)
        self.constant_label_2.setMidLineWidth(0)
        self.constant_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.constant_label_2.setObjectName("constant_label_2")
        self.column_1.addWidget(self.constant_label_2)
        self.constant_label_3 = QtWidgets.QLabel(parent=self.other_rates_widget)
        self.constant_label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(211, 211, 211);\n"
                                            "border-radius: 20px;")
        self.constant_label_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.constant_label_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.constant_label_3.setLineWidth(1)
        self.constant_label_3.setMidLineWidth(0)
        self.constant_label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.constant_label_3.setObjectName("constant_label_3")
        self.column_1.addWidget(self.constant_label_3)
        self.constant_label_4 = QtWidgets.QLabel(parent=self.other_rates_widget)
        self.constant_label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(211, 211, 211);\n"
                                            "border-radius: 20px;")
        self.constant_label_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.constant_label_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.constant_label_4.setLineWidth(1)
        self.constant_label_4.setMidLineWidth(0)
        self.constant_label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.constant_label_4.setObjectName("constant_label_4")
        self.column_1.addWidget(self.constant_label_4)
        self.horizontalLayout_2.addLayout(self.column_1)
        self.column_2 = QtWidgets.QVBoxLayout()
        self.column_2.setObjectName("column_2")
        self.previous_date = QtWidgets.QLabel(parent=self.other_rates_widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.previous_date.setFont(font)
        self.previous_date.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius: 20px;\n"
                                         "font: bold;")
        self.previous_date.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.previous_date.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.previous_date.setLineWidth(1)
        self.previous_date.setMidLineWidth(0)
        self.previous_date.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.previous_date.setObjectName("previous_date")
        self.column_2.addWidget(self.previous_date)
        self.previous_usd = QtWidgets.QLabel(parent=self.other_rates_widget)
        self.previous_usd.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(211, 211, 211);\n"
                                        "border-radius: 20px;")
        self.previous_usd.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.previous_usd.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.previous_usd.setLineWidth(1)
        self.previous_usd.setMidLineWidth(0)
        self.previous_usd.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.previous_usd.setObjectName("previous_usd")
        self.column_2.addWidget(self.previous_usd)
        self.previous_eur = QtWidgets.QLabel(parent=self.other_rates_widget)
        self.previous_eur.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(211, 211, 211);\n"
                                        "border-radius: 20px;")
        self.previous_eur.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.previous_eur.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.previous_eur.setLineWidth(1)
        self.previous_eur.setMidLineWidth(0)
        self.previous_eur.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.previous_eur.setObjectName("previous_eur")
        self.column_2.addWidget(self.previous_eur)
        self.previous_cny = QtWidgets.QLabel(parent=self.other_rates_widget)
        self.previous_cny.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(211, 211, 211);\n"
                                        "border-radius: 20px;")
        self.previous_cny.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.previous_cny.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.previous_cny.setLineWidth(1)
        self.previous_cny.setMidLineWidth(0)
        self.previous_cny.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.previous_cny.setObjectName("previous_cny")
        self.column_2.addWidget(self.previous_cny)
        self.horizontalLayout_2.addLayout(self.column_2)
        self.column_3 = QtWidgets.QVBoxLayout()
        self.column_3.setObjectName("column_3")
        self.current_date = QtWidgets.QLabel(parent=self.other_rates_widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.current_date.setFont(font)
        self.current_date.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 20px;\n"
                                        "font: bold;")
        self.current_date.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.current_date.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.current_date.setLineWidth(1)
        self.current_date.setMidLineWidth(0)
        self.current_date.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.current_date.setObjectName("current_date")
        self.column_3.addWidget(self.current_date)
        self.current_usd = QtWidgets.QLabel(parent=self.other_rates_widget)
        self.current_usd.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                       "color: rgb(211, 211, 211);\n"
                                       "border-radius: 20px;")
        self.current_usd.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.current_usd.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.current_usd.setLineWidth(1)
        self.current_usd.setMidLineWidth(0)
        self.current_usd.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.current_usd.setObjectName("current_usd")
        self.column_3.addWidget(self.current_usd)
        self.current_eur = QtWidgets.QLabel(parent=self.other_rates_widget)
        self.current_eur.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                       "color: rgb(211, 211, 211);\n"
                                       "border-radius: 20px;")
        self.current_eur.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.current_eur.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.current_eur.setLineWidth(1)
        self.current_eur.setMidLineWidth(0)
        self.current_eur.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.current_eur.setObjectName("current_eur")
        self.column_3.addWidget(self.current_eur)
        self.current_cny = QtWidgets.QLabel(parent=self.other_rates_widget)
        self.current_cny.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                       "color: rgb(211, 211, 211);\n"
                                       "border-radius: 20px;")
        self.current_cny.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.current_cny.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.current_cny.setLineWidth(1)
        self.current_cny.setMidLineWidth(0)
        self.current_cny.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.current_cny.setObjectName("current_cny")
        self.column_3.addWidget(self.current_cny)
        self.horizontalLayout_2.addLayout(self.column_3)
        self.verticalLayout_2.addWidget(self.other_rates_widget)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.moex_widget = QtWidgets.QWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.moex_widget.setFont(font)
        self.moex_widget.setStyleSheet("background-color: rgb(100, 100, 100);\n"
                                       "border-radius: 20px;")
        self.moex_widget.setObjectName("moex_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.moex_widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.constant_logo_label = QtWidgets.QLabel(parent=self.moex_widget)
        self.constant_logo_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                               "color: rgb(211, 211, 211);\n"
                                               "border-radius: 20px;\n"
                                               "font: bold;")
        self.constant_logo_label.setText("")
        self.constant_logo_label.setPixmap(QtGui.QPixmap("assets/moex_logo.png"))
        self.constant_logo_label.setScaledContents(False)
        self.constant_logo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.constant_logo_label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.constant_logo_label.setObjectName("constant_logo_label")
        self.verticalLayout.addWidget(self.constant_logo_label)
        self.moex_update_btn = QtWidgets.QPushButton(parent=self.moex_widget)
        self.moex_update_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.moex_update_btn.setStyleSheet("QPushButton {\n"
                                           "    font: bold;\n"
                                           "    background-color: rgb(90, 115, 205);\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    border-style: outset;\n"
                                           "    border-radius: 10px;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    font: bold;\n"
                                           "    background-color: rgb(112, 145, 255);\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    border-style: outset;\n"
                                           "    border-radius: 10px;\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    font: bold;\n"
                                           "    background-color: rgb(54, 69, 205);\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    border-style: outset;\n"
                                           "    border-radius: 10px;\n"
                                           "}")
        self.moex_update_btn.setDefault(False)
        self.moex_update_btn.setObjectName("moex_update_btn")
        self.verticalLayout.addWidget(self.moex_update_btn)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.moex_rates_layout = QtWidgets.QVBoxLayout()
        self.moex_rates_layout.setObjectName("moex_rates_layout")
        self.usd_layout_moex = QtWidgets.QHBoxLayout()
        self.usd_layout_moex.setObjectName("usd_layout_moex")
        self.contant_label_6 = QtWidgets.QLabel(parent=self.moex_widget)
        self.contant_label_6.setStyleSheet("font: bold;\n"
                                           "background-color: rgba(255, 255, 255, 0);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-radius: 20px;")
        self.contant_label_6.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.contant_label_6.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.contant_label_6.setLineWidth(1)
        self.contant_label_6.setMidLineWidth(0)
        self.contant_label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.contant_label_6.setObjectName("contant_label_6")
        self.usd_layout_moex.addWidget(self.contant_label_6)
        self.moex_usd = QtWidgets.QLabel(parent=self.moex_widget)
        self.moex_usd.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-radius: 20px;")
        self.moex_usd.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.moex_usd.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.moex_usd.setLineWidth(1)
        self.moex_usd.setMidLineWidth(0)
        self.moex_usd.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.moex_usd.setObjectName("moex_usd")
        self.usd_layout_moex.addWidget(self.moex_usd)
        self.moex_rates_layout.addLayout(self.usd_layout_moex)
        self.eur_layout_moex = QtWidgets.QHBoxLayout()
        self.eur_layout_moex.setObjectName("eur_layout_moex")
        self.contant_label_7 = QtWidgets.QLabel(parent=self.moex_widget)
        self.contant_label_7.setStyleSheet("font: bold;\n"
                                           "background-color: rgba(255, 255, 255, 0);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-radius: 20px;")
        self.contant_label_7.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.contant_label_7.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.contant_label_7.setLineWidth(1)
        self.contant_label_7.setMidLineWidth(0)
        self.contant_label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.contant_label_7.setObjectName("contant_label_7")
        self.eur_layout_moex.addWidget(self.contant_label_7)
        self.moex_eur = QtWidgets.QLabel(parent=self.moex_widget)
        self.moex_eur.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-radius: 20px;")
        self.moex_eur.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.moex_eur.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.moex_eur.setLineWidth(1)
        self.moex_eur.setMidLineWidth(0)
        self.moex_eur.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.moex_eur.setObjectName("moex_eur")
        self.eur_layout_moex.addWidget(self.moex_eur)
        self.moex_rates_layout.addLayout(self.eur_layout_moex)
        self.horizontalLayout_3.addLayout(self.moex_rates_layout)
        self.verticalLayout_2.addWidget(self.moex_widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rates"))
        self.constant_label_0.setText(_translate("MainWindow", "Ключевая ставка ЦБ"))
        self.main_rate.setText(_translate("MainWindow", "main_rate"))
        self.constant_label_1.setText(_translate("MainWindow", "ЦБ РФ"))
        self.constant_label_2.setText(_translate("MainWindow", "USD"))
        self.constant_label_3.setText(_translate("MainWindow", "EUR"))
        self.constant_label_4.setText(_translate("MainWindow", "CNY"))
        self.previous_date.setText(_translate("MainWindow", "previous_date"))
        self.previous_usd.setText(_translate("MainWindow", "previous_usd"))
        self.previous_eur.setText(_translate("MainWindow", "previous_eur"))
        self.previous_cny.setText(_translate("MainWindow", "previous_cny"))
        self.current_date.setText(_translate("MainWindow", "current_date"))
        self.current_usd.setText(_translate("MainWindow", "current_usd"))
        self.current_eur.setText(_translate("MainWindow", "current_eur"))
        self.current_cny.setText(_translate("MainWindow", "current_cny"))
        self.moex_update_btn.setText(_translate("MainWindow", "Обновить"))
        self.contant_label_6.setText(_translate("MainWindow", "USD"))
        self.moex_usd.setText(_translate("MainWindow", "moex_usd"))
        self.contant_label_7.setText(_translate("MainWindow", "EUR"))
        self.moex_eur.setText(_translate("MainWindow", "moex_eur"))