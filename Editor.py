# -*- coding: utf-8 -*-
# @Author: YokDen
# @Time: 2022/10/1
# @Email: dyk_693@qq.com

import os
import sys

import chardet
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QTextCursor, QPalette
from PyQt5.QtWidgets import QMdiSubWindow, QTextEdit, QFileDialog, QMainWindow, QWidget, QFontDialog, QColorDialog, \
    QMessageBox


class Ui_Editor(QWidget):
    def __init__(self):
        super(Ui_Editor, self).__init__()
        self.search_box = Ui_SearchBox()
        self.search_box.setWindowModality(Qt.ApplicationModal)
        self.search_box.setupUi(self.search_box)

    def setupUi(self, Editor):
        Editor.setObjectName("Editor")
        Editor.resize(1600, 1400)
        Editor.setWindowIcon(QIcon("images/note.png"))
        self.centralwidget = QtWidgets.QWidget(Editor)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        self.verticalLayout.addWidget(self.mdiArea)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        Editor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Editor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        Editor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Editor)
        self.statusbar.setObjectName("statusbar")
        Editor.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Editor)
        self.toolBar.setObjectName("toolBar")
        Editor.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_new = QtWidgets.QAction(Editor)
        self.action_new.setObjectName("action_new")
        self.action_open = QtWidgets.QAction(Editor)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(Editor)
        self.action_save.setObjectName("action_save")
        self.action_saveas = QtWidgets.QAction(Editor)
        self.action_saveas.setObjectName("action_saveas")
        self.action_close = QtWidgets.QAction(Editor)
        self.action_close.setObjectName("action_close")
        self.action_about = QtWidgets.QAction(Editor)
        self.action_about.setObjectName("action_about")
        self.actioncascade = QtWidgets.QAction(Editor)
        self.actioncascade.setObjectName("actionpile")
        self.actiontile = QtWidgets.QAction(Editor)
        self.actiontile.setObjectName("actionverti")
        self.actioncut = QtWidgets.QAction(Editor)
        self.actioncut.setObjectName("actioncut")
        self.actioncopy = QtWidgets.QAction(Editor)
        self.actioncopy.setObjectName("actioncopy")
        self.actionpaste = QtWidgets.QAction(Editor)
        self.actionpaste.setObjectName("actionpaste")
        self.actionfont = QtWidgets.QAction(Editor)
        self.actionfont.setObjectName("actionfont")
        self.actioncolor = QtWidgets.QAction(Editor)
        self.actioncolor.setObjectName("actioncolor")
        self.actionsearch = QtWidgets.QAction(Editor)
        self.actionsearch.setObjectName("actionsearch")
        self.aleft = QtWidgets.QAction(Editor)
        self.aleft.setObjectName("aleft")
        self.amid = QtWidgets.QAction(Editor)
        self.amid.setObjectName("amid")
        self.aright = QtWidgets.QAction(Editor)
        self.aright.setObjectName("aright")
        self.undo = QtWidgets.QAction(Editor)
        self.undo.setObjectName("undo")
        self.redo = QtWidgets.QAction(Editor)
        self.redo.setObjectName("redo")
        self.menu.addAction(self.action_new)
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_saveas)
        self.menu.addSeparator()
        self.menu.addAction(self.action_close)
        self.menu_2.addAction(self.actioncut)
        self.menu_2.addAction(self.actioncopy)
        self.menu_2.addAction(self.actionpaste)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionfont)
        self.menu_2.addAction(self.actioncolor)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.undo)
        self.menu_2.addAction(self.redo)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionsearch)
        self.menu_3.addAction(self.actioncascade)
        self.menu_3.addAction(self.actiontile)
        self.menu_4.addAction(self.action_about)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)

        self.action_init()
        self.toolbar_init()
        self.connector()

    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        Editor.setWindowTitle(_translate("Editor", "TextEditor"))
        self.menu.setTitle(_translate("Editor", "??????"))
        self.menu_2.setTitle(_translate("Editor", "??????"))
        self.menu_3.setTitle(_translate("Editor", "??????"))
        self.menu_4.setTitle(_translate("Editor", "??????"))
        self.toolBar.setWindowTitle(_translate("Editor", "toolBar"))
        self.action_new.setText(_translate("Editor", "??????"))
        self.action_open.setText(_translate("Editor", "??????"))
        self.action_save.setText(_translate("Editor", "??????"))
        self.action_saveas.setText(_translate("Editor", "?????????..."))
        self.action_close.setText(_translate("Editor", "??????"))
        self.action_about.setText(_translate("Editor", "??????"))
        self.actioncascade.setText(_translate("Editor", "????????????"))
        self.actiontile.setText(_translate("Editor", "????????????"))
        self.actioncut.setText(_translate("Editor", "??????"))
        self.actioncopy.setText(_translate("Editor", "??????"))
        self.actionpaste.setText(_translate("Editor", "??????"))
        self.actionfont.setText(_translate("Editor", "??????"))
        self.actioncolor.setText(_translate("Editor", "??????"))
        self.actionsearch.setText(_translate("Editor", "????????????"))
        self.aleft.setText(_translate("Editor", "?????????"))
        self.amid.setText(_translate("Editor", "????????????"))
        self.aright.setText(_translate("Editor", "?????????"))
        self.undo.setText(_translate("Editor", "??????"))
        self.redo.setText(_translate("Editor", "??????"))

    # ??????????????????
    def action_init(self):
        self.action_new.setIcon(QIcon('images/new.png'))
        self.action_new.setShortcut('Ctrl+N')
        self.action_new.setToolTip('??????')
        self.action_new.setStatusTip('????????????')

        self.action_open.setIcon(QIcon('images/open.png'))
        self.action_open.setShortcut('Ctrl+O')
        self.action_open.setToolTip('??????')
        self.action_open.setStatusTip('????????????')

        self.action_save.setIcon(QIcon('images/save.png'))
        self.action_save.setShortcut('Ctrl+S')
        self.action_save.setToolTip('??????')
        self.action_save.setStatusTip('????????????')

        self.action_saveas.setIcon(QIcon('images/saveas.png'))
        self.action_saveas.setStatusTip('????????????')

        self.action_close.setIcon(QIcon('images/close.png'))

        self.actioncut.setIcon(QIcon('images/cut.png'))
        self.actioncut.setShortcut('Ctrl+X')
        self.actioncut.setToolTip('??????')
        self.actioncut.setStatusTip('??????????????????')

        self.actioncopy.setIcon(QIcon('images/copy.png'))
        self.actioncopy.setShortcut('Ctrl+C')
        self.actioncopy.setToolTip('??????')
        self.actioncopy.setStatusTip('??????????????????')

        self.actionpaste.setIcon(QIcon('images/paste.png'))
        self.actionpaste.setShortcut('Ctrl+V')
        self.actionpaste.setToolTip('??????')
        self.actionpaste.setStatusTip('????????????')

        self.actioncascade.setIcon(QIcon('images/cascade.png'))
        self.actioncascade.setStatusTip('????????????')

        self.actiontile.setIcon(QIcon('images/tile.png'))
        self.actiontile.setStatusTip('????????????')

        self.undo.setIcon(QIcon('images/undo.png'))
        self.undo.setShortcut('Ctrl+Z')
        self.undo.setToolTip('??????')
        self.undo.setStatusTip('??????')

        self.redo.setIcon(QIcon('images/redo.png'))
        self.redo.setShortcut('Ctrl+Y')
        self.redo.setToolTip('??????')
        self.redo.setStatusTip('????????????')

        self.aleft.setIcon(QIcon('images/left.png'))
        self.aleft.setToolTip('?????????')
        self.aleft.setStatusTip('?????????')
        self.aright.setIcon(QIcon('images/right.png'))
        self.aright.setToolTip('?????????')
        self.aright.setStatusTip('?????????')
        self.amid.setIcon(QIcon('images/center.png'))
        self.amid.setToolTip('????????????')
        self.amid.setStatusTip('????????????')

        self.actioncolor.setIcon(QIcon('images/color.png'))
        self.actioncolor.setToolTip('??????')
        self.actioncolor.setStatusTip('????????????')

        self.actionfont.setIcon(QIcon('images/font.png'))
        self.actionfont.setToolTip('??????')
        self.actionfont.setStatusTip('????????????')

        self.actionsearch.setIcon(QIcon('images/search.png'))
        self.actionsearch.setToolTip('????????????')
        self.actionsearch.setStatusTip('????????????')

        self.action_about.setIcon(QIcon('images/about.png'))
        self.action_about.setStatusTip('??????')

    # ??????????????????
    def toolbar_init(self):
        self.toolBar.addActions([self.action_new, self.action_open, self.action_save])
        self.toolBar.addActions([self.actionfont, self.actioncolor])
        self.toolBar.addActions([self.undo, self.redo])
        self.toolBar.addActions([self.aleft, self.amid, self.aright])
        self.toolBar.addActions([self.actioncut, self.actioncopy, self.actionpaste])
        self.toolBar.addActions([self.actionsearch])

    def connector(self):
        self.action_close.triggered.connect(sub.close)
        self.action_new.triggered.connect(self.new_fun)
        self.action_open.triggered.connect(self.open_fun)
        self.action_save.triggered.connect(self.save_fun)
        self.action_saveas.triggered.connect(self.saveas_fun)
        self.actioncut.triggered.connect(
            lambda: self.mdiArea.activeSubWindow().widget().cut() if self.mdiArea.subWindowList() else None)
        self.actioncopy.triggered.connect(
            lambda: self.mdiArea.activeSubWindow().widget().copy() if self.mdiArea.subWindowList() else None)
        self.actionpaste.triggered.connect(
            lambda: self.mdiArea.activeSubWindow().widget().paste() if self.mdiArea.subWindowList() else None)
        self.actioncascade.triggered.connect(self.mdiArea.cascadeSubWindows)
        self.actiontile.triggered.connect(self.mdiArea.tileSubWindows)
        self.undo.triggered.connect(
            lambda: self.mdiArea.activeSubWindow().widget().undo() if self.mdiArea.subWindowList() else None)
        self.redo.triggered.connect(
            lambda: self.mdiArea.activeSubWindow().widget().redo() if self.mdiArea.subWindowList() else None)
        self.aleft.triggered.connect(lambda: self.mdiArea.activeSubWindow().widget().setAlignment(
            Qt.AlignLeft) if self.mdiArea.subWindowList() else None)
        self.aright.triggered.connect(lambda: self.mdiArea.activeSubWindow().widget().setAlignment(
            Qt.AlignRight) if self.mdiArea.subWindowList() else None)
        self.amid.triggered.connect(lambda: self.mdiArea.activeSubWindow().widget().setAlignment(
            Qt.AlignCenter) if self.mdiArea.subWindowList() else None)
        self.actionfont.triggered.connect(self.set_font)
        self.actioncolor.triggered.connect(self.set_color)
        self.action_about.triggered.connect(self.about)
        self.actionsearch.triggered.connect(self.show_search_box)

        self.search_box.pub_search.clicked.connect(self.search)
        self.search_box.pub_replace.clicked.connect(self.replace)
        self.search_box.pub_replace_all.clicked.connect(self.replace_all)
        self.search_box.lineEdit_sec.textChanged.connect(
            lambda: self.mdiArea.activeSubWindow().widget().moveCursor(QTextCursor.Start))

    # ????????????
    def new_fun(self):
        try:
            newDoc = MdiTextEdit()
            newDoc.setWindowTitle('Untitled-' + str(MdiTextEdit.newDocIndex))
            MdiTextEdit.newDocIndex += 1
            self.mdiArea.addSubWindow(newDoc)
            newDoc.show()
        except Exception as e:
            print(e)

    # ????????????
    def open_fun(self):
        path, filetype = QFileDialog.getOpenFileName(self, "????????????", "./",
                                                     "????????? (*.txt);;?????? (*.htm; *.html)")
        if path:
            filename = os.path.basename(path)
            try:
                def get_encoding(file):  # ????????????????????????
                    with open(file, 'rb') as f:
                        tmp = chardet.detect(f.read())
                        return tmp['encoding']

                with open(path, 'r', encoding=get_encoding(path)) as f:
                    content = f.read()
            except Exception as e:
                print(e)
            else:
                openDoc = MdiTextEdit()
                openDoc.path = path
                openDoc.setWindowTitle(filename)
                if "(*.txt)" in filetype:
                    openDoc.textedit.setPlainText(content)
                elif "(*.htm; *.html)" in filetype:
                    openDoc.textedit.setHtml(content)
                openDoc.textedit.document().setModified(False)
                self.mdiArea.addSubWindow(openDoc)
                openDoc.show()

    # ????????????
    def save_fun(self):
        if self.mdiArea.subWindowList():
            activeWindow = self.mdiArea.activeSubWindow()
            if not activeWindow.path:
                return self.saveas_fun()
            else:
                with open(activeWindow.path, 'w', encoding='utf-8') as f:
                    if activeWindow.path.endswith(".txt"):
                        f.write(activeWindow.widget().toPlainText())
                    elif activeWindow.path.endswith(".htm") or activeWindow.path.endswith(".html"):
                        f.write(activeWindow.widget().toHtml())
                activeWindow.textedit.document().setModified(False)
                return True
        return False

    # ???????????????
    def saveas_fun(self):
        if self.mdiArea.subWindowList():
            activeWindow = self.mdiArea.activeSubWindow()
            filename = activeWindow.windowTitle()
            path, filetype = QFileDialog.getSaveFileName(self, "????????????", "./" + filename,
                                                         "????????? (*.txt);;?????? (*.html; *.htm)")
            if path:
                with open(path, 'w', encoding='utf-8') as f:
                    if "(*.txt)" in filetype:
                        f.write(activeWindow.widget().toPlainText())
                    elif "(*.html; *.htm)" in filetype:
                        f.write(activeWindow.widget().toHtml())
                activeWindow.setWindowTitle(os.path.basename(path))
                activeWindow.path = path
                activeWindow.textedit.document().setModified(False)
                return True
        return False

    # ????????????
    def set_font(self):
        if self.mdiArea.subWindowList():
            font, ok = QFontDialog.getFont()
            if ok:
                self.mdiArea.activeSubWindow().widget().setCurrentFont(font)

    # ????????????
    def set_color(self):
        if self.mdiArea.subWindowList():
            color = QColorDialog.getColor()
            if color.isValid():
                self.mdiArea.activeSubWindow().widget().setTextColor(color)

    # ??????
    def about(self):
        self.setWindowIcon(QIcon("images/about.png"))
        QMessageBox.about(self, "??????", "It is a simple Multi-Editor designed by YokDen")

    def show_search_box(self):
        if self.mdiArea.subWindowList():
            self.search_box.show()
            self.mdiArea.activeSubWindow().widget().moveCursor(QTextCursor.Start)

    def search(self):
        textedit = self.mdiArea.activeSubWindow().widget()
        search_text = self.search_box.lineEdit_sec.text()
        if search_text:
            if textedit.find(search_text):
                pass
            else:
                self.setWindowIcon(QIcon("images/search.png"))
                dlg = QMessageBox.question(self, "??????", "?????????????????????????????????????????????",
                                           QMessageBox.Ok | QMessageBox.No)
                if dlg == QMessageBox.Ok:
                    textedit.moveCursor(QTextCursor.Start)

    def replace(self):
        textedit = self.mdiArea.activeSubWindow().widget()
        replace_text = self.search_box.lineEdit_rep.text()
        search_text = self.search_box.lineEdit_sec.text()
        if textedit.textCursor().selectedText() or textedit.find(search_text):
            textedit.textCursor().insertText(replace_text)
        else:
            self.setWindowIcon(QIcon("images/search.png"))
            dlg = QMessageBox.question(self, "??????", "?????????????????????????????????????????????",
                                       QMessageBox.Ok | QMessageBox.No)
            if dlg == QMessageBox.Ok:
                textedit.moveCursor(QTextCursor.Start)

    def replace_all(self):
        textedit = self.mdiArea.activeSubWindow().widget()
        replace_text = self.search_box.lineEdit_rep.text()
        search_text = self.search_box.lineEdit_sec.text()
        if search_text:
            textedit.moveCursor(QTextCursor.Start)
            cnt = 0
            while textedit.find(search_text):
                textedit.textCursor().insertText(replace_text)
                cnt += 1
            self.setWindowIcon(QIcon("images/search.png"))
            if cnt == 0:
                QMessageBox.information(self, "??????", "?????????????????????")
            else:
                QMessageBox.information(self, "??????", f"???????????????????????????{cnt}?????????")


# ?????????
class MdiTextEdit(QMdiSubWindow):
    newDocIndex = 1  # ???????????????????????????

    def __init__(self):
        super(MdiTextEdit, self).__init__()
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setWindowIcon(QIcon("images/note.png"))
        self.resize(782, 720)
        self.path = ''
        self.textedit = QTextEdit(self)
        self.textedit.document().setModified(False)  # ?????????????????????
        self.setWidget(self.textedit)
        palette = self.textedit.palette()
        palette.setColor(QPalette.Highlight, palette.color(QPalette.Active, QPalette.Highlight))
        self.textedit.setPalette(palette)

    def closeEvent(self, closeEvent: QtGui.QCloseEvent) -> None:  # ????????????closeEvent??????????????????
        if self.textedit.document().isModified():
            dlg = QMessageBox.question(self, "TextEdit", f"??????????????????{self.windowTitle()}?????????????",
                                       QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if dlg == QMessageBox.Yes:
                if not ui.save_fun():
                    closeEvent.ignore()
            elif dlg == QMessageBox.Cancel:
                closeEvent.ignore()


class Editor(QMainWindow, QWidget):  # ????????????closeEvent??????????????????
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        unsaved_file = 0
        for window in ui.mdiArea.subWindowList():
            if window.textedit.document().isModified():
                unsaved_file += 1
        if unsaved_file:
            ui.setWindowIcon(QIcon("images/note.png"))
            dlg = QMessageBox.warning(ui, "TextEdit", f"??????{unsaved_file}??????????????????,?????????????",
                                      QMessageBox.Yes | QMessageBox.No)
            if dlg == QMessageBox.No:
                a0.ignore()


class Ui_SearchBox(QMainWindow):
    def setupUi(self, SearchBox):
        SearchBox.setObjectName("SearchBox")
        SearchBox.resize(367, 142)
        SearchBox.setWindowIcon(QIcon("images/search.png"))
        self.centralwidget = QtWidgets.QWidget(SearchBox)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lbl_search = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_search.sizePolicy().hasHeightForWidth())
        self.lbl_search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbl_search.setFont(font)
        self.lbl_search.setObjectName("lbl_search")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_search)
        self.lbl_replace = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_replace.sizePolicy().hasHeightForWidth())
        self.lbl_replace.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbl_replace.setFont(font)
        self.lbl_replace.setObjectName("lbl_replace")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_replace)
        self.lineEdit_sec = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_sec.setFont(font)
        self.lineEdit_sec.setObjectName("lineEdit_sec")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_sec)
        self.lineEdit_rep = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_rep.setFont(font)
        self.lineEdit_rep.setObjectName("lineEdit_rep")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_rep)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 11, -1, -1)
        self.horizontalLayout.setSpacing(38)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pub_search = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pub_search.setFont(font)
        self.pub_search.setObjectName("pub_search")
        self.horizontalLayout.addWidget(self.pub_search)
        self.pub_replace = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pub_replace.setFont(font)
        self.pub_replace.setObjectName("pub_replace")
        self.horizontalLayout.addWidget(self.pub_replace)
        self.pub_replace_all = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pub_replace_all.setFont(font)
        self.pub_replace_all.setObjectName("pub_replace_all")
        self.horizontalLayout.addWidget(self.pub_replace_all)
        self.verticalLayout.addLayout(self.horizontalLayout)
        SearchBox.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchBox)
        QtCore.QMetaObject.connectSlotsByName(SearchBox)

    def retranslateUi(self, SearchBox):
        _translate = QtCore.QCoreApplication.translate
        SearchBox.setWindowTitle(_translate("SearchBox", "????????????"))
        self.lbl_search.setText(_translate("SearchBox", "???????????????"))
        self.lbl_replace.setText(_translate("SearchBox", "????????????"))
        self.pub_search.setText(_translate("SearchBox", "??????"))
        self.pub_replace.setText(_translate("SearchBox", "??????"))
        self.pub_replace_all.setText(_translate("SearchBox", "????????????"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sub = Editor()
    ui = Ui_Editor()
    ui.setupUi(sub)
    sub.show()
    sys.exit(app.exec_())
