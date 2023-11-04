# UI
import math
import random
import re
import sys
from collections import Counter

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from num2words import num2words
from unidecode import unidecode

qtCreatorFile = "kryptoUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


def jedinecne(string):
    freq = Counter(string)

    if (len(freq) == len(string)):
        return True
    else:
        return False


def listnastring(s):
    # initialize an empty string
    str1 = ""
    return (str1.join(s))


def index2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return i, x.index(v)


class MyApp(QMainWindow, Ui_MainWindow):
    def change(self):
        if self.matica_5X5.isChecked():
            self.tableWidget_2.hide()
            self.tableWidget.show()
            self.label_3.show()
            self.label_4.hide()

        elif self.matica_6X6.isChecked():
            self.tableWidget.hide()
            self.tableWidget_2.show()
            self.label_3.hide()
            self.label_4.show()

    def check(self):
        check = False
        if self.matica_5X5.isChecked():
            if self.CheckBox_JazykCZ.isChecked():
                Abeceda = ""
                test = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
                for i in range(5):
                    for j in range(5):
                        widgetItem = self.tableWidget.item(i, j)
                        Abeceda += (widgetItem.text())

                if jedinecne(Abeceda) == True and sorted(Abeceda) == sorted(test):
                    check = True
                elif jedinecne(Abeceda) == False:
                    self.labelVysledek.setText("!Duplicita!")
                elif sorted(Abeceda) != sorted(test):
                    self.labelVysledek.setText("Pouzite nedovolene znaky")
                else:
                    self.labelVysledek.setText("Error")
            elif self.CheckBox_JazykEN.isChecked():
                Abeceda = ""
                test = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
                for i in range(5):
                    for j in range(5):
                        widgetItem = self.tableWidget.item(i, j)
                        Abeceda += (widgetItem.text())

                if jedinecne(Abeceda) == True and sorted(Abeceda) == sorted(test):
                    self.labelVysledek.setText("Vše je správně")
                    check = True
                elif jedinecne(Abeceda) == False:
                    self.labelVysledek.setText("!Duplicita!")
                elif sorted(Abeceda) != test:
                    self.labelVysledek.setText("PouZite nedovolene znaky")
                else:
                    self.labelVysledek.setText("Error")
            else:
                self.labelVysledok.setText("Error")

        elif self.matica_6X6.isChecked():
            Abeceda = ""
            test = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            for i in range(6):
                for j in range(6):
                    widgetItem = self.tableWidget_2.item(i, j)
                    Abeceda += (widgetItem.text())
            if jedinecne(Abeceda) == True and sorted(Abeceda) == sorted(test):
                check = True
            elif jedinecne(Abeceda) == False:
                self.labelVysledek.setText("!Duplicita!")
            elif sorted(Abeceda) != sorted(test):
                self.labelVysledek.setText("Pouzite nedovolene znaky")
            else:
                self.labelVysledek.setText("Error")
        return check

    def clean(self):
        if self.matica_6X6.isChecked():
            for i in range(6):
                for j in range(6):
                    self.tableWidget_2.setItem(i, j, QTableWidgetItem(""))
        else:
            for i in range(5):
                for j in range(5):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(""))

    def generate(self):
        if self.matica_5X5.isChecked():
            self.tableWidget_2.hide()
            self.tableWidget.show()
            self.label_3.show()
            self.label_4.hide()
            Abeceda = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            random.shuffle(Abeceda)
            Abeceda = listnastring(Abeceda)

            if self.CheckBox_JazykCZ.isChecked():
                Abeceda = Abeceda.replace("J", "")
            elif self.CheckBox_JazykEN.isChecked():
                Abeceda = Abeceda.replace("Q", "")
            else:
                self.labelVysledek.setText("Vyberte jazyk")

            Abeceda = list(Abeceda)
            f = 0
            for i in range(5):
                for j in range(5):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(Abeceda[f]))
                    f += 1
        else:
            self.tableWidget.hide()
            self.tableWidget_2.show()
            self.label_3.hide()
            self.label_4.show()
            Abeceda = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            random.shuffle(Abeceda)
            Abeceda = listnastring(Abeceda)
            Abeceda = list(Abeceda)
            f = 0
            for i in range(6):
                for j in range(6):
                    self.tableWidget_2.setItem(i, j, QTableWidgetItem(Abeceda[f]))
                    f += 1
        return Abeceda

    def encrypt6x6(self):

        list_slov = {
            "0": "A",
            "1": "D",
            "2": "F",
            "3": "G",
            "4": "V",
            "5": "X"
        }

        key = str(self.plainTextEdit_A.toPlainText())
        if key.isdigit():
            self.labelVysledek.setText("zadajte platne klucove slovo")
            exit()

        key = unidecode(key)
        for k in key.split("\n"):
            key = (re.sub(r"[^a-zA-Z0-9]+", '', k))
        key = key.upper()

        input = str(self.plainTextEdit_Input.toPlainText())
        input = unidecode(input)
        input = input.replace(" ", "XmezeraX")

        for k in input.split("\n"):
            input = (re.sub(r"[^a-zA-Z0-9]+", '', k))

        input = input.upper()

        subs = []

        matrix_abcd = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        for i in range(6):
            for j in range(6):
                widgetItem = self.tableWidget_2.item(i, j)
                matrix_abcd[i][j] = widgetItem.text()

        i = 0
        j = 0
        while i < len(input):
            index1 = index2d(matrix_abcd, input[i])
            j = str(index1[0])
            k = str(index1[1])
            subs.append(j)
            subs.append(k)
            i += 1
        for i in range(len(subs)):
            subs[i] = list_slov[subs[i]]
        subs = listnastring(subs)

        serazeny_ks = list(key)
        serazeny_ks.sort()

        cols = len(key)
        rows = math.ceil(len(subs) / len(key))
        matrix_trans = [[0] * cols for y in range(rows)]

        k = 0
        i = 0
        j = 0

        for i in range(rows):
            for j in range(cols):
                if k == len(subs):
                    break
                else:
                    matrix_trans[i][j] = subs[k]
                    k += 1

        trans = []
        i = 0
        j = 0
        k = 0
        KS = list(key)

        for i in range(0, len(key)):
            for j in range(0, len(key)):
                if serazeny_ks[i] == KS[j]:
                    for k in range(0, len(matrix_trans)):
                        if (matrix_trans[k][j] == 0):
                            continue
                        else:
                            trans.append(matrix_trans[k][j])
                    KS[j] = "#"
        trans = listnastring(trans)
        trans = ' '.join([trans[i:i + 5] for i in range(0, len(trans), 5)])

        self.labelVysledek.setText(trans)

    def encrypt(self):

        list_slov = {
            "0": "A",
            "1": "D",
            "2": "F",
            "3": "G",
            "4": "X"
        }

        key = str(self.plainTextEdit_A.toPlainText())
        if key.isdigit():
            self.labelVysledek.setText("Zadejte platný key")
            exit()

        key = unidecode(key)
        for k in key.split("\n"):
            key = (re.sub(r"[^a-zA-Z0-9]+", '', k))

        key = key.upper()

        input = str(self.plainTextEdit_Input.toPlainText())

        i = 0
        while i < len(input):
            if input[i].isdigit():
                if self.CheckBox_JazykCZ.isChecked():
                    x = num2words(input[i], lang="cz")
                elif self.CheckBox_JazykEN.isChecked():

                    x = num2words(input[i], lang="en")
                else:
                    self.labelVysledek.setText("Vyberte možnosť jazyka")
                    exit(1)

                input = input.replace(input[i], x)
            i += 1

        input = unidecode(input)
        input = input.replace(" ", "XmezeraX")

        for k in input.split("\n"):
            input = (re.sub(r"[^a-zA-Z0-9]+", '', k))

        input = input.upper()
        if self.CheckBox_JazykCZ.isChecked():
            input = input.replace("J", "I")
        elif self.CheckBox_JazykEN.isChecked():
            input = input.replace("Q", "O")

        subs = []

        matrix_abcd = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        for i in range(5):
            for j in range(5):
                widgetItem = self.tableWidget.item(i, j)
                matrix_abcd[i][j] = widgetItem.text()

        i = 0
        j = 0
        while i < len(input):
            index1 = index2d(matrix_abcd, input[i])
            j = str(index1[0])
            k = str(index1[1])
            subs.append(j)
            subs.append(k)
            i += 1
        for i in range(len(subs)):
            subs[i] = list_slov[subs[i]]
        subs = listnastring(subs)

        serazeny_ks = list(key)
        serazeny_ks.sort()

        cols = len(key)
        rows = math.ceil(len(subs) / len(key))
        matrix_trans = [[0] * cols for y in range(rows)]

        k = 0
        i = 0
        j = 0

        for i in range(rows):
            for j in range(cols):
                if k == len(subs):
                    break
                else:
                    matrix_trans[i][j] = subs[k]
                    k += 1

        trans = []
        i = 0
        j = 0
        k = 0
        KS = list(key)

        for i in range(0, len(key)):
            for j in range(0, len(key)):
                if serazeny_ks[i] == KS[j]:
                    for k in range(0, len(matrix_trans)):
                        if (matrix_trans[k][j] == 0):
                            continue
                        else:
                            trans.append(matrix_trans[k][j])
                    KS[j] = "#"
        trans = listnastring(trans)
        trans = ' '.join([trans[i:i + 5] for i in range(0, len(trans), 5)])

        self.labelVysledek.setText(trans)

    def decrypt(self):

        list_slov = {
            "A": 0,
            "D": 1,
            "F": 2,
            "G": 3,
            "X": 4
        }

        key = str(self.plainTextEdit_A.toPlainText())

        if key.isdigit():
            """self.labelVysledek.setText(Zadejte platný key")"""
            exit()

        key = unidecode(key)
        for k in key.split("\n"):
            key = (re.sub(r"[^a-zA-Z0-9]+", '', k))

        key = key.upper()

        input = str(self.plainTextEdit_Input.toPlainText())

        input = input.upper()
        input = input.replace(" ", "")
        if self.CheckBox_JazykCZ.isChecked():
            input = input.replace("J", "I")
        elif self.CheckBox_JazykEN.isChecked():
            input = input.replace("Q", "O")

        cols = len(key)
        rows = math.ceil(len(input) / len(key))
        matrix_trans = [[0] * cols for y in range(rows)]
        Sortedmatrix_trans = [[0] * cols for y in range(rows)]

        if len(input) % len(key) > 0:
            doplnok = ((math.ceil(len(input) / len(key)) * len(key)) - len(input))
        else:
            doplnok = 0

        if doplnok != 0:
            for i in range(0, doplnok):
                matrix_trans[rows - 1][cols - i - 1] = "#"

        serazeny_ks = list(key)
        serazeny_ks.sort()
        KS = list(key)

        for i in range(0, len(key)):
            for j in range(0, len(key)):
                if serazeny_ks[i] == KS[j]:
                    for k in range(0, len(matrix_trans)):
                        Sortedmatrix_trans[k][i] = matrix_trans[k][j]
                    serazeny_ks[i] = "@"
                    KS[j] = "/"

        k = 0
        i = 0
        j = 0

        for i in range(cols):
            for j in range(rows):
                if k == len(input):
                    break
                else:
                    if Sortedmatrix_trans[j][i] != "#":
                        Sortedmatrix_trans[j][i] = input[k]
                        k += 1
                    else:
                        continue

        trans = []
        i = 0
        j = 0
        k = 0
        serazeny_ks = list(key)
        serazeny_ks.sort()
        KS = list(key)

        for i in range(0, len(key)):
            for j in range(0, len(key)):
                if KS[i] == serazeny_ks[j]:
                    for k in range(0, len(Sortedmatrix_trans)):
                        matrix_trans[k][i] = Sortedmatrix_trans[k][j]
                    KS[i] = "@"
                    serazeny_ks[j] = "/"

        for i in range(0, rows):
            for j in range(0, cols):
                if matrix_trans[i][j] != "#":
                    trans.append(matrix_trans[i][j])
                else:
                    continue

        for i in range(len(trans)):
            trans[i] = list_slov[trans[i]]

        matrix_abcd = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        for i in range(5):
            for j in range(5):
                widgetItem = self.tableWidget.item(i, j)
                matrix_abcd[i][j] = widgetItem.text()

        subs = []
        i = 0
        k = 0
        while i < len(trans):
            j = trans[i]
            l = trans[i + 1]
            subs.append(matrix_abcd[j][l])
            i += 2

        subs = listnastring(subs)
        subs = subs.replace("XMEZERAX", " ")
        if self.CheckBox_JazykCZ.isChecked():
            subs = subs.replace("IEDNA", "1").replace("DVA", "2").replace("TRI", "3").replace("CTYRI",
                                                                                                            "4").replace(
                "PET", "5").replace("SEST", "6").replace("SEDM", "7").replace("OSM", "8").replace("DEVET", "9").replace(
                "NULA", "0")
        elif self.CheckBox_JazykEN.isChecked():
            subs = subs.replace("ONE", "1").replace("TWO", "2").replace("THREE", "3").replace("FOUR",
                                                                                                            "4").replace(
                "FIVE", "5").replace("SIX", "6").replace("SEVEN", "7").replace("EIGHT", "8").replace("NINE",
                                                                                                     "9").replace(
                "ZERO", "0")
        self.labelVysledek.setText(subs)

    def decrypt6x6(self):

        list_slov = {
            "A": 0,
            "D": 1,
            "F": 2,
            "G": 3,
            "V": 4,
            "X": 5
        }

        key = str(self.plainTextEdit_A.toPlainText())

        if key.isdigit():
            """self.labelVysledek.setText("Zadejte platný key")"""
            exit()

        key = unidecode(key)
        for k in key.split("\n"):
            key = (re.sub(r"[^a-zA-Z0-9]+", '', k))

        key = key.upper()

        input = str(self.plainTextEdit_Input.toPlainText())

        input = input.upper()
        input = input.replace(" ", "")

        cols = len(key)
        rows = math.ceil(len(input) / len(key))
        matrix_trans = [[0] * cols for y in range(rows)]
        Sortedmatrix_trans = [[0] * cols for y in range(rows)]

        if len(input) % len(key) > 0:
            doplnok = ((math.ceil(len(input) / len(key)) * len(key)) - len(input))
        else:
            doplnok = 0
        if doplnok != 0:
            for i in range(0, doplnok):
                matrix_trans[rows - 1][cols - i - 1] = "#"

        serazeny_ks = list(key)
        serazeny_ks.sort()
        KS = list(key)

        for i in range(0, len(key)):
            for j in range(0, len(key)):
                if serazeny_ks[i] == KS[j]:
                    for k in range(0, len(matrix_trans)):
                        Sortedmatrix_trans[k][i] = matrix_trans[k][j]
                    serazeny_ks[i] = "@"
                    KS[j] = "/"

        k = 0
        i = 0
        j = 0

        for i in range(cols):
            for j in range(rows):
                if k == len(input):
                    break
                else:
                    if Sortedmatrix_trans[j][i] != "#":
                        Sortedmatrix_trans[j][i] = input[k]
                        k += 1
                    else:
                        continue

        trans = []
        i = 0
        j = 0
        k = 0
        serazeny_ks = list(key)
        serazeny_ks.sort()
        KS = list(key)

        for i in range(0, len(key)):
            for j in range(0, len(key)):
                if KS[i] == serazeny_ks[j]:
                    for k in range(0, len(Sortedmatrix_trans)):
                        matrix_trans[k][i] = Sortedmatrix_trans[k][j]
                    KS[i] = "@"
                    serazeny_ks[j] = "/"

        for i in range(0, rows):
            for j in range(0, cols):
                if matrix_trans[i][j] != "#":
                    trans.append(matrix_trans[i][j])
                else:
                    continue

        for i in range(len(trans)):
            trans[i] = list_slov[trans[i]]

        matrix_abcd = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

        for i in range(6):
            for j in range(6):
                widgetItem = self.tableWidget_2.item(i, j)
                matrix_abcd[i][j] = widgetItem.text()

        subs = []
        i = 0
        k = 0
        while i < len(trans):
            j = trans[i]
            l = trans[i + 1]
            subs.append(matrix_abcd[j][l])
            i += 2

        subs = listnastring(subs)
        subs = subs.replace("XMEZERAX", " ")
        self.labelVysledek.setText(subs)

    def execute(self):
        ks = self.plainTextEdit_A.toPlainText()
        ks = ks.replace(" ", "")
        if self.CheckBox_Desifrovat.isChecked() and self.matica_5X5.isChecked() and self.check() == True and len(
                ks) > 0:

            string = self.plainTextEdit_Input.toPlainText()
            string = string.replace(" ", "")

            if len(string) % 2 == 0:
                self.decrypt()
            elif len(string) % 2 != 0:
                self.labelVysledek.setText("Nespravny input")

        elif self.CheckBox_Sifrovat.isChecked() and self.matica_5X5.isChecked() and self.check() == True and len(
                ks) > 0:
            self.encrypt()
        elif self.CheckBox_Sifrovat.isChecked() and self.matica_6X6.isChecked() and self.check() == True and len(
                ks) > 0:
            self.encrypt6x6()
        elif self.CheckBox_Desifrovat.isChecked() and self.matica_6X6.isChecked() and self.check() == True and len(
                ks) > 0:
            string = self.plainTextEdit_Input.toPlainText()
            string = string.replace(" ", "")
            if len(string) % 2 == 0:
                self.decrypt6x6()
            else:
                self.labelVysledek.setText("Nesprávný input")

        elif self.check() == False:
            self.labelVysledek.setText("Opravte matici kontrolu můžete provést tlačítkem kontrola")

        elif len(ks) == 0:
            self.labelVysledek.setText("Zdejte platný klíč")

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Button_Execute.clicked.connect(self.execute)
        self.Button_Generate.clicked.connect(self.generate)
        self.Button_Reset.clicked.connect(self.clean)
        self.pushButtonKontrola.clicked.connect(self.check)
        self.tableWidget_2.hide()
        self.pushButton.clicked.connect(self.change)
        self.label_4.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
