import sys
from PyQt5.QtGui import QPainter, QPen, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt, QPoint, QLineF


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 700, 500)
        self.image = QImage(self.size(), QImage.Format_ARGB32_Premultiplied)
        self.image.fill(Qt.white)
        self.start = QPoint()
        self.lines = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.white);

        for line in self.lines:
            start, end, color, thick, style = line
            painter.setPen(QPen(color, thick, style))
            painter.drawLine(start, end)

        painter.drawImage(self.rect(), self.image, self.image.rect())


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.image.fill(Qt.transparent)
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
            painter.drawLine(self.start, event.pos())
            self.update()

    def mouseReleaseEvent(self, event):
        self.lines.append((self.start, event.pos(), Qt.black, 5, Qt.SolidLine))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec_())
