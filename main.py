import sys

from window import *


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
