# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QButtonGroup, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextBrowser, QTextEdit, QWidget)
from Utils.business_logic import fCkriptograf, logicButton, DatabaseManager
import re
class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.BUTTON_STYLE_NORMAL = "QPushButton { background-color: white; }"
        self.BUTTON_STYLE_PRESSED = "QPushButton { background-color: lightblue; }"
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1600, 900)
        MainWindow.setToolTip(u"")
        MainWindow.setStatusTip(u"")
        MainWindow.setWhatsThis(u"")
        self.actionButton_1 = QAction(MainWindow)
        self.actionButton_1.setObjectName(u"actionButton_1")
        self.actionButton_1.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setToolTip(u"")
        self.centralwidget.setStatusTip(u"")
        self.centralwidget.setWhatsThis(u"")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 0, 1631, 901))
        self.tabWidget.setToolTip(u"")
        self.tabWidget.setStatusTip(u"")
        self.tabWidget.setWhatsThis(u"")
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)

        # tab1
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.tab1.setInputMethodHints(Qt.ImhNone)

        self.ButtonT_1chesary = QPushButton(self.tab1)
        self.ButtonT_1chesary.setObjectName(u"ButtonT_1chesary")
        self.ButtonT_1chesary.setGeometry(QRect(0, 40, 121, 31))
        self.ButtonT_1chesary.clicked.connect(self.run_chesary_cipher)

        self.ButtonT_2Sloganistic = QPushButton(self.tab1)
        self.ButtonT_2Sloganistic.setObjectName(u"ButtonT_2Sloganistic")
        self.ButtonT_2Sloganistic.setGeometry(QRect(0, 70, 121, 31))
        self.ButtonT_2Sloganistic.clicked.connect(self.run_sloganistic_cipher)

        self.ButtonT_3TablPris = QPushButton(self.tab1)
        self.ButtonT_3TablPris.setObjectName(u"ButtonT_3TablPris")
        self.ButtonT_3TablPris.setGeometry(QRect(0, 100, 121, 31))
        self.ButtonT_3TablPris.clicked.connect(self.run_tablpris_cipher)

        self.ButtonT_4Ramzai = QPushButton(self.tab1)
        self.ButtonT_4Ramzai.setObjectName(u"ButtonT_4Ramzai")
        self.ButtonT_4Ramzai.setGeometry(QRect(0, 130, 121, 31))
        self.ButtonT_4Ramzai.clicked.connect(self.run_ramzai_cipher)

        self.TextTOnButton = QTextBrowser(self.tab1)
        self.TextTOnButton.setObjectName(u"TextTOnButton")
        self.TextTOnButton.setGeometry(QRect(0, 0, 120, 41))

        self.TextTOutput = QTextEdit(self.tab1)
        self.TextTOutput.setObjectName(u"TextTOutput")
        self.TextTOutput.setGeometry(QRect(121, 0, 1471, 851))

        self.TextTOutput.setReadOnly(True)
        self.tabWidget.addTab(self.tab1, "")

        # # tab 2
        # self.tab2 = QWidget()
        # self.tab2.setObjectName(u"tab2")
        #
        # self.TextPOutput = QTextEdit(self.tab2)
        # self.TextPOutput.setObjectName(u"TextPOutput")
        # self.TextPOutput.setGeometry(QRect(121, 0, 1471, 721))
        #
        # self.TextPOutput.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        # self.TextPOnButton = QTextBrowser(self.tab2)
        # self.TextPOnButton.setObjectName(u"TextPOnButton")
        # self.TextPOnButton.setGeometry(QRect(0, 0, 120, 41))
        #
        # self.ButtonP_1chesary = QPushButton(self.tab2)
        # self.ButtonP_1chesary.setObjectName(u"ButtonP_1chesary")
        # self.ButtonP_1chesary.setGeometry(QRect(0, 40, 121, 31))
        #
        # self.ButtonP_2Sloganistic = QPushButton(self.tab2)
        # self.ButtonP_2Sloganistic.setObjectName(u"ButtonP_2Sloganistic")
        # self.ButtonP_2Sloganistic.setGeometry(QRect(0, 70, 121, 31))
        #
        # self.ButtonP_3TablPris = QPushButton(self.tab2)
        # self.ButtonP_3TablPris.setObjectName(u"ButtonP_3TablPris")
        # self.ButtonP_3TablPris.setGeometry(QRect(0, 100, 121, 31))
        #
        # self.ButtonP_4Ramzai = QPushButton(self.tab2)
        # self.ButtonP_4Ramzai.setObjectName(u"ButtonP_4Ramzai")
        # self.ButtonP_4Ramzai.setGeometry(QRect(0, 130, 121, 31))
        #
        # self.textEdit = QTextEdit(self.tab2)
        # self.textEdit.setObjectName(u"textEdit")
        # self.textEdit.setGeometry(QRect(241, 722, 1351, 41))
        # self.textEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        #
        # self.pushButton = QPushButton(self.tab2)
        # self.pushButton.setObjectName(u"pushButton")
        # self.pushButton.setGeometry(QRect(1472, 763, 121, 31))
        # self.tabWidget.addTab(self.tab2, "")

        # tab3
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        self.tab3.setFont(font)
        self.tab3.setToolTip(u"")
        self.tab3.setStatusTip(u"")
        self.tab3.setWhatsThis(u"")

        self.TextCDOnButton = QTextBrowser(self.tab3)
        self.TextCDOnButton.setObjectName(u"TextCDOnButton")
        self.TextCDOnButton.setEnabled(True)
        self.TextCDOnButton.setGeometry(QRect(0, 0, 120, 40))
        self.TextCDOnButton.setToolTip(u"")
        self.TextCDOnButton.setStatusTip(u"")
        self.TextCDOnButton.setWhatsThis(u"")

        self.ButtonCD_3TablPris = QPushButton(self.tab3)
        self.ButtonCD_3TablPris.setObjectName(u"ButtonCD_3TablPris")
        self.ButtonCD_3TablPris.setEnabled(True)
        self.ButtonCD_3TablPris.setGeometry(QRect(0, 100, 121, 31))
        self.ButtonCD_3TablPris.setToolTip(u"")
        self.ButtonCD_3TablPris.setStatusTip(u"")
        self.ButtonCD_3TablPris.setWhatsThis(u"")
        self.ButtonCD_3TablPris.clicked.connect(self.on_ButtonCD_TablPris_clicked)

        self.ButtonCD_2Sloganistic = QPushButton(self.tab3)
        self.ButtonCD_2Sloganistic.setObjectName(u"ButtonCD_2Sloganistic")
        self.ButtonCD_2Sloganistic.setEnabled(True)
        self.ButtonCD_2Sloganistic.setGeometry(QRect(0, 70, 121, 31))
        self.ButtonCD_2Sloganistic.setToolTip(u"")
        self.ButtonCD_2Sloganistic.setStatusTip(u"")
        self.ButtonCD_2Sloganistic.setWhatsThis(u"")
        self.ButtonCD_2Sloganistic.clicked.connect(self.on_ButtonCD_Slogan_clicked)

        self.ButtonCD_4Ramzai = QPushButton(self.tab3)
        self.ButtonCD_4Ramzai.setObjectName(u"ButtonCD_4Ramzai")
        self.ButtonCD_4Ramzai.setEnabled(True)
        self.ButtonCD_4Ramzai.setGeometry(QRect(0, 130, 121, 31))
        self.ButtonCD_4Ramzai.setToolTip(u"")
        self.ButtonCD_4Ramzai.setStatusTip(u"")
        self.ButtonCD_4Ramzai.setWhatsThis(u"")
        self.ButtonCD_4Ramzai.clicked.connect(self.on_ButtonCD_Ramsai_clicked)

        self.ButtonCD_1chesary = QPushButton(self.tab3)
        self.ButtonCD_1chesary.setObjectName(u"ButtonCD_1chesary")
        self.ButtonCD_1chesary.setEnabled(True)
        self.ButtonCD_1chesary.setGeometry(QRect(0, 40, 121, 31))
        self.ButtonCD_1chesary.setToolTip(u"")
        self.ButtonCD_1chesary.setStatusTip(u"")
        self.ButtonCD_1chesary.setWhatsThis(u"")
        self.ButtonCD_1chesary.clicked.connect(self.on_ButtonCD_Chesary_clicked)

        self.TextCD_Cod = QTextEdit(self.tab3)
        self.TextCD_Cod.setObjectName(u"TextCD_Cod")
        self.TextCD_Cod.setEnabled(True)
        self.TextCD_Cod.setGeometry(QRect(124, 40, 735, 101))
        self.TextCD_Cod.setAcceptDrops(False)

        self.TextCD_Cod.setToolTip(u"")
        self.TextCD_Cod.setStatusTip(u"")
        self.TextCD_Cod.setWhatsThis(u"")

        self.ButtonCD_Codir = QPushButton(self.tab3)
        self.ButtonCD_Codir.setObjectName(u"ButtonCD_Codir")
        self.ButtonCD_Codir.setEnabled(True)
        self.ButtonCD_Codir.setGeometry(QRect(760, 140, 101, 47))
        self.ButtonCD_Codir.setToolTip(u"")
        self.ButtonCD_Codir.setStatusTip(u"")
        self.ButtonCD_Codir.setWhatsThis(u"")

        self.TextCDCod = QTextBrowser(self.tab3)
        self.TextCDCod.setObjectName(u"TextCDCod")
        self.TextCDCod.setEnabled(True)
        self.TextCDCod.setGeometry(QRect(124, -1, 735, 41))
        self.TextCDCod.setToolTip(u"")
        self.TextCDCod.setStatusTip(u"")
        self.TextCDCod.setWhatsThis(u"")

        self.TextCDDecod = QTextBrowser(self.tab3)
        self.TextCDDecod.setObjectName(u"TextCDDecod")
        self.TextCDDecod.setEnabled(True)
        self.TextCDDecod.setGeometry(QRect(860, 0, 731, 41))
        self.TextCDDecod.setToolTip(u"")
        self.TextCDDecod.setStatusTip(u"")
        self.TextCDDecod.setWhatsThis(u"")

        self.TextCD_Decod = QTextEdit(self.tab3)
        self.TextCD_Decod.setObjectName(u"TextCD_Decod")
        self.TextCD_Decod.setEnabled(True)
        self.TextCD_Decod.setGeometry(QRect(860, 40, 731, 101))
        self.TextCD_Decod.setAcceptDrops(False)
        self.TextCD_Decod.setToolTip(u"")
        self.TextCD_Decod.setStatusTip(u"")
        self.TextCD_Decod.setWhatsThis(u"")

        self.ButtonCD_Decodir = QPushButton(self.tab3)
        self.ButtonCD_Decodir.setObjectName(u"ButtonCD_Decodir")
        self.ButtonCD_Decodir.setEnabled(True)
        self.ButtonCD_Decodir.setGeometry(QRect(1490, 140, 101, 47))
        self.ButtonCD_Decodir.setToolTip(u"")
        self.ButtonCD_Decodir.setStatusTip(u"")
        self.ButtonCD_Decodir.setWhatsThis(u"")

        self.textCod1 = QTextBrowser(self.tab3)
        self.textCod1.setObjectName(u"textCod1")
        self.textCod1.setGeometry(QRect(124, 142, 100, 44))

        self.TextCD_KeyC = QTextEdit(self.tab3)
        self.TextCD_KeyC.setObjectName(u"TextCD_KeyC")
        self.TextCD_KeyC.setGeometry(QRect(225, 142, 537, 44))

        self.TextCD_KeyD = QTextEdit(self.tab3)
        self.TextCD_KeyD.setObjectName(u"TextCD_KeyD")
        self.TextCD_KeyD.setGeometry(QRect(961, 142, 531, 44))

        self.textCod2 = QTextBrowser(self.tab3)
        self.textCod2.setObjectName(u"textCod2")
        self.textCod2.setGeometry(QRect(860, 142, 100, 44))

        self.TextStep = QTextBrowser(self.tab3)
        self.TextStep.setObjectName(u"TextStep")
        self.TextStep.setGeometry(QRect(124, 228, 1465, 621))

        self.textSteps = QTextBrowser(self.tab3)
        self.textSteps.setObjectName(u"textSteps")
        self.textSteps.setGeometry(QRect(124, 187, 1465, 41))

        icon = QIcon(QIcon.fromTheme(u"accessories-calculator"))
        self.tabWidget.addTab(self.tab3, icon, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setToolTip(u"")
        self.statusbar.setStatusTip(u"")
        self.statusbar.setWhatsThis(u"")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.ButtonT_1chesary.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

        self.current_codir_handler = None
        self.current_decodir_handler = None

    def only_digits(self, input_str):
        return input_str.isdigit()

    def check_eng(self, stext):
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?;:'-()[]{} ")
        for c in stext:
            if c not in allowed_chars:
                return False
        return True

    def letters_and_digits(self, input_str):
        return input_str.isalnum()

    def on_ButtonCD_Chesary_clicked(self):
        BUTTON_STYLE_NORMAL = "QPushButton { background-color: white; }"
        BUTTON_STYLE_PRESSED = "QPushButton { background-color: lightblue; }"

        self.disconnect_signals()
        self.ButtonCD_Codir.clicked.connect(self.Ches_Encript)
        self.ButtonCD_Decodir.clicked.connect(self.Ches_Decript)
        self.current_codir_handler = self.Ches_Encript
        self.current_decodir_handler = self.Ches_Decript

        self.ButtonCD_1chesary.setStyleSheet(BUTTON_STYLE_PRESSED)
        self.ButtonCD_2Sloganistic.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonCD_3TablPris.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonCD_4Ramzai.setStyleSheet(BUTTON_STYLE_NORMAL)

    def on_ButtonCD_Slogan_clicked(self):
        self.disconnect_signals()
        self.ButtonCD_Codir.clicked.connect(self.Slogan_Encript)
        self.ButtonCD_Decodir.clicked.connect(self.Slogan_Decript)
        self.current_codir_handler = self.Slogan_Encript
        self.current_decodir_handler = self.Slogan_Decript

        BUTTON_STYLE_NORMAL = "QPushButton { background-color: white; }"
        BUTTON_STYLE_PRESSED = "QPushButton { background-color: lightblue; }"

        self.ButtonCD_1chesary.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonCD_2Sloganistic.setStyleSheet(BUTTON_STYLE_PRESSED)
        self.ButtonCD_3TablPris.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonCD_4Ramzai.setStyleSheet(BUTTON_STYLE_NORMAL)

    def on_ButtonCD_TablPris_clicked(self):
        self.disconnect_signals()
        self.ButtonCD_Codir.clicked.connect(self.TablPrisemys_Encript)
        self.ButtonCD_Decodir.clicked.connect(self.TablPrisemys_Decript)
        self.current_codir_handler = self.TablPrisemys_Encript
        self.current_decodir_handler = self.TablPrisemys_Decript

        BUTTON_STYLE_NORMAL = "QPushButton { background-color: white; }"
        BUTTON_STYLE_PRESSED = "QPushButton { background-color: lightblue; }"

        self.ButtonCD_1chesary.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonCD_2Sloganistic.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonCD_3TablPris.setStyleSheet(BUTTON_STYLE_PRESSED)
        self.ButtonCD_4Ramzai.setStyleSheet(BUTTON_STYLE_NORMAL)

    def on_ButtonCD_Ramsai_clicked(self):
        self.disconnect_signals()
        self.ButtonCD_Codir.clicked.connect(self.Ramsai_Encript)
        self.ButtonCD_Decodir.clicked.connect(self.Ramsai_Decript)
        self.current_codir_handler = self.Ramsai_Encript
        self.current_decodir_handler = self.Ramsai_Decript

        BUTTON_STYLE_NORMAL = "QPushButton { background-color: white; }"
        BUTTON_STYLE_PRESSED = "QPushButton { background-color: lightblue; }"

        self.ButtonCD_1chesary.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonCD_2Sloganistic.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonCD_3TablPris.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonCD_4Ramzai.setStyleSheet(BUTTON_STYLE_PRESSED)

    def disconnect_signals(self):
        if self.current_codir_handler:
            try:
                self.ButtonCD_Codir.clicked.disconnect(self.current_codir_handler)
            except TypeError:
                pass
        if self.current_decodir_handler:
            try:
                self.ButtonCD_Decodir.clicked.disconnect(self.current_decodir_handler)
            except TypeError:
                pass

        self.current_codir_handler = None
        self.current_decodir_handler = None

    def Ches_Encript(self):
        text = self.TextCD_Cod.toPlainText()
        key = self.TextCD_KeyC.toPlainText()

        if not self.only_digits(key):
            self.TextStep.setPlainText("Вы ввели буквы в строку ключ")
            return
        if int(key) > 26:
            self.TextStep.setPlainText("Вы ввели значение больше 26 в строку ключ")
            return
        if not self.check_eng(text):
            self.TextStep.setPlainText("Текст должен содержать только английские буквы.")
            return
        if len(text) > 10000:
            self.TextStep.setPlainText("Текст должен быть менее 10000 символов .")
            return
        if len(self.key) > 100:
            self.TextStep.setPlainText("Ключ должен быть менее 100 символов.")
            return

        self.answer, self.steps = fCkriptograf.Chesary.encrypt(text, key)

        self.TextCD_Decod.setText(self.answer)
        self.display_steps(self.steps)

    def Ches_Decript(self):
        self.text = self.TextCD_Decod.toPlainText()
        self.key = self.TextCD_KeyD.toPlainText()

        if not self.only_digits(self.key):
            self.TextStep.setPlainText("Вы ввели буквы в строку ключ")
            return
        if int(self.key) > 26:
            self.TextStep.setPlainText("Вы ввели значение больше 26  в строку ключ")
            return
        if not self.check_eng(self.text):
            self.TextStep.setPlainText("Текст должен содержать только английские буквы.")
            return
        if len(self.text) > 100000:
            self.TextStep.setPlainText("Текст должен быть менее 10000 символов .")
            return
        if len(self.key) > 100:
            self.TextStep.setPlainText("Ключ должен быть менее 100 символов.")
            return

        self.answer, self.steps = fCkriptograf.Chesary.decrypt(self.text, self.key)

        self.TextCD_Cod.setText(self.answer)
        self.display_steps(self.steps)

    def Slogan_Encript(self):
        self.text = self.TextCD_Cod.toPlainText()
        self.key = self.TextCD_KeyC.toPlainText()

        if not self.check_eng(self.key):
            self.TextStep.setPlainText("Ключ должен содержать только английские буквы.")
            return
        if not self.check_eng(self.text):
            self.TextStep.setPlainText("Текст должен содержать только английские буквы.")
            return
        if len(self.text) > 10000:
            self.TextStep.setPlainText("Текст должен быть менее 10000 символов .")
            return
        if len(self.key) > 100:
            self.TextStep.setPlainText("Ключ должен быть менее 100 символов.")
            return

        self.answer, self.steps, self.orig_alph, self.shif_alph = fCkriptograf.SloganCipher(self.key).encrypt(self.text)

        self.TextCD_Decod.setText(self.answer)
        self.display_steps(self.steps, self.orig_alph, self.shif_alph)

    def Slogan_Decript(self):
        self.text = self.TextCD_Decod.toPlainText()
        self.key = self.TextCD_KeyD.toPlainText()

        if not self.check_eng(self.key):
            self.TextStep.setPlainText("Ключ должен содержать только английские буквы.")
            return
        if not self.check_eng(self.text):
            self.TextStep.setPlainText("Текст должен содержать только английские буквы.")
            return
        if len(self.text) > 10000:
            self.TextStep.setPlainText("Текст должен быть менее 10000 символов .")
            return
        if len(self.key) > 100:
            self.TextStep.setPlainText("Ключ должен быть менее 100 символов.")
            return

        self.answer, self.steps, self.orig_alph, self.shif_alph = fCkriptograf.SloganCipher(self.key).decrypt(self.text)

        self.TextCD_Cod.setText(self.answer)
        self.display_steps(self.steps, self.orig_alph, self.shif_alph)

    def TablPrisemys_Encript(self):
        self.text = self.TextCD_Cod.toPlainText().lower()
        self.key = self.TextCD_KeyC.toPlainText().lower()

        if not self.check_eng(self.key):
            self.TextStep.setPlainText("Ключ должен содержать только английские буквы.")
            return
        if not self.check_eng(self.text):
            self.TextStep.setPlainText("Текст должен содержать только английские буквы.")
            return
        if len(self.text) > 10000:
            self.TextStep.setPlainText("Текст должен быть менее 10000 символов .")
            return
        if len(self.key) > 100:
            self.TextStep.setPlainText("Ключ должен быть менее 100 символов.")
            return

        self.answer, self.steps, self.primesus_table = fCkriptograf.TrisemusCipher(self.key).encrypt(self.text)

        self.TextCD_Decod.setText(self.answer)
        self.display_steps(self.steps)
        self.display_table(self.primesus_table)

    def TablPrisemys_Decript(self):
        self.text = self.TextCD_Decod.toPlainText().lower()
        self.key = self.TextCD_KeyD.toPlainText().lower()

        if not self.check_eng(self.key):
            self.TextStep.setPlainText("Kлюч должен содержать только английские буквы.")
            return
        if not self.check_eng(self.text):
            self.TextStep.setPlainText("Текст должен содержать только английские буквы.")
            return
        if len(self.text) > 10000:
            self.TextStep.setPlainText("Текст должен быть менее 10000 символов.")
            return
        if len(self.key) > 100:
            self.TextStep.setPlainText("Ключ должен быть менее 100 символов.")
            return

        self.answer, self.steps, self.primesus_table = fCkriptograf.TrisemusCipher(self.key).decrypt(self.text)

        self.TextCD_Cod.setText(self.answer)
        self.display_steps(self.steps)
        self.display_table(self.primesus_table)

    def Ramsai_Encript(self):
        self.text = self.TextCD_Cod.toPlainText()
        self.key = self.TextCD_KeyC.toPlainText()

        if not self.check_eng(self.key):
            self.TextStep.setPlainText("Kлюч должен содержать только английские буквы.")
            return
        if not self.check_eng(self.text):
            self.TextStep.setPlainText("Текст должен содержать только английские буквы.")
            return
        if len(self.text) > 10000:
            self.TextStep.setPlainText("Текст должен быть менее 10000 символов .")
            return
        if len(self.key) > 100:
            self.TextStep.setPlainText("Ключ должен быть менее 100 символов.")
            return

        self.answer, self.steps, abc = fCkriptograf.KeywordSubstitutionCipher(self.key.upper()).encrypt(self.text)

        self.TextCD_Decod.setText(self.answer)
        self.display_steps(self.steps)
        self.display_table_in_one_line(abc)

    def Ramsai_Decript(self):
        self.text = self.TextCD_Decod.toPlainText()
        self.key = self.TextCD_KeyD.toPlainText()

        if not self.check_eng(self.key):
            self.TextStep.setPlainText("Kлюч должен содержать только английские буквы.")
            return
        if not self.check_eng(self.text):
            self.TextStep.setPlainText("Текст должен содержать только английские буквы.")
            return
        if len(self.text) > 10000:
            self.TextStep.setPlainText("Текст должен быть менее 10000 символов .")
            return
        if len(self.key) > 100:
            self.TextStep.setPlainText("Ключ должен быть менее 100 символов.")
            return

        self.answer, self.steps, abc = fCkriptograf.KeywordSubstitutionCipher(self.key.upper()).decrypt(self.text)

        self.TextCD_Cod.setText(self.answer)
        self.display_steps(self.steps)
        self.display_table_in_one_line(abc)

    # Convert list to formatted string
    def display_steps(self, steps_list, orig_alph=None, shif_alph=None):
        if orig_alph and shif_alph:
            alphabets_display = "Оригинальный алфавит: " + " ".join(orig_alph) + "\n" + "Изменённый алфавит: " + " ".join(shif_alph)
        else:
            alphabets_display = ""

        print(steps_list)
        self.formatted_steps = "\n".join(f"{index + 1} шаг - {step}" for index, step in enumerate(steps_list))

        if alphabets_display:
            self.formatted_steps = alphabets_display + "\n\n" + self.formatted_steps

        self.TextStep.setPlainText(self.formatted_steps)

    def display_table(self, table):
        formatted_table = "\n".join([" ".join(row) for row in table])
        self.TextStep.insertPlainText("\nТаблица Присемуса:\n" + formatted_table + "\n")

    def display_table_in_one_line(self, table):
        formatted_table = "|".join([" ".join(row) for row in table])
        self.TextStep.insertPlainText("\n Измененный алфавит Рамзай: " + formatted_table + "\n")
    def run_chesary_cipher(self):
        BUTTON_STYLE_NORMAL = "QPushButton { background-color: white; }"
        BUTTON_STYLE_PRESSED = "QPushButton { background-color: lightblue; }"

        self.ButtonT_1chesary.setStyleSheet(BUTTON_STYLE_PRESSED)
        self.ButtonT_2Sloganistic.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonT_3TablPris.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonT_4Ramzai.setStyleSheet(BUTTON_STYLE_NORMAL)


        self.TextTOutput.setHtml(
            "<h2>Шифр Цезаря</h2>"
            "<p><b>Шифр Цезаря (Caesar Cipher)</b> - один из простейших и наиболее широко известных методов шифрования. Этот шифр получил свое название от древнеримского полководца Юлия Цезаря, который использовал его для секретной переписки.</p>"
            "<p>Шифр Цезаря основан на принципе сдвига букв в алфавите. Каждая буква в открытом тексте заменяется на букву, находящуюся на некотором постоянном числе позиций в алфавите. Это число называется ключом шифра.</p>"
            "<p>Например, если ключ шифра равен 3, то буква A заменяется на D, B на E, C на F и так далее. Последняя буква алфавита заменяется на первую.</p>"
            "<h3>Пример</h3>"
            "<p>Рассмотрим шифрование слова \"HELLO\" с ключом 3:</p>"
            "<ol>"
            "    <li>H -> H + 3 = L</li>"
            "    <li>E -> E + 3 = H</li>"
            "    <li>L -> L + 3 = O</li>"
            "    <li>L -> L + 3 = O</li>"
            "    <li>O -> O + 3 = R</li>"
            "</ol>"
            "<p>Таким образом, слово \"HELLO\" зашифровывается как \"LOKRO\".</p>"
            "<p>Преимущество шифра Цезаря в его простоте и легкости реализации. Однако он является крайне уязвимым к атаке методом анализа частоты букв и легко поддается взлому, особенно при использовании коротких текстов или если известно, что текст зашифрован с использованием шифра Цезаря.</p>"
            "<p>Шифр Цезаря часто используется в образовательных целях для демонстрации основных принципов шифрования, а также в качестве простого упражнения для начинающих в криптографии.</p>"
        )


    def run_sloganistic_cipher(self):
        BUTTON_STYLE_NORMAL = "QPushButton { background-color: white; }"
        BUTTON_STYLE_PRESSED = "QPushButton { background-color: lightblue; }"

        self.ButtonT_1chesary.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonT_2Sloganistic.setStyleSheet(BUTTON_STYLE_PRESSED)
        self.ButtonT_3TablPris.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonT_4Ramzai.setStyleSheet(BUTTON_STYLE_NORMAL)

        self.TextTOutput.setHtml(
            "<h2>Шифр слогана</h2>"
            "<p><b>Шифр слогана (Slogan Cipher)</b> является простым методом шифрования, который использует уникальный набор символов, называемый слоганом, для перестановки букв в алфавите.</p>"
            "<h3>Принцип работы</h3>"
            "<p><u>Инициализация:</u> В начале работы шифра задается слоган, который представляет собой уникальный набор символов, обычно слова или фраза, без пробелов и без учета регистра. Например, 'CIPHER' или 'HELLO'.</p>"
            "<p><u>Формирование зашифрованного алфавита:</u> Для создания зашифрованного алфавита сначала добавляются символы из слогана. Затем оставшиеся символы алфавита добавляются в конец в том же порядке, в котором они следуют в исходном алфавите, исключая символы, уже добавленные из слогана.</p>"
            "<p><u>Шифрование:</u> Каждая буква из открытого текста заменяется соответствующей буквой в зашифрованном алфавите. Замена происходит на основе порядка символов в алфавите и слогане. Если буква не найдена в зашифрованном алфавите (например, цифры, пробелы или знаки препинания), она остается неизменной.</p>"
            "<p><u>Расшифровка:</u> Процесс обратный шифрованию. Каждая буква из зашифрованного текста заменяется соответствующей буквой в исходном алфавите, восстанавливая исходный текст.</p>"
            "<h3>Пример</h3>"
            "<p>Рассмотрим пример шифрования и дешифрования сообщения \"HELLO WORLD\" с использованием слогана \"CIPHER\":</p>"
            "<p><strong>Шифрование:</strong></p>"
            "<ol>"
            "    <li>Зашифрованный алфавит на основе слогана \"CIPHER\": CIPHERABDGJKLMNQSTUVWXYZ</li>"
            "    <li>Заменяем буквы исходного сообщения \"HELLO WORLD\" соответствующими буквами в зашифрованном алфавите: \"RJCCP YPSKX\"</li>"
            "</ol>"
            "<p><strong>Дешифрование:</strong></p>"
            "<ol>"
            "    <li>Восстанавливаем исходный алфавит: ABCDEFGHIJKLMNOPQRSTUVWXYZ</li>"
            "    <li>Заменяем буквы зашифрованного сообщения \"RJCCP YPSKX\" соответствующими буквами в исходном алфавите: \"HELLO WORLD\"</li>"
            "</ol>"
            "<h3>Преимущества и недостатки</h3>"
            "<p><u>Простота:</u> Шифр слогана легко реализовать и понять.</p>"
            "<p><u>Уникальность:</u> Зашифрованный алфавит зависит от выбранного слогана, что делает его уникальным для каждой задачи шифрования.</p>"
            "<p><u>Образовательность:</u> Подходит для обучения основам криптографии.</p>"
            "<p>Но стоит отметить, что шифр слогана не обладает высоким уровнем безопасности, так как подвержен частотному анализу и легко поддается взлому при использовании коротких или предсказуемых слоганов. Он больше подходит для образовательных целей или для создания легких шифрованных сообщений без серьезных требований к безопасности.</p>"
        )

    def run_tablpris_cipher(self):
        BUTTON_STYLE_NORMAL = "QPushButton { background-color: white; }"
        BUTTON_STYLE_PRESSED = "QPushButton { background-color: lightblue; }"

        self.ButtonT_1chesary.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonT_2Sloganistic.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonT_3TablPris.setStyleSheet(BUTTON_STYLE_PRESSED)
        self.ButtonT_4Ramzai.setStyleSheet(BUTTON_STYLE_NORMAL)

        self.TextTOutput.setHtml(
        "<h2>Теория шифрования таблицей Трисемуса</h2>"
        "<h3>Введение</h3>"
        "<p>Шифрование таблицей Трисемуса (или шифр Трисемуса) — это метод полиграфического шифрования, использующий матрицу (таблицу) для замены букв текста. Шифр Трисемуса является примером подстановочного шифра, который обеспечивает большую безопасность по сравнению с простыми шифрами подстановки за счет использования более сложной схемы замены символов.</p>"
        # "<h3>История</h3>"
        # "<p>Шифр был изобретен немецким ученым Йоганном Трисемусом в начале XVI века и является одним из старейших методов полиграфического шифрования. Он использовался для защиты переписки и информации в различных сферах, включая военные и дипломатические сообщения.</p>"
        "<h3>Основные принципы</h3>"
        "<ol>"
        "    <li><strong>Таблица шифрования:</strong> Таблица Трисемуса представляет собой квадратную матрицу размером 5x5 (или 6x6 для расширенных алфавитов), в которую вписываются все буквы алфавита. Например, для английского алфавита из 26 букв используется таблица 5x5, где 'I' и 'J' объединяются в один символ, чтобы вместить все буквы.</li>"
        "    <li><strong>Заполнение таблицы:</strong> Таблица заполняется ключевым словом, за которым следуют остальные буквы алфавита, которые не входят в ключевое слово. Каждая буква используется только один раз."
        "        <br>Пример: ключевое слово \"keyword\""
        "        <pre>"
        "        <br>k e y  w  o"
        "        <br>r d a  b  c"
        "        <br>f g h i/j l"
        "        <br>m n p  q  s"
        "        <br>t u v  x  z"
        "        </pre>"
        "    </li>"
        "    <li><strong>Процесс шифрования:</strong> Шифрование происходит путем замены каждой буквы открытого текста на соответствующую букву из таблицы. Для этого используется следующий метод:"
        "        <ul>"
        "            <li>Каждая буква открытого текста заменяется буквой, расположенной под ней в таблице. Если буква находится в нижней строке таблицы, то она заменяется буквой из верхней строки того же столбца.</li>"
        "        </ul>"
        "    </li>"
        "    <li><strong>Процесс дешифрования:</strong> Дешифрование осуществляется аналогично шифрованию, но буквы заменяются на те, которые находятся над ними в таблице. Если буква находится в верхней строке таблицы, то она заменяется буквой из нижней строки того же столбца.</li>"
        "</ol>"
        "<h3>Пример шифрования</h3>"
        "<p>Рассмотрим пример шифрования слова \"hello\" с использованием вышеуказанной таблицы:</p>"
        "<ol>"
        "    <li>h -> буква под H в таблице: h заменяется на p</li>"
        "    <li>e -> буква под E в таблице: e заменяется на d</li>"
        "    <li>l -> буква под L в таблице: l заменяется на s</li>"
        "    <li>l -> буква под l в таблице: l заменяется на s</li>"
        "    <li>o -> буква под o в таблице: o заменяется на c</li>"
        "</ol>"
        "<p>Таким образом, \"hello\" шифруется как \"pdssc\".</p>"
        "<p>Расшифрование \"pdssc\" шифруется как \"hello\".</p>"
        "<h3>Заключение</h3>"
        "<p>Шифр Трисемуса является простым, но эффективным методом шифрования, который использует таблицу для замены букв. Этот метод обеспечивает более высокую степень безопасности по сравнению с простыми шифрами подстановки, делая его подходящим для различных применений в исторической и современной криптографии.</p>"
    )

    def run_ramzai_cipher(self):
        BUTTON_STYLE_NORMAL = "QPushButton { background-color: white; }"
        BUTTON_STYLE_PRESSED = "QPushButton { background-color: lightblue; }"

        self.ButtonT_1chesary.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonT_2Sloganistic.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonT_3TablPris.setStyleSheet(BUTTON_STYLE_NORMAL)
        self.ButtonT_4Ramzai.setStyleSheet(BUTTON_STYLE_PRESSED)

        self.TextTOutput.setHtml(
            "<h2>Шифр Рамзая</h2>"
            "<h3>Описание</h3>"
            "<p><b>Шифр Рамзая</b> (Ramzey Cipher) представляет собой метод шифрования, основанный на принципе <i>подстановки</i> символов. Этот шифр получил свое название от предполагаемого создателя или пользователя, но конкретные детали о его происхождении часто неизвестны.</p>"
            "<p>Принцип работы шифра Рамзая основан на перестановке символов в алфавите в соответствии с заданным ключом. Алгоритм шифрования включает в себя следующие шаги:</p>"
            "<ol>"
            "    <li><strong>Создание зашифрованного алфавита:</strong> На первом этапе формируется зашифрованный алфавит на основе ключевого слова или фразы, выбранной для шифрования. Ключевое слово используется для определения порядка символов в новом алфавите. Обычно ключевое слово не содержит повторяющихся символов, и все символы приводятся к верхнему регистру.</li>"
            "    <li><strong>Шифрование сообщения:</strong> Каждая буква исходного текста заменяется соответствующей буквой в зашифрованном алфавите. При этом сохраняется регистр символов и пунктуация. Если символ не является буквой алфавита, он остается без изменений.</li>"
            "    <li><strong>Расшифровка сообщения:</strong> Для расшифровки зашифрованного текста используется тот же самый ключ, чтобы восстановить исходный алфавит. Затем каждая буква зашифрованного текста заменяется соответствующей буквой в исходном алфавите.</li>"
            "</ol>"
            "<h3>Пример</h3>"
            "<p>Рассмотрим пример шифрования и дешифрования сообщения \"HELLO WORLD\" с ключевым словом \"CIPHER\":</p>"
            "<p><strong>Шифрование:</strong></p>"
            "<ol>"
            "    <li>Создадим зашифрованный алфавит на основе ключа \"CIPHER\": CIPHERABDGJKLMNQSTUVWXYZ</li>"
            "    <li>Зашифруем сообщение \"HELLO WORLD\", заменяя каждую букву соответствующей буквой в зашифрованном алфавите: \"RJCCP YPSKX\"</li>"
            "</ol>"
            "<p><strong>Дешифрование:</strong></p>"
            "<ol>"
            "    <li>Восстановим исходный алфавит на основе того же ключа \"CIPHER\": ABCDEFGHIJKLMNOPQRSTUVWXYZ</li>"
            "    <li>Расшифруем зашифрованное сообщение \"RJCCP YPSKX\", заменяя каждую букву соответствующей буквой в исходном алфавите: \"HELLO WORLD\"</li>"
            "</ol>"
            "<p>Основным преимуществом шифра Рамзая является простота его реализации и понимания. Однако он обладает недостатком в безопасности, так как существует возможность атаки методом анализа частоты символов.</p>"
            "<p>Шифр Рамзая может быть использован для шифрования текстовых сообщений, но не рекомендуется для защиты конфиденциальной информации из-за своей уязвимости к криптоанализу. Он больше подходит для образовательных целей или в случаях, когда требуется легкая форма шифрования без серьезных требований к безопасности.</p>"
        )

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Лотус", None))
        self.actionButton_1.setText(QCoreApplication.translate("MainWindow", "Цезарь", None))
        self.ButtonT_4Ramzai.setText(QCoreApplication.translate("MainWindow", "Рамзай", None))
        self.ButtonT_1chesary.setText(QCoreApplication.translate("MainWindow", "Цезаря", None))
        self.ButtonT_3TablPris.setText(QCoreApplication.translate("MainWindow", "Табл.Трисемуса", None))
        self.TextTOnButton.setHtml(QCoreApplication.translate("MainWindow",
                                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "hr { height: 1px; border-width: 0; }\n"
                                                              "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                              "li.checked::marker { content: \"\\2612\"; }\n"
                                                              "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Шифры</p></body></html>",
                                                              None))
        self.ButtonT_2Sloganistic.setText(QCoreApplication.translate("MainWindow", "Слогоновый", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1),
                                  QCoreApplication.translate("MainWindow", "Теория", None))
        # self.TextPOnButton.setHtml(QCoreApplication.translate("MainWindow",
        #                                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        #                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        #                                                       "p, li { white-space: pre-wrap; }\n"
        #                                                       "hr { height: 1px; border-width: 0; }\n"
        #                                                       "li.unchecked::marker { content: \"\\2610\"; }\n"
        #                                                       "li.checked::marker { content: \"\\2612\"; }\n"
        #                                                       "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        #                                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Шифры</p></body></html>",
        #                                                       None))
        # self.ButtonP_1chesary.setText(QCoreApplication.translate("MainWindow", "Цезаря", None))
        # self.ButtonP_4Ramzai.setText(QCoreApplication.translate("MainWindow", "Ключевое слово", None))
        # self.ButtonP_2Sloganistic.setText(QCoreApplication.translate("MainWindow", "Слогоновый", None))
        # self.ButtonP_3TablPris.setText(QCoreApplication.translate("MainWindow", "Табл.Присемуса", None))
        # self.pushButton.setText(QCoreApplication.translate("MainWindow", "Проверить", None))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2),
        #                           QCoreApplication.translate("MainWindow", "Практика", None))
        self.TextCDOnButton.setHtml(QCoreApplication.translate("MainWindow",
                                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                               "p, li { white-space: pre-wrap; }\n"
                                                               "hr { height: 1px; border-width: 0; }\n"
                                                               "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                               "li.checked::marker { content: \"\\2612\"; }\n"
                                                               "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Шифры</p></body></html>",
                                                               None))
        self.ButtonCD_3TablPris.setText(QCoreApplication.translate("MainWindow", "Табл.Трисемуса", None))
        self.ButtonCD_2Sloganistic.setText(QCoreApplication.translate("MainWindow", "Слогоновый", None))
        self.ButtonCD_4Ramzai.setText(QCoreApplication.translate("MainWindow", "Рамзай", None))
        self.ButtonCD_1chesary.setText(QCoreApplication.translate("MainWindow", "Цезаря", None))
        self.ButtonCD_Codir.setText(QCoreApplication.translate("MainWindow", "Зашифровать", None))
        self.TextCDCod.setHtml(QCoreApplication.translate("MainWindow",
                                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n"
                                                          "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n"
                                                          "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                          "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Раскодированный текст</span></p></body></html>",
                                                          None))
        self.TextCDDecod.setHtml(QCoreApplication.translate("MainWindow",
                                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "hr { height: 1px; border-width: 0; }\n"
                                                            "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                            "li.checked::marker { content: \"\\2612\"; }\n"
                                                            "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Закодированный текст</span></p></body></html>",
                                                            None))
        self.ButtonCD_Decodir.setText(QCoreApplication.translate("MainWindow", "Дешифровать", None))
        self.textCod1.setHtml(QCoreApplication.translate("MainWindow",
                                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "hr { height: 1px; border-width: 0; }\n"
                                                         "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                         "li.checked::marker { content: \"\\2612\"; }\n"
                                                         "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Ключ</span></p></body></html>",
                                                         None))
        self.textCod2.setHtml(QCoreApplication.translate("MainWindow",
                                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "hr { height: 1px; border-width: 0; }\n"
                                                         "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                         "li.checked::marker { content: \"\\2612\"; }\n"
                                                         "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Ключ</span></p></body></html>",
                                                         None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3),
                                  QCoreApplication.translate("MainWindow", "кодир/декодир", None))
        self.textSteps.setHtml(QCoreApplication.translate("MainWindow",
                                                            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "hr { height: 1px; border-width: 0; }\n"
                                                            "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                            "li.checked::marker { content: \"\\2612\"; }\n"
                                                            "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">\u041f\u043e\u0448\u0430\u0433\u043e\u0432\u0430\u044f \u0440\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f</span></p></body></html>",
                                                            None))

    # retranslateUi
#
