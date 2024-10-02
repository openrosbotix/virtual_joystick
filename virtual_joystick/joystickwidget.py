from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
import sys
from enum import Enum

class Direction(Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3

class joyStickWidget(QWidget):
    def __init__(self, parent=None):
        super(joyStickWidget, self).__init__(parent)
        self.setMinimumSize(100, 100)
        self.movingOffset = QPointF(0, 0)
        self.grabCenter = False
        self.__maxDistance = 50
        self.angle = 0
        self.distance = 0
        self.normVector = QLineF(QPointF(0,0), QPointF(0,0))


    def paintEvent(self, event):
        painter = QPainter(self)
        bounds = QRectF(-self.__maxDistance, -self.__maxDistance, self.__maxDistance * 2, self.__maxDistance * 2).translated(self._center())
        painter.drawEllipse(bounds)
        painter.setBrush(Qt.black)
        painter.drawEllipse(self._centerEllipse())

    def _centerEllipse(self):
        if self.grabCenter:
            return QRectF(-20, -20, 40, 40).translated(self.movingOffset)
        return QRectF(-20, -20, 40, 40).translated(self._center())

    def _center(self):
        return QPointF(self.width()/2, self.height()/2)


    def _boundJoystick(self, point):
        limitLine = QLineF(self._center(), point)
        if (limitLine.length() > self.__maxDistance):
            limitLine.setLength(self.__maxDistance)
        return limitLine.p2()

    def joystickDirection(self):
        if not self.grabCenter:
            return 0
        self.normVector = QLineF(self._center(), self.movingOffset)
        currentDistance = self.normVector.length()
        self.angle = self.normVector.angle()

        self.distance = min(currentDistance / self.__maxDistance, 1.0)
        if 45 <= self.angle < 135:
            return (Direction.Up, self.distance)
        elif 135 <= self.angle < 225:
            return (Direction.Left, self.distance)
        elif 225 <= self.angle < 315:
            return (Direction.Down, self.distance)
        return (Direction.Right, self.distance)


    def mousePressEvent(self, ev):
        self.grabCenter = self._centerEllipse().contains(ev.pos())
        return super().mousePressEvent(ev)

    def mouseReleaseEvent(self, event):
        self.grabCenter = False
        self.movingOffset = QPointF(0, 0)
        self.angle = 0
        self.distance = 0
        self.update()

    def mouseMoveEvent(self, event):
        if self.grabCenter:
            self.movingOffset = self._boundJoystick(event.pos())
            self.update()
            self.joystickDirection()