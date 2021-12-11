"""
Módulo principal
"""
import tkinter as tk
from modulos.main_view import Ui_main_view
from modulos.view import View
from modulos.model import Model
from modulos.controller import Controller

class App():
    """
    clase App
    por lo que entiendo hereda Tk
    inspirado en https://www.pythontutorial.net/tkinter/tkinter-mvc/
    """
    def __init__(self):
        # create a model
        model = Model()

        # create a view and place it on the root window
        view = Ui_main_view()

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
