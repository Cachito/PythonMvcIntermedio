# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from modulos.clases import *
from modulos.model import Model
from modulos.controller import Controller
import modulos.constant as constants
class Ui_main_view(object):
    """
    main y vista principal
    """
    def setupUi(self, main_view):
        self.nota_id = 0

        main_view.setObjectName("main_view")
        main_view.resize(500, 641)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_view.sizePolicy().hasHeightForWidth())
        main_view.setSizePolicy(sizePolicy)
        main_view.setMinimumSize(QtCore.QSize(500, 641))
        main_view.setMaximumSize(QtCore.QSize(500, 641))
        icon_form = QtGui.QIcon()
        icon_form.addPixmap(QtGui.QPixmap("./imagenes/noticias.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        main_view.setWindowIcon(icon_form)
        main_view.setToolTip("")
        # widgwt central
        self.centralwidget = QtWidgets.QWidget(main_view)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 641))
        self.centralwidget.setMaximumSize(QtCore.QSize(500, 641))
        self.centralwidget.setObjectName("centralwidget")
        # frame para barra de herramientas
        self.tool_frame = QtWidgets.QFrame(self.centralwidget)
        self.tool_frame.setGeometry(QtCore.QRect(10, 0, 481, 61))
        self.tool_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tool_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tool_frame.setObjectName("tool_frame")
        self.btn_base = QtWidgets.QToolButton(self.tool_frame)
        # botón base de datos
        self.btn_base.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.btn_base.setText("")
        icon_db = QtGui.QIcon()
        icon_db.addPixmap(QtGui.QPixmap("./imagenes/iconDb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_base.setIcon(icon_db)
        self.btn_base.setIconSize(QtCore.QSize(32, 32))
        self.btn_base.setAutoRaise(False)
        self.btn_base.setObjectName("btn_base")
        self.btn_base.clicked.connect(self.create_db)
        # botón tablas
        self.btn_tabla = QtWidgets.QToolButton(self.tool_frame)
        self.btn_tabla.setGeometry(QtCore.QRect(70, 10, 51, 41))
        self.btn_tabla.setText("")
        icon_tabla = QtGui.QIcon()
        icon_tabla.addPixmap(QtGui.QPixmap("./imagenes/iconTable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_tabla.setIcon(icon_tabla)
        self.btn_tabla.setIconSize(QtCore.QSize(32, 32))
        self.btn_tabla.setAutoRaise(False)
        self.btn_tabla.setObjectName("btn_tabla")
        self.btn_tabla.clicked.connect(self.create_tables)
        # botón noticia nueva
        self.btn_nuevo = QtWidgets.QToolButton(self.tool_frame)
        self.btn_nuevo.setGeometry(QtCore.QRect(130, 10, 51, 41))
        self.btn_nuevo.setText("")
        icon_nuevo = QtGui.QIcon()
        icon_nuevo.addPixmap(QtGui.QPixmap("./imagenes/iconNew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_nuevo.setIcon(icon_nuevo)
        self.btn_nuevo.setIconSize(QtCore.QSize(32, 32))
        self.btn_nuevo.setAutoRaise(False)
        self.btn_nuevo.setObjectName("btn_nuevo")
        self.btn_nuevo.clicked.connect(self.clear_data)
        # botón guardar noticia
        self.btn_guardar = QtWidgets.QToolButton(self.tool_frame)
        self.btn_guardar.setGeometry(QtCore.QRect(190, 10, 51, 41))
        self.btn_guardar.setText("")
        icon_save = QtGui.QIcon()
        icon_save.addPixmap(QtGui.QPixmap("./imagenes/iconSave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_guardar.setIcon(icon_save)
        self.btn_guardar.setIconSize(QtCore.QSize(32, 32))
        self.btn_guardar.setAutoRaise(False)
        self.btn_guardar.setObjectName("btn_guardar")
        self.btn_guardar.clicked.connect(self.save_data)
        # botón eliminar noticia
        self.btn_eliminar = QtWidgets.QToolButton(self.tool_frame)
        self.btn_eliminar.setGeometry(QtCore.QRect(250, 10, 51, 41))
        self.btn_eliminar.setText("")
        icon_delete = QtGui.QIcon()
        icon_delete.addPixmap(QtGui.QPixmap("./imagenes/iconDelete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_eliminar.setIcon(icon_delete)
        self.btn_eliminar.setIconSize(QtCore.QSize(32, 32))
        self.btn_eliminar.setAutoRaise(False)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.btn_eliminar.clicked.connect(self.delete_data)
        # botón refresh
        self.btn_refresh = QtWidgets.QToolButton(self.tool_frame)
        self.btn_refresh.setGeometry(QtCore.QRect(310, 10, 51, 41))
        self.btn_refresh.setText("")
        icon_refresh = QtGui.QIcon()
        icon_refresh.addPixmap(QtGui.QPixmap("./imagenes/iconRefresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_refresh.setIcon(icon_refresh)
        self.btn_refresh.setIconSize(QtCore.QSize(32, 32))
        self.btn_refresh.setAutoRaise(False)
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.clicked.connect(self.refresh)
        # id a buscar
        self.txt_id_search = QtWidgets.QLineEdit(self.tool_frame)
        self.txt_id_search.setGeometry(QtCore.QRect(370, 20, 41, 21))
        self.txt_id_search.setText("")
        self.txt_id_search.setMaxLength(6)
        self.txt_id_search.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_id_search.setObjectName("txt_id_search")
        # botón buscar
        self.btn_search = QtWidgets.QToolButton(self.tool_frame)
        self.btn_search.setGeometry(QtCore.QRect(420, 10, 51, 41))
        self.btn_search.setText("")
        icon_search = QtGui.QIcon()
        icon_search.addPixmap(QtGui.QPixmap("./imagenes/iconSearch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon_search)
        self.btn_search.setIconSize(QtCore.QSize(32, 32))
        self.btn_search.setAutoRaise(False)
        self.btn_search.setObjectName("btn_search")
        self.btn_search.clicked.connect(self.buscar)
        #frame datos
        self.data_frame = QtWidgets.QFrame(self.centralwidget)
        self.data_frame.setGeometry(QtCore.QRect(10, 60, 481, 351))
        self.data_frame.setStyleSheet("border-color: rgb(0, 0, 255);\n" "border-width: thin;")
        self.data_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.data_frame.setLineWidth(2)
        self.data_frame.setObjectName("data_frame")
        # fecha
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
        # medio
        self.lbl_medio = QtWidgets.QLabel(self.data_frame)
        self.lbl_medio.setGeometry(QtCore.QRect(10, 40, 61, 21))
        self.lbl_medio.setObjectName("lbl_medio")
        self.cmb_medios = QtWidgets.QComboBox(self.data_frame)
        self.cmb_medios.setGeometry(QtCore.QRect(90, 40, 231, 22))
        self.cmb_medios.setObjectName("cmb_medios")
        self.cmb_medios.currentIndexChanged.connect(self.load_secciones)
        # sección
        self.lbl_seccion = QtWidgets.QLabel(self.data_frame)
        self.lbl_seccion.setGeometry(QtCore.QRect(10, 70, 61, 21))
        self.lbl_seccion.setObjectName("lbl_seccion")
        self.cmb_secciones = QtWidgets.QComboBox(self.data_frame)
        self.cmb_secciones.setGeometry(QtCore.QRect(90, 70, 231, 22))
        self.cmb_secciones.setObjectName("cmb_secciones")
        # título
        self.lbl_titulo = QtWidgets.QLabel(self.data_frame)
        self.lbl_titulo.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.txt_titulo = QtWidgets.QLineEdit(self.data_frame)
        self.txt_titulo.setGeometry(QtCore.QRect(90, 100, 381, 21))
        self.txt_titulo.setObjectName("txt_titulo")
        # cuerpo
        self.lbl_cuerpo = QtWidgets.QLabel(self.data_frame)
        self.lbl_cuerpo.setGeometry(QtCore.QRect(10, 130, 61, 21))
        self.lbl_cuerpo.setObjectName("lbl_cuerpo")
        self.txt_cuerpo = QtWidgets.QTextEdit(self.data_frame)
        self.txt_cuerpo.setGeometry(QtCore.QRect(90, 130, 381, 211))
        self.txt_cuerpo.setObjectName("txt_cuerpo")
        # tabla (widget)
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
        self.tw_noticias.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tw_noticias.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tw_noticias.setColumnWidth(constants.ID_NOTICIA, 10)
        self.tw_noticias.setColumnWidth(constants.FECHA, 75)
        self.tw_noticias.cellClicked.connect(self.on_click_tw)
        # widget central
        main_view.setCentralWidget(self.centralwidget)
        # menú
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
        self.salir = QtWidgets.QAction(main_view)
        self.salir.setObjectName("salir")
        self.menuArchivo.addAction(self.salir)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.actionAcerca_de.triggered.connect(self.about)
        self.salir.triggered.connect(self.end_program)

        model = Model()
        self.controller = Controller(model, self)

        self.retranslateUi(main_view)
        QtCore.QMetaObject.connectSlotsByName(main_view)

        self.create_db()
        self.create_tables()
        self.load_medios()
        self.refresh()
        self.clear_data()

    def retranslateUi(self, main_view):
        _translate = QtCore.QCoreApplication.translate
        main_view.setWindowTitle(_translate("main_view", "Cargador de Noticias"))
        self.btn_base.setToolTip(_translate("main_view", "Crear base de datos."))
        self.btn_tabla.setToolTip(_translate("main_view", "Crear tablas Noticias, Medios y Secciones."))
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
        self.salir.setText(_translate("main_view", "Salir"))

    def end_program(self):
        sys.exit()

    def on_click_tw(self, index):
        """
        evento click en una row
        de la grilla (tablewidget)
        """
        noticia_id = self.tw_noticias.item(index, 0).text()
        self.controller.get_noticia(noticia_id)

    def set_noticia(self, noticia):
        """
        carga una noticia en pantalla
        """
        self.clear_data()

        self.nota_id = noticia[constants.ID_NOTICIA]
        qdate = QtCore.QDate.fromString(noticia[constants.FECHA], "dd/MM/yyyy")
        self.de_fecha.setDate(qdate)
        self.de_fecha.show()
        self.cmb_medios.setCurrentText(noticia[constants.MEDIO])
        self.cmb_secciones.setCurrentText(noticia[constants.SECCION])
        self.txt_titulo.setText(noticia[constants.TITULO])
        self.txt_cuerpo.setText(noticia[constants.CUERPO])

    def delete_data(self):
        """
        elimina un registro
        """
        self.controller.delete_data(self.nota_id)

    def save_data(self):
        """
        guarda un registro
        """
        fecha = self.de_fecha.date().toPyDate().strftime("%Y-%m-%d")

        medio = self.cmb_medios.currentText()
        inicio = medio.find('- (') + 3
        fin = medio.find(')')
        id_medio = int(medio[inicio : fin : 1])

        seccion = self.cmb_secciones.currentText()
        inicio = seccion.find('- (') + 3
        fin = seccion.find(')')
        id_seccion = int(seccion[inicio : fin : 1])

        titulo = self.txt_titulo.text()

        cuerpo = self.txt_cuerpo.toPlainText()

        noti = Noticia(self.nota_id, fecha, id_medio, id_seccion, titulo, cuerpo)

        self.controller.save_data(noti)

    def create_db(self):
        """
        botón crear base evento click
        """
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.controller.create_db()
        self.clear_data()
        self.clear_grid()
        self.clear_combos()
        QApplication.restoreOverrideCursor()

    def create_tables(self):
        """
        botón crear tablas evento click
        """
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.controller.create_tables()
        self.load_medios()
        QApplication.restoreOverrideCursor()

    def clear_grid(self):
        """
        vacía la grilla
        """
        self.tw_noticias.setRowCount(0)

    def clear_combos(self):
        """
        vacía la combos
        """
        self.cmb_medios.clear()
        self.cmb_secciones.clear()

    def clear_data(self):
        """
        limpia la pantalla
        """
        self.nota_id = 0
        date = QDate.currentDate()
        self.de_fecha.setDate(date)
        self.cmb_medios.setCurrentIndex(0)
        self.txt_id_search.setText("")
        self.txt_titulo.setText("")
        self.txt_cuerpo.setText("")

    def refresh(self):
        """
        botón refresh evento click
        """
        try:
            #'Id', 'Fecha', 'Medio', 'Sección', 'Título', 'Cuerpo'
            noticias = self.controller.get_noticias()
            row = 0
            self.tw_noticias.setRowCount(len(noticias))

            cols = 6
            for n in noticias:
                for col in range(0, cols):
                    #print(row, col, n[col])
                    item = QtWidgets.QTableWidgetItem(n[col])
                    if(col < 2):
                        item.setTextAlignment(QtCore.Qt.AlignRight) # esto no funciona

                    self.tw_noticias.setItem(row, col, QtWidgets.QTableWidgetItem(n[col]))
                row += 1
        except:
            pass

    def load_medios(self):
        """
        carga el combo de medios
        """
        try:
            data = self.controller.get_medios()
            for d in data:
                self.cmb_medios.addItem(f"{d[1]} - ({d[0]})")
        except:
            pass

    def load_secciones(self):
        """
        carga el combo de secciones
        según el medio elegido
        """
        try:
            self.cmb_secciones.clear()

            medio = self.cmb_medios.currentText()
            inicio = medio.find('- (') + 3
            fin = medio.find(')')

            id_medio = int(medio[inicio : fin : 1])

            data = self.controller.get_secciones(id_medio)

            for d in data:
                self.cmb_secciones.addItem(f"{d[1]} - ({d[0]})")
        except:
            pass

    def buscar(self):
        """
        busca según id
        """
        search_id = self.txt_id_search.text()
        self.controller.get_noticia(search_id)

    def about(self):
        """
        dialogo about
        """
        self.salta_violeta("Patrón MVC + PyQt5", "Cargador de Noticias\n\nGrupo:\n- Luis Carro\n- Cristian Maier")

    def salta_violeta(self, titulo, texto):
        """
        muestra un diálogo
        """
        QApplication.restoreOverrideCursor()
        icon_form = QtGui.QIcon()
        icon_form.addPixmap(QtGui.QPixmap("./imagenes/noticias.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        msg = QMessageBox()
        msg.setWindowIcon(icon_form)
        msg.setIcon(QMessageBox.Information)
        msg.setText(texto)
        msg.setInformativeText('e-Learning | utn.ba')
        msg.setWindowTitle(titulo)
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_view = QtWidgets.QMainWindow()
    ui = Ui_main_view()
    ui.setupUi(main_view)
    main_view.show()
    sys.exit(app.exec_())
