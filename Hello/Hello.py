import sys
from PySide.QtCore import *
from PySide.QtGui import *


class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([QPoint(170, 100), QPoint(50, 110), QPoint(132, 100), QPoint(100, 150)])
        p.drawPolygon([QPoint(1, 10), QPoint(5, 110), QPoint(12, 102), QPoint(10, 15)])
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 120, 100, 100, 0, 180 * 16)
        p.drawPie(10, 120, 140, 120, 10, 80 * 10)

        p.drawPolygon([QPoint(50, 200), QPoint(150, 20), QPoint(10, 40)])

        p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
        p.end()


class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 200, 100, 100, 0, 180 * 16)
        p.drawPie(10, 200, 140, 120, 10, 80 * 10)

        p.drawPolygon([QPoint(50, 2), QPoint(150, 20), QPoint(10, 40)])

        p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
        p.end()
def main():
    app = QApplication(sys.argv)
    w1=Simple_drawing_window1()
    w1.show()
    w2=Simple_drawing_window2()
    w2.show()
    w3=Simple_drawing_window3()
    w3.show()

    return app.exec_()
if __name__ == "__main__":
    sys.exit(main())

  
