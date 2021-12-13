# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_view_tw.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_view(object):
    def setupUi(self, main_view):
        main_view.setObjectName("main_view")
        main_view.resize(500, 641)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_view.sizePolicy().hasHeightForWidth())
        main_view.setSizePolicy(sizePolicy)
        main_view.setMinimumSize(QtCore.QSize(500, 641))
        main_view.setMaximumSize(QtCore.QSize(500, 641))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/noticias.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        main_view.setWindowIcon(icon)
        main_view.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(main_view)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 641))
        self.centralwidget.setMaximumSize(QtCore.QSize(500, 641))
        self.centralwidget.setObjectName("centralwidget")
        self.tool_frame = QtWidgets.QFrame(self.centralwidget)
        self.tool_frame.setGeometry(QtCore.QRect(10, 0, 481, 61))
        self.tool_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tool_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tool_frame.setObjectName("tool_frame")
        self.btn_base = QtWidgets.QToolButton(self.tool_frame)
        self.btn_base.setEnabled(True)
        self.btn_base.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.btn_base.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagenes/iconDb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_base.setIcon(icon1)
        self.btn_base.setIconSize(QtCore.QSize(32, 32))
        self.btn_base.setAutoRaise(False)
        self.btn_base.setObjectName("btn_base")
        self.btn_tabla = QtWidgets.QToolButton(self.tool_frame)
        self.btn_tabla.setGeometry(QtCore.QRect(70, 10, 51, 41))
        self.btn_tabla.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../imagenes/iconTable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_tabla.setIcon(icon2)
        self.btn_tabla.setIconSize(QtCore.QSize(32, 32))
        self.btn_tabla.setAutoRaise(False)
        self.btn_tabla.setObjectName("btn_tabla")
        self.btn_nuevo = QtWidgets.QToolButton(self.tool_frame)
        self.btn_nuevo.setGeometry(QtCore.QRect(130, 10, 51, 41))
        self.btn_nuevo.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../imagenes/iconNew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_nuevo.setIcon(icon3)
        self.btn_nuevo.setIconSize(QtCore.QSize(32, 32))
        self.btn_nuevo.setAutoRaise(False)
        self.btn_nuevo.setObjectName("btn_nuevo")
        self.btn_guardar = QtWidgets.QToolButton(self.tool_frame)
        self.btn_guardar.setGeometry(QtCore.QRect(190, 10, 51, 41))
        self.btn_guardar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../imagenes/iconSave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_guardar.setIcon(icon4)
        self.btn_guardar.setIconSize(QtCore.QSize(32, 32))
        self.btn_guardar.setAutoRaise(False)
        self.btn_guardar.setObjectName("btn_guardar")
        self.btn_eliminar = QtWidgets.QToolButton(self.tool_frame)
        self.btn_eliminar.setGeometry(QtCore.QRect(250, 10, 51, 41))
        self.btn_eliminar.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../imagenes/iconDelete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_eliminar.setIcon(icon5)
        self.btn_eliminar.setIconSize(QtCore.QSize(32, 32))
        self.btn_eliminar.setAutoRaise(False)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.btn_refresh = QtWidgets.QToolButton(self.tool_frame)
        self.btn_refresh.setGeometry(QtCore.QRect(310, 10, 51, 41))
        self.btn_refresh.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../imagenes/iconRefresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_refresh.setIcon(icon6)
        self.btn_refresh.setIconSize(QtCore.QSize(32, 32))
        self.btn_refresh.setAutoRaise(False)
        self.btn_refresh.setObjectName("btn_refresh")
        self.txt_id_search = QtWidgets.QLineEdit(self.tool_frame)
        self.txt_id_search.setGeometry(QtCore.QRect(370, 20, 41, 21))
        self.txt_id_search.setText("")
        self.txt_id_search.setMaxLength(6)
        self.txt_id_search.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_id_search.setObjectName("txt_id_search")
        self.btn_search = QtWidgets.QToolButton(self.tool_frame)
        self.btn_search.setGeometry(QtCore.QRect(420, 10, 51, 41))
        self.btn_search.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../imagenes/iconSearch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon7)
        self.btn_search.setIconSize(QtCore.QSize(32, 32))
        self.btn_search.setAutoRaise(False)
        self.btn_search.setObjectName("btn_search")
        self.data_frame = QtWidgets.QFrame(self.centralwidget)
        self.data_frame.setGeometry(QtCore.QRect(10, 60, 481, 351))
        self.data_frame.setStyleSheet("border-color: rgb(0, 0, 255);\n"
"border-width: thin;")
        self.data_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.data_frame.setLineWidth(2)
        self.data_frame.setObjectName("data_frame")
        self.lbl_fecha = QtWidgets.QLabel(self.data_frame)
        self.lbl_fecha.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.lbl_fecha.setObjectName("lbl_fecha")
        self.de_fecha = QtWidgets.QDateEdit(self.data_frame)
        self.de_fecha.setGeometry(QtCore.QRect(90, 10, 91, 22))
        self.de_fecha.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.de_fecha.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.de_fecha.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.de_fecha.setCalendarPopup(True)
        self.de_fecha.setObjectName("de_fecha")
        self.lbl_medio = QtWidgets.QLabel(self.data_frame)
        self.lbl_medio.setGeometry(QtCore.QRect(10, 40, 61, 21))
        self.lbl_medio.setObjectName("lbl_medio")
        self.cmb_medios = QtWidgets.QComboBox(self.data_frame)
        self.cmb_medios.setGeometry(QtCore.QRect(90, 40, 231, 22))
        self.cmb_medios.setObjectName("cmb_medios")
        self.lbl_seccion = QtWidgets.QLabel(self.data_frame)
        self.lbl_seccion.setGeometry(QtCore.QRect(10, 70, 61, 21))
        self.lbl_seccion.setObjectName("lbl_seccion")
        self.cmb_secciones = QtWidgets.QComboBox(self.data_frame)
        self.cmb_secciones.setGeometry(QtCore.QRect(90, 70, 231, 22))
        self.cmb_secciones.setObjectName("cmb_secciones")
        self.lbl_titulo = QtWidgets.QLabel(self.data_frame)
        self.lbl_titulo.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.lineEdit = QtWidgets.QLineEdit(self.data_frame)
        self.lineEdit.setGeometry(QtCore.QRect(90, 100, 381, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lbl_cuerpo = QtWidgets.QLabel(self.data_frame)
        self.lbl_cuerpo.setGeometry(QtCore.QRect(10, 130, 61, 21))
        self.lbl_cuerpo.setObjectName("lbl_cuerpo")
        self.txt_cuerpo = QtWidgets.QTextEdit(self.data_frame)
        self.txt_cuerpo.setGeometry(QtCore.QRect(90, 130, 381, 211))
        self.txt_cuerpo.setObjectName("txt_cuerpo")
        self.tw_noticias = QtWidgets.QTableWidget(self.centralwidget)
        self.tw_noticias.setGeometry(QtCore.QRect(10, 420, 481, 192))
        self.tw_noticias.setObjectName("tw_noticias")
        self.tw_noticias.setColumnCount(6)
        self.tw_noticias.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_noticias.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_noticias.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_noticias.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_noticias.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_noticias.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_noticias.setHorizontalHeaderItem(5, item)
        main_view.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_view)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        main_view.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_view)
        self.statusbar.setObjectName("statusbar")
        main_view.setStatusBar(self.statusbar)
        self.actionAcerca_de = QtWidgets.QAction(main_view)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.menuArchivo.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(main_view)
        QtCore.QMetaObject.connectSlotsByName(main_view)

    def retranslateUi(self, main_view):
        _translate = QtCore.QCoreApplication.translate
        main_view.setWindowTitle(_translate("main_view", "Cargador de Noticias"))
        self.btn_base.setToolTip(_translate("main_view", "Crear base de datos."))
        self.btn_tabla.setToolTip(_translate("main_view", "Crear tabla Noticias."))
        self.btn_nuevo.setToolTip(_translate("main_view", "Noticia nueva."))
        self.btn_guardar.setToolTip(_translate("main_view", "Guardar noticia."))
        self.btn_eliminar.setToolTip(_translate("main_view", "Eliminar noticia."))
        self.btn_refresh.setToolTip(_translate("main_view", "Cargar la grilla."))
        self.txt_id_search.setToolTip(_translate("main_view", "ingrese un id de noticia a buscar..."))
        self.txt_id_search.setInputMask(_translate("main_view", "999999"))
        self.btn_search.setToolTip(_translate("main_view", "Buscar noticia según id."))
        self.lbl_fecha.setText(_translate("main_view", "Fecha"))
        self.de_fecha.setDisplayFormat(_translate("main_view", "dd/MM/yyyy"))
        self.lbl_medio.setText(_translate("main_view", "Medio"))
        self.lbl_seccion.setText(_translate("main_view", "Sección"))
        self.lbl_titulo.setText(_translate("main_view", "Título"))
        self.lbl_cuerpo.setText(_translate("main_view", "Cuerpo"))
        item = self.tw_noticias.horizontalHeaderItem(0)
        item.setText(_translate("main_view", "Id"))
        item = self.tw_noticias.horizontalHeaderItem(1)
        item.setText(_translate("main_view", "Fecha"))
        item = self.tw_noticias.horizontalHeaderItem(2)
        item.setText(_translate("main_view", "Medio"))
        item = self.tw_noticias.horizontalHeaderItem(3)
        item.setText(_translate("main_view", "Seccion"))
        item = self.tw_noticias.horizontalHeaderItem(4)
        item.setText(_translate("main_view", "Título"))
        item = self.tw_noticias.horizontalHeaderItem(5)
        item.setText(_translate("main_view", "Cuerpo"))
        self.menuArchivo.setTitle(_translate("main_view", "Archivo"))
        self.actionAcerca_de.setText(_translate("main_view", "Acerca de..."))
