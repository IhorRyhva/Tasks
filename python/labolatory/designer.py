from PyQt5 import QtWidgets, uic

class TextEncryptionApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("designer.ui", self)

        self.pushButton_2.clicked.connect(self.encrypt_text)
        self.pushButton_3.clicked.connect(self.decrypt_text)

    def encrypt_text(self):
        key = self.spinBox_2.value()
        text = self.textEdit_2.toPlainText()
        list_text = list(text)
        script = ""

        while key > 0:
            i = 0
            while i < len(list_text):
                a = i + 1
                if a % key == 0:
                    if list_text[i] != '0':
                        script += list_text[i]
                    list_text[i] = '0'
                i += 1
            key -= 1

        self.textEdit_3.setPlainText(script)

    def decrypt_text(self):
        key = int(self.spinBox_2.value())
        text = self.textEdit_2.toPlainText()
        list_text = list(text)
        length = len(list_text)
        script = ""

        lengthNewList = int(length / 2)
        
        if key % 2 == 0:
            count = key / 2
            count = int(count)
            for i in range(count):
                first = []
                second = []
                for i in range(length):
                    if i < lengthNewList:
                        second += list_text[i]
                    else:
                        first += list_text[i]

                a = 0
                b = 0
                for i in range(length):
                    numberOfNumber = i + 1
                    if numberOfNumber % 2 != 0:
                        list_text[i] = first[a]
                        a += 1
                    else:
                        list_text[i] = second[b]
                        b += 1
            for i in range(length):
                script += list_text[i]

        self.textEdit_3.setPlainText(script)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = TextEncryptionApp()
    window.show() 
    sys.exit(app.exec_())