import sys
from PyQt.QtWidgets import QApplication, QWidget,QLabel
from PyQt.QtGui import QIcon
from PyQt.QtCore import pyqtSlot

def windows():
    app = QApplication(sys.argv);
    widget = QWidget();

    textLabel = QLabel(Widget);
    textLabel.setText('HelloWorld');
    textLabel.move(110,90);

    widget.setGeometry(50,50,320,200);
    widget.setWindowTitle('PyQt5 Example');
    widget.show();

    sys.exit(app.exec_());


if __name__ == '__main__':
    windows();
    
