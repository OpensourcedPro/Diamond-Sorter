import sys
from PyQt5.QtWidgets import QApplication,  QVBoxLayout, QMenu,QLabel,QHBoxLayout, QPushButton, QWidget, QSizePolicy,QListWidgetItem,QListWidget,QAction
from PyQt5.QtCore import pyqtSignal,QPropertyAnimation, QRect, pyqtProperty, Qt,QPoint,pyqtSlot,QSize
from PyQt5.QtGui import QPainter,  QColor,QBrush,QFont
from qfluentwidgets import DropDownToolButton,RoundMenu,FluentStyleSheet,PrimaryPushButton,isDarkTheme
from PyQt5.QtCore import QEvent
def AvatarFromEncodedText(text):
    import base64
    encoded_bytes = text.encode('utf-8')
    avatar = base64.b64decode(encoded_bytes)
    return avatar
class ReceiveMessageEvent(QEvent):
    EventType = QEvent.Type(QEvent.registerEventType())

    def __init__(self, data,fromGroup=False):
        super().__init__(ReceiveMessageEvent.EventType)
        self.data = data
        self.fromGroup = fromGroup
class NewUserJoinGroupEvent(QEvent):
    EventType = QEvent.Type(QEvent.registerEventType())

    def __init__(self, data):
        super().__init__(NewUserJoinGroupEvent.EventType)
        self.data = data
class ListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 禁用垂直滚动条
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 禁用水平滚动条
        self.setResizeMode(QListWidget.Adjust)
    def addWidgetItem(self, widget):

        item = QListWidgetItem(self)

        size = widget.sizeHint()
        item.setSizeHint(size)

        self.addItem(item)
        self.setItemWidget(item, widget)
        
    def showContextMenu(self, position):
        menu = QMenu()
        remove_action = menu.addAction("Remove")
        action = menu.exec_(self.mapToGlobal(position))
        
        if action == remove_action:
            # 从列表中删除选中的项
            item = self.itemAt(position)
            if item:
                widget = self.itemWidget(item)
                widget.deleteLater()  # 删除小部件
                self.takeItem(self.row(item))  # 从列表中移除项
class BadgeLabel(QLabel):
    def __init__(self, parent=None):
        super(BadgeLabel, self).__init__(parent)
        self.badgeValue = 0
        size = 15
        self.setMaximumHeight(size)
        self.setMaximumWidth(size)
        self.setMinimumHeight(size)
        self.setMinimumWidth(size)
        self.setStyleSheet("background-color: none;")
    def setBadgeValue(self, value):
        self.badgeValue = value
        self.update()  # 触发重绘

    def paintEvent(self, event):
        super(BadgeLabel, self).paintEvent(event)
        if self.badgeValue > 0:
            painter = QPainter(self)
            badgeRect = QRect(0, 0, self.width(), self.height())  # 角标位置和大小
            painter.setBrush(QBrush(QColor(255, 0, 0)))  # 红色背景
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(badgeRect)

            painter.setPen(Qt.yellow)
            painter.setFont(QFont("Arial", 10, QFont.Bold))
            painter.drawText(badgeRect, Qt.AlignCenter, str(self.badgeValue))

class BadgeWidget(QWidget):
    clicked = pyqtSignal()
    valueChanged = pyqtSignal(int)
    def __init__(self, parent=None):
        super(BadgeWidget, self).__init__(parent)
        self.notification_count = 5
        self.countWidget = BadgeLabel(self)
        self.initUI()
        self.countWidget.move(self.width()-self.countWidget.width()-50,0)
        self.count = 0
    def initUI(self):
        self.save_width = 170
        self.setMaximumHeight(30)
        self.setMaximumWidth(self.save_width)
        self.setMinimumWidth(self.save_width)
        self.setFixedWidth(self.save_width)

        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        # 设置默认样式
        self.setStyleSheet("background-color: none;")
    def sizeHint(self) -> QSize:
        return QSize(self.save_width, 30)
    def size(self) -> QSize:
        print("countWidget:",self.countWidget.size())
        print("countWidget position:",self.countWidget.pos().x(),self.countWidget.pos().y())
        return QSize(self.save_width, 30)
    def setBadge(self, count):
        if self.count !=count:
            self.count = count
            self.countWidget.setBadgeValue(self.count)
            self.valueChanged.emit(self.count)
    def clearBadge(self):
        self.setBadge(0)
    def increaseBadge(self):
        self.setBadge(self.count+1)
class MyRoundMenu(RoundMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def addWidget(self, widget: QWidget,action: QAction, selectable=True, onClick=None):
        action.setProperty('selectable', selectable)

        item = self._createActionItem(action)
        print("widgetsize:",widget.size())
        item.setSizeHint(widget.size())

        self.view.addItem(item)
        self.view.setItemWidget(item, widget)

        if not selectable:
            item.setFlags(Qt.NoItemFlags)

        if onClick:
            action.triggered.connect(onClick)

        self.adjustSize()
class MyDropDownToolButton(DropDownToolButton):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.badgeLabel = BadgeLabel(self)
        self.badgeLabel.move(0,0)
    def setBadgeValue(self, value):
        self.badgeLabel.setBadgeValue(value)
        if value <= 0:
            if self.badgeLabel.isVisible():
                self.badgeLabel.hide()
        else:
            if not self.badgeLabel.isVisible():
                self.badgeLabel.show()
class FramelessWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.oldPos = self.pos()
    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QLabel,QHBoxLayout,QSizePolicy,QPushButton,QSpacerItem
from PyQt5.QtGui import QFontMetrics, QPixmap, QFont
from ui.Ui_RequestItem import Ui_RequestItem
from qfluentwidgets import Pivot, setTheme, Theme,ImageLabel,CaptionLabel,FluentStyleSheet,PrimaryPushButton
from PyQt5.QtCore import QEasingCurve, QPropertyAnimation, Qt, QEvent
from PyQt5.QtGui import QColor, QResizeEvent
from PyQt5.QtWidgets import (QDialog, QGraphicsDropShadowEffect,
                             QGraphicsOpacityEffect, QHBoxLayout, QWidget, QFrame)


class MaskBase(QDialog):
    """ Dialog box base class with a mask """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._hBoxLayout = QHBoxLayout(self)
        self.windowMask = QWidget(self)

        # dialog box in the center of mask, all widgets take it as parent
        self.widget = QFrame(self, objectName='centerWidget')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(0, 0, parent.width(), parent.height())
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        c = 255
        self.windowMask.resize(self.size())
        self.windowMask.setStyleSheet(f'background:rgba({c}, {c}, {c}, 0.6)')
        self._hBoxLayout.addWidget(self.widget)
        self.setShadowEffect()
        self.setLayout(self._hBoxLayout)
        # self.window().installEventFilter(self)

    def setShadowEffect(self, blurRadius=60, offset=(0, 10), color=QColor(0, 0, 0, 100)):
        """ add shadow to dialog """
        shadowEffect = QGraphicsDropShadowEffect(self.widget)
        shadowEffect.setBlurRadius(blurRadius)
        shadowEffect.setOffset(*offset)
        shadowEffect.setColor(color)
        self.widget.setGraphicsEffect(None)
        self.widget.setGraphicsEffect(shadowEffect)

    def setMaskColor(self, color: QColor):
        """ set the color of mask """
        self.windowMask.setStyleSheet(f"""
            background: rgba({color.red()}, {color.blue()}, {color.green()}, {color.alpha()})
        """)

    def showEvent(self, e):
        """ fade in """
        opacityEffect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(opacityEffect)
        opacityAni = QPropertyAnimation(opacityEffect, b'opacity', self)
        opacityAni.setStartValue(0)
        opacityAni.setEndValue(1)
        opacityAni.setDuration(200)
        opacityAni.setEasingCurve(QEasingCurve.InSine)
        opacityAni.finished.connect(opacityEffect.deleteLater)
        opacityAni.start()
        super().showEvent(e)

    def done(self, code):
        """ fade out """
        self.widget.setGraphicsEffect(None)
        opacityEffect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(opacityEffect)
        opacityAni = QPropertyAnimation(opacityEffect, b'opacity', self)
        opacityAni.setStartValue(1)
        opacityAni.setEndValue(0)
        opacityAni.setDuration(100)
        opacityAni.finished.connect(lambda: QDialog.done(self, code))
        opacityAni.start()

    def resizeEvent(self, e):
        self.windowMask.resize(self.parent().size())
    def eventFilter(self, obj, e: QEvent):
        mapping ={QEvent.Type.None_ : "None_",
        QEvent.Type.Timer : "Timer",
        QEvent.Type.MouseButtonPress : "MouseButtonPress",
        QEvent.Type.MouseButtonRelease : "MouseButtonRelease",
        QEvent.Type.MouseButtonDblClick : "MouseButtonDblClick",
        QEvent.Type.MouseMove : "MouseMove",
        QEvent.Type.KeyPress : "KeyPress",
        QEvent.Type.KeyRelease : "KeyRelease",
        QEvent.Type.FocusIn : "FocusIn",
        QEvent.Type.FocusOut : "FocusOut",
        QEvent.Type.Enter : "Enter",
        QEvent.Type.Leave : "Leave",
        QEvent.Type.Paint : "Paint",
        QEvent.Type.Move : "Move",
        QEvent.Type.Resize : "Resize",
        QEvent.Type.Show : "Show",
        QEvent.Type.Hide : "Hide",
        QEvent.Type.Close : "Close",
        QEvent.Type.ParentChange : "ParentChange",
        QEvent.Type.ParentAboutToChange : "ParentAboutToChange",
        QEvent.Type.ThreadChange : "ThreadChange",
        QEvent.Type.WindowActivate : "WindowActivate",
        QEvent.Type.WindowDeactivate : "WindowDeactivate",
        QEvent.Type.ShowToParent : "ShowToParent",
        QEvent.Type.HideToParent : "HideToParent",
        QEvent.Type.Wheel : "Wheel",
        QEvent.Type.WindowTitleChange : "WindowTitleChange",
        QEvent.Type.WindowIconChange : "WindowIconChange",
        QEvent.Type.ApplicationWindowIconChange : "ApplicationWindowIconChange",
        QEvent.Type.ApplicationFontChange : "ApplicationFontChange",
        QEvent.Type.ApplicationLayoutDirectionChange : "ApplicationLayoutDirectionChange",
        QEvent.Type.ApplicationPaletteChange : "ApplicationPaletteChange",
        QEvent.Type.PaletteChange : "PaletteChange",
        QEvent.Type.Clipboard : "Clipboard",
        QEvent.Type.MetaCall : "MetaCall",
        QEvent.Type.SockAct : "SockAct",
        QEvent.Type.WinEventAct : "WinEventAct",
        QEvent.Type.DeferredDelete : "DeferredDelete",
        QEvent.Type.DragEnter : "DragEnter",
        QEvent.Type.DragMove : "DragMove",
        QEvent.Type.DragLeave : "DragLeave",
        QEvent.Type.Drop : "Drop",
        QEvent.Type.ChildAdded : "ChildAdded",
        QEvent.Type.ChildPolished : "ChildPolished",
        QEvent.Type.ChildRemoved : "ChildRemoved",
        QEvent.Type.PolishRequest : "PolishRequest",
        QEvent.Type.Polish : "Polish",
        QEvent.Type.LayoutRequest : "LayoutRequest",
        QEvent.Type.UpdateRequest : "UpdateRequest",
        QEvent.Type.UpdateLater : "UpdateLater",
        QEvent.Type.ContextMenu : "ContextMenu",
        QEvent.Type.InputMethod : "InputMethod",
        QEvent.Type.TabletMove : "TabletMove",
        QEvent.Type.LocaleChange : "LocaleChange",
        QEvent.Type.LanguageChange : "LanguageChange",
        QEvent.Type.LayoutDirectionChange : "LayoutDirectionChange",
        QEvent.Type.TabletPress : "TabletPress",
        QEvent.Type.TabletRelease : "TabletRelease",
        QEvent.Type.OkRequest : "OkRequest",
        QEvent.Type.IconDrag : "IconDrag",
        QEvent.Type.FontChange : "FontChange",
        QEvent.Type.EnabledChange : "EnabledChange",
        QEvent.Type.ActivationChange : "ActivationChange",
        QEvent.Type.StyleChange : "StyleChange",
        QEvent.Type.IconTextChange : "IconTextChange",
        QEvent.Type.ModifiedChange : "ModifiedChange",
        QEvent.Type.MouseTrackingChange : "MouseTrackingChange",
        QEvent.Type.WindowBlocked : "WindowBlocked",
        QEvent.Type.WindowUnblocked : "WindowUnblocked",
        QEvent.Type.WindowStateChange : "WindowStateChange",
        QEvent.Type.ToolTip : "ToolTip",
        QEvent.Type.WhatsThis : "WhatsThis",
        QEvent.Type.StatusTip : "StatusTip",
        QEvent.Type.ActionChanged : "ActionChanged",
        QEvent.Type.ActionAdded : "ActionAdded",
        QEvent.Type.ActionRemoved : "ActionRemoved",
        QEvent.Type.FileOpen : "FileOpen",
        QEvent.Type.Shortcut : "Shortcut",
        QEvent.Type.ShortcutOverride : "ShortcutOverride",
        QEvent.Type.WhatsThisClicked : "WhatsThisClicked",
        QEvent.Type.ToolBarChange : "ToolBarChange",
        QEvent.Type.ApplicationActivate : "ApplicationActivate",
        QEvent.Type.ApplicationActivated : "ApplicationActivated",
        QEvent.Type.ApplicationDeactivate : "ApplicationDeactivate",
        QEvent.Type.ApplicationDeactivated : "ApplicationDeactivated",
        QEvent.Type.QueryWhatsThis : "QueryWhatsThis",
        QEvent.Type.EnterWhatsThisMode : "EnterWhatsThisMode",
        QEvent.Type.LeaveWhatsThisMode : "LeaveWhatsThisMode",
        QEvent.Type.ZOrderChange : "ZOrderChange",
        QEvent.Type.HoverEnter : "HoverEnter",
        QEvent.Type.HoverLeave : "HoverLeave",
        QEvent.Type.HoverMove : "HoverMove",
        QEvent.Type.GraphicsSceneMouseMove : "GraphicsSceneMouseMove",
        QEvent.Type.GraphicsSceneMousePress : "GraphicsSceneMousePress",
        QEvent.Type.GraphicsSceneMouseRelease : "GraphicsSceneMouseRelease",
        QEvent.Type.GraphicsSceneMouseDoubleClick : "GraphicsSceneMouseDoubleClick",
        QEvent.Type.GraphicsSceneContextMenu : "GraphicsSceneContextMenu",
        QEvent.Type.GraphicsSceneHoverEnter : "GraphicsSceneHoverEnter",
        QEvent.Type.GraphicsSceneHoverMove : "GraphicsSceneHoverMove",
        QEvent.Type.GraphicsSceneHoverLeave : "GraphicsSceneHoverLeave",
        QEvent.Type.GraphicsSceneHelp : "GraphicsSceneHelp",
        QEvent.Type.GraphicsSceneDragEnter : "GraphicsSceneDragEnter",
        QEvent.Type.GraphicsSceneDragMove : "GraphicsSceneDragMove",
        QEvent.Type.GraphicsSceneDragLeave : "GraphicsSceneDragLeave",
        QEvent.Type.GraphicsSceneDrop : "GraphicsSceneDrop",
        QEvent.Type.GraphicsSceneWheel : "GraphicsSceneWheel",
        QEvent.Type.GraphicsSceneResize : "GraphicsSceneResize",
        QEvent.Type.GraphicsSceneMove : "GraphicsSceneMove",
        QEvent.Type.KeyboardLayoutChange : "KeyboardLayoutChange",
        QEvent.Type.DynamicPropertyChange : "DynamicPropertyChange",
        QEvent.Type.TabletEnterProximity : "TabletEnterProximity",
        QEvent.Type.TabletLeaveProximity : "TabletLeaveProximity",
        QEvent.Type.NonClientAreaMouseMove : "NonClientAreaMouseMove",
        QEvent.Type.NonClientAreaMouseButtonPress : "NonClientAreaMouseButtonPress",
        QEvent.Type.NonClientAreaMouseButtonRelease : "NonClientAreaMouseButtonRelease",
        QEvent.Type.NonClientAreaMouseButtonDblClick : "NonClientAreaMouseButtonDblClick",
        QEvent.Type.MacSizeChange : "MacSizeChange",
        QEvent.Type.ContentsRectChange : "ContentsRectChange",
        QEvent.Type.CursorChange : "CursorChange",
        QEvent.Type.ToolTipChange : "ToolTipChange",
        QEvent.Type.GrabMouse : "GrabMouse",
        QEvent.Type.UngrabMouse : "UngrabMouse",
        QEvent.Type.GrabKeyboard : "GrabKeyboard",
        QEvent.Type.UngrabKeyboard : "UngrabKeyboard",
        QEvent.Type.StateMachineSignal : "StateMachineSignal",
        QEvent.Type.StateMachineWrapped : "StateMachineWrapped",
        QEvent.Type.TouchBegin : "TouchBegin",
        QEvent.Type.TouchUpdate : "TouchUpdate",
        QEvent.Type.TouchEnd : "TouchEnd",
        QEvent.Type.RequestSoftwareInputPanel : "RequestSoftwareInputPanel",
        QEvent.Type.CloseSoftwareInputPanel : "CloseSoftwareInputPanel",
        QEvent.Type.WinIdChange : "WinIdChange",
        QEvent.Type.Gesture : "Gesture",
        QEvent.Type.GestureOverride : "GestureOverride",
        QEvent.Type.FocusAboutToChange : "FocusAboutToChange",
        QEvent.Type.ScrollPrepare : "ScrollPrepare",
        QEvent.Type.Scroll : "Scroll",
        QEvent.Type.Expose : "Expose",
        QEvent.Type.InputMethodQuery : "InputMethodQuery",
        QEvent.Type.OrientationChange : "OrientationChange",
        QEvent.Type.TouchCancel : "TouchCancel",
        QEvent.Type.PlatformPanel : "PlatformPanel",
        QEvent.Type.ApplicationStateChange : "ApplicationStateChange",
        QEvent.Type.ReadOnlyChange : "ReadOnlyChange",
        QEvent.Type.PlatformSurface : "PlatformSurface",
        QEvent.Type.TabletTrackingChange : "TabletTrackingChange",
        QEvent.Type.User : "User",
        QEvent.Type.MaxUser : "MaxUser"}
        if obj is self.window():
            print(obj,mapping[e.type()])
            if e.type() == QEvent.Resize:
                re = QResizeEvent(e)
                self.resize(re.size())

        return super().eventFilter(obj, e)
class ModifiedMessageBoxBase(MaskBase):
    """ Message box base """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.buttonGroup = QFrame(self.widget)
        self.yesButton = PrimaryPushButton(self.tr('OK'), self.buttonGroup)
        self.cancelButton = PrimaryPushButton(self.tr('Cancel'), self.buttonGroup)

        self.vBoxLayout = QVBoxLayout(self.widget)
        self.widget.setLayout(self.vBoxLayout)
        self.buttonLayout = QHBoxLayout(self.buttonGroup)
        self.buttonGroup.setLayout(self.buttonLayout)
        self.__initWidget()
    def __initWidget(self):
        self.__setQss()
        self.__initLayout()

        self.setShadowEffect(60, (0, 10), QColor(0, 0, 0, 50))
        self.setMaskColor(QColor(0, 0, 0, 76))


        self.yesButton.setAttribute(Qt.WA_LayoutUsesWidgetRect)
        self.cancelButton.setAttribute(Qt.WA_LayoutUsesWidgetRect)

        self.yesButton.setFocus()
        self.buttonGroup.setFixedHeight(81)

    def __initLayout(self):
        self._hBoxLayout.removeWidget(self.widget)
        self._hBoxLayout.addWidget(self.widget, 0, Qt.AlignCenter)

        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.addWidget(self.buttonGroup, 0, Qt.AlignCenter)

        self.buttonLayout.setSpacing(12)
        self.buttonLayout.setContentsMargins(24, 24, 24, 24)
        self.buttonLayout.addWidget(self.yesButton, 1, Qt.AlignVCenter)
        self.buttonLayout.addWidget(self.cancelButton, 1, Qt.AlignVCenter)
    def __setQss(self):
        self.buttonGroup.setObjectName('buttonGroup')
        self.cancelButton.setObjectName('cancelButton')
        FluentStyleSheet.DIALOG.apply(self)
    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.windowMask.resize(self.parent().size())
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())
        print("parent size:",self.parent().size())
        print("self size:",self.size())
        self.widget.show()
        self.widget.activateWindow()
    def hideYesButton(self):
        if not self.yesButton.isHidden():
            self.yesButton.hide()
            self.buttonLayout.insertStretch(0, 1)
    def showYesButton(self):
        if self.yesButton.isHidden():
            self.yesButton.show()

            self.buttonLayout.removeItem(self.buttonLayout.itemAt(0))

    def showCancelButton(self):
        if self.cancelButton.isHidden():
            self.cancelButton.show()

            self.buttonLayout.removeItem(self.buttonLayout.itemAt(0))
    def hideCancelButton(self):
        if not self.cancelButton.isHidden():
            self.cancelButton.hide()
            self.buttonLayout.insertStretch(0, 1)
    def setParent(self, parent:QWidget, *args):
        super().setParent(parent, *args)
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())
from datetime import datetime,timedelta
from datetime import datetime, timedelta
import calendar

def getTime(timestamp):
    if timestamp:
        message_time = datetime.fromtimestamp(timestamp)
        current_time = datetime.now()

        if message_time.date() == current_time.date():
            return message_time.strftime("%H:%M")

        elif message_time.date() == current_time.date() - timedelta(days=1):
            return "yesterday"

        current_year, current_week, _ = current_time.isocalendar()
        message_year, message_week, _ = message_time.isocalendar()

        if message_year == current_year and message_week == current_week:
            return "week" + str(calendar.day_name[message_time.weekday()])

        elif message_year == current_year:
            return message_time.strftime("%m-%d")

        else:
            return message_time.strftime("%Y-%m-%d")

    return ""
class TimeHorizontalSeparator(QWidget):
    """ Horizontal separator """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedHeight(30)
        self.timestamp = None
    def setTimeStamp(self,timestamp):
        self.timestamp = int(timestamp)
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)

        if isDarkTheme():
            painter.setPen(QColor(255, 255, 255, 51))
        else:
            painter.setPen(QColor(0, 0, 0, 22))

        painter.drawLine(0, 15, self.width(), 15)
        painter.setPen(QColor(0, 0, 0, 50))
        painter.setFont(QFont('SimSun', 10))
        painter.setRenderHint(QPainter.Antialiasing)

        rectWindow = QRect(0, 0, self.width(), self.height())

        rect = painter.drawText(rectWindow, Qt.AlignCenter, getTime(self.timestamp))
        painter.fillRect(rect, self.palette().window())
        painter.drawText(rectWindow, Qt.AlignCenter, getTime(self.timestamp))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # from qfluentwidgets import ListWidget
    a = QWidget()
    b = TimeHorizontalSeparator(a)
    b.setTimeStamp(1000000)
    layout = QHBoxLayout(a)
    layout.addWidget(b)
    layout.addWidget(QPushButton("test"))
    a.show()
    # custom_list_widget = ListWidget()
    # def f(widget,self=custom_list_widget):
    #     # 创建一个新的 QListWidgetItem
    #     item = QListWidgetItem(self)
    #     # 设置小部件大小提示
    #     size = widget.sizeHint()
    #     item.setSizeHint(size)
    #     # 添加到列表中
    #     self.addItem(item)
    #     self.setItemWidget(item, widget)
    # custom_list_widget.addWidgetItem = f
    
    # # 添加一些自定义的小部件到列表中
    # for i in range(5):
    #     widget = ContactItemWidget()
    #     custom_list_widget.addWidgetItem(widget)
        
    # custom_list_widget.show()
    sys.exit(app.exec_())
