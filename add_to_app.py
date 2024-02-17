import sys
from PyQt5.QtCore import QUrl, Qt, QTimer, pyqtSignal, pyqtSlot, QThread, QThreadPool, QBasicTimer, QTimerEvent, QMessageLogContext, QtMsgType, QRect
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QDockWidget, QPlainTextEdit, QLCDNumber, QWidget, QVBoxLayout, QTextBrowser, QFileDialog, QTextEdit, QComboBox, QPushButton, QMessageBox, QFrame, QInputDialog, QLabel, QCheckBox, QScrollBar, QDialogButtonBox, QDialog, QGridLayout, QMenu, QAction, QTabBar
from PyQt5.QtWidgets import QMenuBar

import preditor


def existing_application():
    """Example of a pre-existing application you want to add PrEditor to."""
    main_gui = QMainWindow()
    main_gui.setWindowTitle('PrEditor Test Application')
    QMenuBar = QMenuBar(main_gui)
    main_gui.setMenuBar(QMenuBar)
    uiEdit = QTextEdit(main_gui)
    uiEdit.setPlaceholderText('Use menu to show PrEditor')
    main_gui.setCentralWidget(uiEdit)
    menu = QMenuBar.addMenu('File')
    act = menu.addAction('Exit')
    act.triggered.connect(main_gui.close)

    return main_gui


def raise_error():
    """Simulate a python exception being raised. You will be prompted to show
    PrEditor if its not currently visible. This can be disabled by setting
    `excepthook` to false when calling `preditor.configure`.
    """
    raise RuntimeError(
        "The user generated this error. If PrEditor is not already "
        "visible, the user is prompted to show it."
    )


if __name__ == '__main__':
    # Configure PrEditor for this application, start capturing all text output
    # from stderr/stdout so once PrEditor is launched, it can show this text.
    # This does not initialize any QtGui/QtWidgets.
    preditor.configure(
        # This is the name used to store PrEditor preferences and workboxes
        # specific to this application.
        'add_to_app',
    )
    import preditor.debug

    preditor.debug.BlurExcepthook.install()

    # Create a Gui Application allowing the user to show PrEditor
    app = QApplication(sys.argv)
    main_gui = existing_application()

    # Get the menu from the window instance. This method assumes you don't have
    # the ability to directly add the menu items when building the application.
    for act in main_gui.menuBar().actions():
        if act.text() == "File":
            menu = act.menu()
            break
    else:
        raise RuntimeError("Unable to find the File menu.")

    menu.addSeparator()
    # Add the PrEditor menu items to the pre-existing GUI.
    # If the user presses "F2" or uses the menu item, show the GUI
    act = preditor.connect_preditor(main_gui)
    menu.addAction(act)

    # Simulate something raising an error in the application
    act = menu.addAction('Raise Error')
    act.triggered.connect(raise_error)

    main_gui.show()
    app.exec_()
