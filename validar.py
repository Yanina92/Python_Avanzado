import re
from tkinter import messagebox

"""
    CLASE PARA VALIDAR LOS INGRESOS DE DATOS
"""


class Validar:
    def __init__(
        self,
    ):
        pass

    """
        REGEX PARA VALIDAR EL ISBN DEL LIBRO
    """

    def valida_isbn(self, isbn):
        isbn_a_validar = isbn.get()
        isbn_regex = re.compile("^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$")
        return isbn_regex.search(isbn_a_validar) is not None

    def valida_ingresos(self, tit, des, aut, edi, isbn, clasi, agno, img):

        try:
            if (
                tit.get() != ""
                and des.get() != ""
                and aut.get() != ""
                and edi.get() != ""
                and isbn.get() != ""
                and clasi.get() != ""
                and agno.get() != ""
                and img != ""
            ):
                ret = True
            else:
                ret = False

            return ret
        except (TypeError, ValueError):
            messagebox.showinfo(
                message="Verifique la información !!",
                title="Estado",
            )
        except:
            raise ("Error inesperado !! Avisar a Sistemas")
