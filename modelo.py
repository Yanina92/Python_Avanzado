import sqlite3
from tkinter import messagebox
from validar import Validar
import pandas as pd


def extraer_datos_graficar():
    miconexion = sqlite3.connect("biblioteca.db")
    micursor = miconexion.cursor()
    micursor.execute("SELECT * FROM libros")
    variable = micursor.fetchall()
    miconexion.commit()
    miconexion.close()
    df = pd.DataFrame(variable)
    df = df.rename(
        columns={
            0: "ID",
            1: "Titulo",
            2: "Descripcion",
            3: "Autor",
            4: "Editorial",
            5: "Isbn",
            6: "Clasificacion",
            7: "Anio",
            8: "Imagen",
        }
    )
    return df


"""
    ALTA, BAJA, MODIFICACION Y CONSULTA A LA BASE DE DATOS
"""


class Accionar_bd:
    def __init__(
        self,
    ):
        self.valido = Validar()
        try:
            con = self.conexion()
            cursorObj = con.cursor()
            cursorObj.execute(
                "CREATE TABLE libros(id integer PRIMARY KEY, titulo text, \
                     descripcion text, autor text, editorial text, isbn text, \
                     clasificacion text, anio text, imagen blob"
            )
            con.commit()
            con.close()
            messagebox("La Base de Datos fue creada correctamente!!!")
        except:
            pass

    def conexion(
        self,
    ):
        try:
            con = sqlite3.connect("biblioteca.db")
            return con
        except sqlite3.Error:
            raise ("Error grave!! Comuníquese con Sistemas")

    def cerrar_conexion(
        self,
    ):
        try:
            self.con.close()
        except sqlite3.Error:
            raise ("Error grave!! Comuníquese con Sistemas")

    def actualizar_treeview(self, mitreeview):

        registros = mitreeview.get_children()
        for elemento in registros:
            mitreeview.delete(elemento)

        sql = "SELECT * FROM libros ORDER BY id DESC"

        con = self.conexion()
        try:
            cursorobj = con.cursor()
            datos = cursorobj.execute(sql)
            con.commit()
        except:
            messagebox.showinfo(
                message="Se produjo un error !!",
                title="Estado",
            )

        resultado = datos.fetchall()
        for fila in resultado:
            mitreeview.insert(
                "",
                0,
                text=fila[0],
                values=(
                    fila[1],
                    fila[2],
                    fila[3],
                    fila[4],
                    fila[5],
                    fila[6],
                    fila[7],
                    fila[8],
                ),
            )
        con.close()

    def alta(
        self,
        titulo,
        descripcion,
        autor,
        editorial,
        isbn,
        clasificacion,
        anio,
        imagen,
        mitreeview,
    ):
        if not self.valido.valida_ingresos(
            titulo,
            descripcion,
            autor,
            editorial,
            isbn,
            clasificacion,
            anio,
            imagen,
        ):
            messagebox.showinfo(
                message="Debe completar todos los campos",
                title="Estado",
            )
        else:
            if self.valido.valida_isbn(isbn):
                confirma = messagebox.askquestion(
                    "Confirma el ALTA", "Está seguro"
                )
                if confirma == "yes":
                    try:
                        datos = (
                            titulo.get(),
                            descripcion.get(),
                            autor.get(),
                            editorial.get(),
                            isbn.get(),
                            clasificacion.get(),
                            anio.get(),
                            imagen,
                        )

                        con = self.conexion()
                        sql = "INSERT INTO libros(titulo, descripcion, autor, editorial, isbn, \
                                clasificacion, anio, imagen) VALUES(?, ?, ?, ?, ?, ?, ?, ?) "
                        cur = con.cursor()
                        cur.execute(sql, datos)
                        con.commit()
                        self.actualizar_treeview(mitreeview)
                        con.close()
                        messagebox.showinfo(
                            message="El libro ha sido dado de alta.",
                            title="Estado",
                        )
                    except sqlite3.OperationalError:
                        messagebox.showinfo(
                            message="El libro NO ha sido dado de alta.",
                            title="Estado",
                        )
                    finally:
                        messagebox.showinfo(
                            message="Proceso de Alta finalizado.",
                            title="Estado",
                        )
                else:
                    messagebox.showinfo(
                        message="El libro NO ha sido dado de alta",
                        title="Estado",
                    )
            else:
                messagebox.showinfo(
                    message="Debe ingresar un ISBN válido",
                    title="Estado",
                )

    def baja(self, tit, mitreeview):
        confirma = messagebox.askquestion(
            "Confirmación de BAJA", "Está seguro"
        )
        if confirma == "yes":
            try:
                datos = (tit.get(),)
                con = self.conexion()
                sql = "DELETE FROM libros WHERE (titulo=?)"
                cur = con.cursor()
                cur.execute(sql, datos)
                con.commit()
                self.actualizar_treeview(mitreeview)
                con.close()
            except:
                messagebox.showinfo(
                    message="El libro NO ha sido eliminado",
                    title="Estado",
                )
        else:
            messagebox.showinfo(
                message="El libro NO ha sido eliminado",
                title="Estado",
            )

    def modificar(
        self,
        titulo,
        descripcion,
        autor,
        editorial,
        isbn,
        clasificacion,
        anio,
        imagen,
        mitreeview,
    ):
        if not self.valido.valida_ingresos(
            titulo,
            descripcion,
            autor,
            editorial,
            isbn,
            clasificacion,
            anio,
            imagen,
        ):
            messagebox.showinfo(
                message="Debe completar todos los campos",
                title="Estado",
            )
            return False
        else:
            if self.valido.valida_isbn(isbn):
                confirma = messagebox.askquestion(
                    "Confirmación de MODIFICACION", "Está seguro"
                )
                if confirma == "yes":
                    try:
                        datos = (
                            descripcion.get(),
                            autor.get(),
                            editorial.get(),
                            isbn.get(),
                            clasificacion.get(),
                            anio.get(),
                            imagen,
                            titulo.get(),
                        )
                        con = self.conexion()
                        sql = "UPDATE libros SET descripcion = ?, autor = ?, editorial = ?, \
                                 isbn = ?, clasificacion = ?, anio = ?, imagen = ? WHERE titulo = ?"
                        cur = con.cursor()
                        cur.execute(sql, datos)
                        con.commit()
                        self.actualizar_treeview(mitreeview)
                        con.close()
                    except:
                        messagebox.showinfo(
                            message="El libro NO ha sido modificado",
                            title="Estado",
                        )
                else:
                    messagebox.showinfo(
                        message="El libro NO ha sido modificado",
                        title="Estado",
                    )
            else:
                messagebox.showinfo(
                    message="Debe ingresar un ISBN válido",
                    title="Estado",
                )

    def consultar(
        self,
        titulo,
        descripcion,
        autor,
        editorial,
        isbn,
        clasificacion,
        anio,
        mitreeview,
    ):
        confirma = messagebox.askquestion(
            "Confirma la CONSULTA", "Está seguro"
        )
        if confirma == "yes":
            try:
                datos = (
                    titulo.get(),
                    descripcion.get(),
                    autor.get(),
                    editorial.get(),
                    isbn.get(),
                    clasificacion.get(),
                    anio.get(),
                )
                con = self.conexion()
                sql = "SELECT * FROM libros WHERE titulo=? OR descripcion=? OR autor=? \
                        OR editorial=? OR isbn=? OR clasificacion=? OR anio=?"
                cur = con.cursor()
                encontrados = cur.execute(sql, datos)
                con.commit()

                registros = mitreeview.get_children()
                for elemento in registros:
                    mitreeview.delete(elemento)

                resultado = encontrados.fetchall()
                if resultado != []:
                    for fila in resultado:
                        mitreeview.insert(
                            "",
                            0,
                            text=fila[0],
                            values=(
                                fila[1],
                                fila[2],
                                fila[3],
                                fila[4],
                                fila[5],
                                fila[6],
                                fila[7],
                            ),
                        )
                    con.close()
                else:
                    messagebox.showinfo(
                        message="No se encontró información.",
                        title="Estado",
                    )
            except:
                messagebox.showinfo(
                    message="El libro NO ha sido encontrado",
                    title="Estado",
                )
