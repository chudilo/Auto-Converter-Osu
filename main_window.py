from PyQt5.QtWidgets import * #(QWidget, QLabel, QApplication)
import sys

def main():
    app = QApplication(sys.argv)
    m = QWidget()
    m.resize(100,100)
    m.move(1000,1000)
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        bar = self.menuBar()

        menu = bar.addMenu('Menu')
        act = menu.addAction('Open_file')
        act.triggered.connect(self.showMaximized)
        
if __name__ == '__main__':
    main()

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
