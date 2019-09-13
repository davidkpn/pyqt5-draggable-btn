"""
Owner: David K.
Use this to make any widget to be a visually draggable.
this Class will make the Object dragged within his parent element.
drag will occur on left mouse click hold, change lines 26, 33 to RightButton
for dragging on right mouse click.
"""
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt

# inherits from QWidget,
class Draggable(QPushButton):
    def __init__(self, title, parent):
        super(Draggable, self).__init__(title, parent)
        self.initUI()

    def initUI(self):
        """
        Add elements on the dragable widget/button
        """
        pass

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()
        super(Draggable, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            widget_pos = self.mapToGlobal(self.pos())
            mouse_pos = event.globalPos()
            diff = mouse_pos - self.__mouseMovePos
            new_pos = self.mapFromGlobal(widget_pos + diff)
            parent_height = self.parent().height()
            parent_width = self.parent().width()
            if mouse_pos.x() not in range(int(parent_width*.05), int(parent_width *.95))  or mouse_pos.y() not in range(int(parent_height*.05),int(parent_height*.95)):
                return
            self.move(new_pos)
            self.__mouseMovePos = mouse_pos
        super(Draggable, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return
        super(Draggable, self).mouseReleaseEvent(event)
