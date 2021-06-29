from tkinter import Tk
from vista import Ventana_principal, Splash_screen


class Controlador:
    """
    CLASE PRINCIPAL DE LA APLICACIÓN
    """

    def __init__(self, root):
        self.root_controlador = root
        self.activa_pantalla()

    def activa_pantalla(
        self,
    ):

        Ventana_principal(self.root_controlador)


def main_window():
    spl_screen.destroy()
    root_tk = Tk()
    biblio_app = Controlador(root_tk)
    root_tk.mainloop()


if __name__ == "__main__":
    spl_screen = Tk()
    presentacion = Splash_screen(spl_screen)
    spl_screen.after(
        5000, main_window
    )  # Indica que acción realizaré luego de 5 segundos
    spl_screen.mainloop()
