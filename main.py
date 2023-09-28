from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(300, 500)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        form.setFont(font)
        form.setStyleSheet("background-color:black;")
        self.display = QtWidgets.QLabel(form)
        self.display.setGeometry(QtCore.QRect(0, 0, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.display.setFont(font)
        self.display.setStyleSheet("color:white;\n"
                                   "background-color:rgb(101, 106, 109);\n"
                                   "padding-left:27px;")
        self.display.setObjectName("display")
        self.btn_1 = QtWidgets.QPushButton(form)
        self.btn_1.setGeometry(QtCore.QRect(0, 120, 75, 75))
        self.btn_1.setStyleSheet("/* Style calculator buttons */\n"
                                 "QPushButton {\n"
                                 "    background-color: #FAAE3C; /* Light gray background color */\n"
                                 "    border: 1px solid #FAAE3C; /* Light gray border */\n"
                                 "    border-radius: 5px; /* Rounded corners */\n"
                                 "    font: bold 16px; /* Bold 16px font */\n"
                                 "    padding: 10px 20px; /* Padding around the text */\n"
                                 "    margin: 5px; /* Margin between buttons */\n"
                                 "\n"
                                 "    color: #333; /* Text color */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style hovered calculator buttons */\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #FAAE3C; /* Slightly darker gray background on hover */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style clicked calculator buttons */\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #FAAE3C; /* Even darker gray background on click */\n"
                                 "}")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(form)
        self.btn_2.setGeometry(QtCore.QRect(70, 120, 75, 75))
        self.btn_2.setStyleSheet("/* Style calculator buttons */\n"
                                 "QPushButton {\n"
                                 "    background-color: #FAAE3C; /* Light gray background color */\n"
                                 "    border: 1px solid #FAAE3C; /* Light gray border */\n"
                                 "    border-radius: 5px; /* Rounded corners */\n"
                                 "    font: bold 16px; /* Bold 16px font */\n"
                                 "    padding: 10px 20px; /* Padding around the text */\n"
                                 "    margin: 5px; /* Margin between buttons */\n"
                                 "\n"
                                 "    color: #333; /* Text color */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style hovered calculator buttons */\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #FAAE3C; /* Slightly darker gray background on hover */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style clicked calculator buttons */\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #FAAE3C; /* Even darker gray background on click */\n"
                                 "}")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(form)
        self.btn_3.setGeometry(QtCore.QRect(140, 120, 75, 75))
        self.btn_3.setStyleSheet("/* Style calculator buttons */\n"
                                 "QPushButton {\n"
                                 "    background-color: #FAAE3C; /* Light gray background color */\n"
                                 "    border: 1px solid #FAAE3C; /* Light gray border */\n"
                                 "    border-radius: 5px; /* Rounded corners */\n"
                                 "    font: bold 16px; /* Bold 16px font */\n"
                                 "    padding: 10px 20px; /* Padding around the text */\n"
                                 "    margin: 5px; /* Margin between buttons */\n"
                                 "\n"
                                 "    color: #333; /* Text color */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style hovered calculator buttons */\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #FAAE3C; /* Slightly darker gray background on hover */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style clicked calculator buttons */\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #FAAE3C; /* Even darker gray background on click */\n"
                                 "}")
        self.btn_3.setObjectName("btn_3")
        self.btn_divide = QtWidgets.QPushButton(form)
        self.btn_divide.setGeometry(QtCore.QRect(210, 120, 91, 75))
        self.btn_divide.setStyleSheet("/* Style calculator buttons */\n"
                                      "QPushButton {\n"
                                      "    background-color: #3CB7F0; /* Light gray background color */\n"
                                      "    border: 1px solid #3CB7F0; /* Light gray border */\n"
                                      "    border-radius: 5px; /* Rounded corners */\n"
                                      "    font: bold 16px; /* Bold 16px font */\n"
                                      "    padding: 10px 20px; /* Padding around the text */\n"
                                      "    margin: 5px; /* Margin between buttons */\n"
                                      "\n"
                                      "    color: #333; /* Text color */\n"
                                      "}\n"
                                      "\n"
                                      "/* Style hovered calculator buttons */\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #3CB7F0; /* Slightly darker gray background on hover */\n"
                                      "}\n"
                                      "\n"
                                      "/* Style clicked calculator buttons */\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: #3CB7F0; /* Even darker gray background on click */\n"
                                      "}")
        self.btn_divide.setObjectName("btn_divide")
        self.btn_4 = QtWidgets.QPushButton(form)
        self.btn_4.setGeometry(QtCore.QRect(0, 195, 75, 75))
        self.btn_4.setStyleSheet("/* Style calculator buttons */\n"
                                 "QPushButton {\n"
                                 "    background-color: #FAAE3C; /* Light gray background color */\n"
                                 "    border: 1px solid #FAAE3C; /* Light gray border */\n"
                                 "    border-radius: 5px; /* Rounded corners */\n"
                                 "    font: bold 16px; /* Bold 16px font */\n"
                                 "    padding: 10px 20px; /* Padding around the text */\n"
                                 "    margin: 5px; /* Margin between buttons */\n"
                                 "\n"
                                 "    color: #333; /* Text color */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style hovered calculator buttons */\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #FAAE3C; /* Slightly darker gray background on hover */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style clicked calculator buttons */\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #FAAE3C; /* Even darker gray background on click */\n"
                                 "}")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(form)
        self.btn_5.setGeometry(QtCore.QRect(70, 195, 75, 75))
        self.btn_5.setStyleSheet("/* Style calculator buttons */\n"
                                 "QPushButton {\n"
                                 "    background-color: #FAAE3C; /* Light gray background color */\n"
                                 "    border: 1px solid #FAAE3C; /* Light gray border */\n"
                                 "    border-radius: 5px; /* Rounded corners */\n"
                                 "    font: bold 16px; /* Bold 16px font */\n"
                                 "    padding: 10px 20px; /* Padding around the text */\n"
                                 "    margin: 5px; /* Margin between buttons */\n"
                                 "\n"
                                 "    color: #333; /* Text color */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style hovered calculator buttons */\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #FAAE3C; /* Slightly darker gray background on hover */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style clicked calculator buttons */\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #FAAE3C; /* Even darker gray background on click */\n"
                                 "}")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(form)
        self.btn_6.setGeometry(QtCore.QRect(140, 195, 75, 75))
        self.btn_6.setStyleSheet("/* Style calculator buttons */\n"
                                 "QPushButton {\n"
                                 "    background-color: #FAAE3C; /* Light gray background color */\n"
                                 "    border: 1px solid #FAAE3C; /* Light gray border */\n"
                                 "    border-radius: 5px; /* Rounded corners */\n"
                                 "    font: bold 16px; /* Bold 16px font */\n"
                                 "    padding: 10px 20px; /* Padding around the text */\n"
                                 "    margin: 5px; /* Margin between buttons */\n"
                                 "\n"
                                 "    color: #333; /* Text color */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style hovered calculator buttons */\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #FAAE3C; /* Slightly darker gray background on hover */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style clicked calculator buttons */\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #FAAE3C; /* Even darker gray background on click */\n"
                                 "}")
        self.btn_6.setObjectName("btn_6")
        self.btn_multiply = QtWidgets.QPushButton(form)
        self.btn_multiply.setGeometry(QtCore.QRect(210, 195, 91, 75))
        self.btn_multiply.setStyleSheet("/* Style calculator buttons */\n"
                                        "QPushButton {\n"
                                        "    background-color: #3CB7F0; /* Light gray background color */\n"
                                        "    border: 1px solid #3CB7F0; /* Light gray border */\n"
                                        "    border-radius: 5px; /* Rounded corners */\n"
                                        "    font: bold 16px; /* Bold 16px font */\n"
                                        "    padding: 10px 20px; /* Padding around the text */\n"
                                        "    margin: 5px; /* Margin between buttons */\n"
                                        "\n"
                                        "    color: #333; /* Text color */\n"
                                        "}\n"
                                        "\n"
                                        "/* Style hovered calculator buttons */\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #3CB7F0; /* Slightly darker gray background on hover */\n"
                                        "}\n"
                                        "\n"
                                        "/* Style clicked calculator buttons */\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #3CB7F0; /* Even darker gray background on click */\n"
                                        "}")
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_7 = QtWidgets.QPushButton(form)
        self.btn_7.setGeometry(QtCore.QRect(0, 270, 75, 75))
        self.btn_7.setStyleSheet("/* Style calculator buttons */\n"
                                 "QPushButton {\n"
                                 "    background-color: #FAAE3C; /* Light gray background color */\n"
                                 "    border: 1px solid #FAAE3C; /* Light gray border */\n"
                                 "    border-radius: 5px; /* Rounded corners */\n"
                                 "    font: bold 16px; /* Bold 16px font */\n"
                                 "    padding: 10px 20px; /* Padding around the text */\n"
                                 "    margin: 5px; /* Margin between buttons */\n"
                                 "\n"
                                 "    color: #333; /* Text color */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style hovered calculator buttons */\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #FAAE3C; /* Slightly darker gray background on hover */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style clicked calculator buttons */\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #FAAE3C; /* Even darker gray background on click */\n"
                                 "}")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(form)
        self.btn_8.setGeometry(QtCore.QRect(70, 270, 75, 75))
        self.btn_8.setStyleSheet("/* Style calculator buttons */\n"
                                 "QPushButton {\n"
                                 "    background-color: #FAAE3C; /* Light gray background color */\n"
                                 "    border: 1px solid #FAAE3C; /* Light gray border */\n"
                                 "    border-radius: 5px; /* Rounded corners */\n"
                                 "    font: bold 16px; /* Bold 16px font */\n"
                                 "    padding: 10px 20px; /* Padding around the text */\n"
                                 "    margin: 5px; /* Margin between buttons */\n"
                                 "\n"
                                 "    color: #333; /* Text color */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style hovered calculator buttons */\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #FAAE3C; /* Slightly darker gray background on hover */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style clicked calculator buttons */\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #FAAE3C; /* Even darker gray background on click */\n"
                                 "}")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(form)
        self.btn_9.setGeometry(QtCore.QRect(140, 270, 75, 75))
        self.btn_9.setStyleSheet("/* Style calculator buttons */\n"
                                 "QPushButton {\n"
                                 "    background-color: #FAAE3C; /* Light gray background color */\n"
                                 "    border: 1px solid #FAAE3C; /* Light gray border */\n"
                                 "    border-radius: 5px; /* Rounded corners */\n"
                                 "    font: bold 16px; /* Bold 16px font */\n"
                                 "    padding: 10px 20px; /* Padding around the text */\n"
                                 "    margin: 5px; /* Margin between buttons */\n"
                                 "\n"
                                 "    color: #333; /* Text color */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style hovered calculator buttons */\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #FAAE3C; /* Slightly darker gray background on hover */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style clicked calculator buttons */\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #FAAE3C; /* Even darker gray background on click */\n"
                                 "}")
        self.btn_9.setObjectName("btn_9")
        self.btn_subtract = QtWidgets.QPushButton(form)
        self.btn_subtract.setGeometry(QtCore.QRect(210, 270, 91, 75))
        self.btn_subtract.setStyleSheet("/* Style calculator buttons */\n"
                                        "QPushButton {\n"
                                        "    background-color: #3CB7F0; /* Light gray background color */\n"
                                        "    border: 1px solid #3CB7F0; /* Light gray border */\n"
                                        "    border-radius: 5px; /* Rounded corners */\n"
                                        "    font: bold 16px; /* Bold 16px font */\n"
                                        "    padding: 10px 20px; /* Padding around the text */\n"
                                        "    margin: 5px; /* Margin between buttons */\n"
                                        "\n"
                                        "    color: #333; /* Text color */\n"
                                        "}\n"
                                        "\n"
                                        "/* Style hovered calculator buttons */\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #3CB7F0; /* Slightly darker gray background on hover */\n"
                                        "}\n"
                                        "\n"
                                        "/* Style clicked calculator buttons */\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #3CB7F0; /* Even darker gray background on click */\n"
                                        "}")
        self.btn_subtract.setObjectName("btn_subtract")
        self.btn_0 = QtWidgets.QPushButton(form)
        self.btn_0.setGeometry(QtCore.QRect(0, 345, 75, 75))
        self.btn_0.setStyleSheet("/* Style calculator buttons */\n"
                                 "QPushButton {\n"
                                 "    background-color: #FAAE3C; /* Light gray background color */\n"
                                 "    border: 1px solid #FAAE3C; /* Light gray border */\n"
                                 "    border-radius: 5px; /* Rounded corners */\n"
                                 "    font: bold 16px; /* Bold 16px font */\n"
                                 "    padding: 10px 20px; /* Padding around the text */\n"
                                 "    margin: 5px; /* Margin between buttons */\n"
                                 "\n"
                                 "    color: #333; /* Text color */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style hovered calculator buttons */\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #FAAE3C; /* Slightly darker gray background on hover */\n"
                                 "}\n"
                                 "\n"
                                 "/* Style clicked calculator buttons */\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #FAAE3C; /* Even darker gray background on click */\n"
                                 "}")
        self.btn_0.setObjectName("btn_0")
        self.btn_decimal = QtWidgets.QPushButton(form)
        self.btn_decimal.setGeometry(QtCore.QRect(70, 345, 75, 75))
        self.btn_decimal.setStyleSheet("/* Style calculator buttons */\n"
                                       "QPushButton {\n"
                                       "    background-color: #FAAE3C; /* Light gray background color */\n"
                                       "    border: 1px solid #FAAE3C; /* Light gray border */\n"
                                       "    border-radius: 5px; /* Rounded corners */\n"
                                       "    font: bold 16px; /* Bold 16px font */\n"
                                       "    padding: 10px 20px; /* Padding around the text */\n"
                                       "    margin: 5px; /* Margin between buttons */\n"
                                       "\n"
                                       "    color: #333; /* Text color */\n"
                                       "}\n"
                                       "\n"
                                       "/* Style hovered calculator buttons */\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: #FAAE3C; /* Slightly darker gray background on hover */\n"
                                       "}\n"
                                       "\n"
                                       "/* Style clicked calculator buttons */\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: #FAAE3C; /* Even darker gray background on click */\n"
                                       "}")
        self.btn_decimal.setObjectName("btn_decimal")
        self.btn_add = QtWidgets.QPushButton(form)
        self.btn_add.setGeometry(QtCore.QRect(140, 345, 75, 75))
        self.btn_add.setStyleSheet("/* Style calculator buttons */\n"
                                   "QPushButton {\n"
                                   "    background-color: #3CB7F0; /* Light gray background color */\n"
                                   "    border: 1px solid #3CB7F0; /* Light gray border */\n"
                                   "    border-radius: 5px; /* Rounded corners */\n"
                                   "    font: bold 16px; /* Bold 16px font */\n"
                                   "    padding: 10px 20px; /* Padding around the text */\n"
                                   "    margin: 5px; /* Margin between buttons */\n"
                                   "\n"
                                   "    color: #333; /* Text color */\n"
                                   "}\n"
                                   "\n"
                                   "/* Style hovered calculator buttons */\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: #3CB7F0; /* Slightly darker gray background on hover */\n"
                                   "}\n"
                                   "\n"
                                   "/* Style clicked calculator buttons */\n"
                                   "QPushButton:pressed {\n"
                                   "    background-color: #3CB7F0; /* Even darker gray background on click */\n"
                                   "}")
        self.btn_add.setObjectName("btn_add")
        self.btn_clear = QtWidgets.QPushButton(form)
        self.btn_clear.setGeometry(QtCore.QRect(210, 345, 91, 75))
        self.btn_clear.setStyleSheet("/* Style calculator buttons */\n"
                                     "QPushButton {\n"
                                     "    background-color: #3CB7F0; /* Light gray background color */\n"
                                     "    border: 1px solid #3CB7F0; /* Light gray border */\n"
                                     "    border-radius: 5px; /* Rounded corners */\n"
                                     "    font: bold 16px; /* Bold 16px font */\n"
                                     "    padding: 10px 20px; /* Padding around the text */\n"
                                     "    margin: 5px; /* Margin between buttons */\n"
                                     "\n"
                                     "    color: #333; /* Text color */\n"
                                     "}\n"
                                     "\n"
                                     "/* Style hovered calculator buttons */\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: #3CB7F0; /* Slightly darker gray background on hover */\n"
                                     "}\n"
                                     "\n"
                                     "/* Style clicked calculator buttons */\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: #3CB7F0; /* Even darker gray background on click */\n"
                                     "}")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_equals = QtWidgets.QPushButton(form)
        self.btn_equals.setGeometry(QtCore.QRect(0, 420, 300, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_equals.setFont(font)
        self.btn_equals.setStyleSheet("/* Style calculator equals button */\n"
                                      "QPushButton {\n"
                                      "    background-color: #4CAF50; /* Green background color */\n"
                                      "    border: 1px solid #4CAF50; /* Green border */\n"
                                      "    border-radius: 5px; /* Rounded corners */\n"
                                      "    font: bold 24px; /* Bold 24px font */\n"
                                      "    padding: 10px 20px; /* Padding around the text */\n"
                                      "    margin: 5px; /* Margin between buttons */\n"
                                      "\n"
                                      "    color: white; /* Text color */\n"
                                      "}\n"
                                      "\n"
                                      "/* Style hovered calculator equals button */\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #45A049; /* Slightly darker green background on hover */\n"
                                      "}\n"
                                      "\n"
                                      "/* Style clicked calculator equals button */\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: #4CAF50; /* Even darker green background on click */\n"
                                      "}")
        self.btn_equals.setObjectName("btn_equals")
        self.btn_add.clicked.connect(self.on_add_clicked)
        self.btn_subtract.clicked.connect(self.on_subtract_clicked)
        self.btn_multiply.clicked.connect(self.on_multiply_clicked)
        self.btn_divide.clicked.connect(self.on_divide_clicked)
        self.btn_clear.clicked.connect(self.on_clear_clicked)
        self.btn_equals.clicked.connect(self.on_equals_clicked)
        self.btn_0.clicked.connect(lambda: self.on_number_clicked("0"))
        self.btn_1.clicked.connect(lambda: self.on_number_clicked("1"))
        self.btn_2.clicked.connect(lambda: self.on_number_clicked("2"))
        self.btn_3.clicked.connect(lambda: self.on_number_clicked("3"))
        self.btn_4.clicked.connect(lambda: self.on_number_clicked("4"))
        self.btn_5.clicked.connect(lambda: self.on_number_clicked("5"))
        self.btn_6.clicked.connect(lambda: self.on_number_clicked("6"))
        self.btn_7.clicked.connect(lambda: self.on_number_clicked("7"))
        self.btn_8.clicked.connect(lambda: self.on_number_clicked("8"))
        self.btn_9.clicked.connect(lambda: self.on_number_clicked("9"))
        self.btn_decimal.clicked.connect(lambda: self.on_number_clicked("."))

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "Calculator"))
        self.display.setText(_translate("form", "0"))
        self.btn_1.setText(_translate("form", "1"))
        self.btn_2.setText(_translate("form", "2"))
        self.btn_3.setText(_translate("form", "3"))
        self.btn_divide.setText(_translate("form", "/"))
        self.btn_4.setText(_translate("form", "4"))
        self.btn_5.setText(_translate("form", "5"))
        self.btn_6.setText(_translate("form", "6"))
        self.btn_multiply.setText(_translate("form", "x"))
        self.btn_7.setText(_translate("form", "7"))
        self.btn_8.setText(_translate("form", "8"))
        self.btn_9.setText(_translate("form", "9"))
        self.btn_subtract.setText(_translate("form", "-"))
        self.btn_0.setText(_translate("form", "0"))
        self.btn_decimal.setText(_translate("form", "."))
        self.btn_add.setText(_translate("form", "+"))
        self.btn_clear.setText(_translate("form", "C"))
        self.btn_equals.setText(_translate("form", "="))

    def on_number_clicked(self, digit):
        # Handle the digit button clicks (0-9, decimal point)
        current_text = self.display.text()
        # Ignore leading zeros (e.g., "03" becomes "3")
        if current_text == "0":
            self.display.setText(digit)
        else:
            self.display.setText(current_text + digit)

    def on_add_clicked(self):
        # Handle the addition operator button click
        current_text = self.display.text()
        if current_text != "0":
            self.display.setText(current_text + " + ")

    def on_subtract_clicked(self):
        # Handle the subtraction operator button click
        current_text = self.display.text()
        if current_text != "0":
            self.display.setText(current_text + " - ")

    def on_multiply_clicked(self):
        # Handle the multiplication operator button click
        current_text = self.display.text()
        if current_text != "0":
            self.display.setText(current_text + " x ")

    def on_divide_clicked(self):
        # Handle the division operator button click
        current_text = self.display.text()
        if current_text != "0":
            self.display.setText(current_text + " / ")

    def on_clear_clicked(self):
        # Handle the clear button click
        self.display.setText("0")

    def on_equals_clicked(self):
    # Handle the equals button click
       current_text = self.display.text()
    # Replace 'x' with '*' for multiplication
       current_text = current_text.replace('x', '*')
       try:
        result = eval(current_text)
        self.display.setText(str(result))
       except Exception as e:
        self.display.setText("Error")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = Ui_form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())
