# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\auth.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_authorization(object):
    def setupUi(self, authorization):
        authorization.setObjectName("authorization")
        authorization.resize(529, 553)
        authorization.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(authorization)
        self.centralwidget.setStyleSheet("QWidget{\n"
                                         "background-color: white\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(180, 190, 181, 31))
        self.login.setStyleSheet("QLineEdit{\n"
                                 "border: 1px solid rgb(188, 188, 186);\n"
                                 "border-radius: 10px;\n"
                                 "}")
        self.login.setText("")
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(180, 260, 181, 31))
        self.password.setStyleSheet("QLineEdit{\n"
                                    "border: 1px solid rgb(188, 188, 186);\n"
                                    "border-radius: 10px;\n"
                                    "}")
        self.password.setObjectName("password")
        self.sign_in = QtWidgets.QPushButton(self.centralwidget)
        self.sign_in.setGeometry(QtCore.QRect(180, 310, 81, 31))
        self.sign_in.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        self.sign_in.setFont(font)
        self.sign_in.setStyleSheet("QPushButton{\n"
                                   "border: 1px solid rgb(188, 188, 186);\n"
                                   "border-radius: 10px;\n"
                                   "background-color: rgb(219, 255, 246)\n"
                                   "}")
        self.sign_in.setCheckable(False)
        self.sign_in.setAutoRepeatDelay(300)
        self.sign_in.setObjectName("sign_in")
        self.admin = QtWidgets.QPushButton(self.centralwidget)
        self.admin.setGeometry(QtCore.QRect(200, 370, 138, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.admin.setFont(font)
        self.admin.setStyleSheet("QPushButton{\n"
                                 "border: 1px solid rgb(188, 188, 186);\n"
                                 "border-radius: 10px;\n"
                                 "background-color: rgb(255, 170, 127)\n"
                                 "}")
        self.admin.setObjectName("admin")
        self.sign_up = QtWidgets.QPushButton(self.centralwidget)
        self.sign_up.setGeometry(QtCore.QRect(280, 310, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        self.sign_up.setFont(font)
        self.sign_up.setStyleSheet("QPushButton{\n"
                                   "border: 1px solid rgb(188, 188, 186);\n"
                                   "border-radius: 10px;\n"
                                   "background-color: rgb(219, 255, 246)\n"
                                   "}\n"
                                   "")
        self.sign_up.setObjectName("sign_up")
        self.password.raise_()
        self.sign_in.raise_()
        self.login.raise_()
        self.admin.raise_()
        self.sign_up.raise_()
        authorization.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(authorization)
        self.statusbar.setObjectName("statusbar")
        authorization.setStatusBar(self.statusbar)

        self.retranslateUi(authorization)
        QtCore.QMetaObject.connectSlotsByName(authorization)

    def retranslateUi(self, authorization):
        _translate = QtCore.QCoreApplication.translate
        authorization.setWindowTitle(_translate("authorization", "Authorization"))
        self.login.setPlaceholderText(_translate("authorization", "Login.."))
        self.password.setPlaceholderText(_translate("authorization", "Password.."))
        self.sign_in.setText(_translate("authorization", "Sign in"))
        self.admin.setText(_translate("authorization", "Administration"))
        self.sign_up.setText(_translate("authorization", "Sign up"))
