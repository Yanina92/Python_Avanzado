from tkinter import (
    StringVar,
    IntVar,
    Frame,
    Entry,
    Label,
    Button,
    Radiobutton,
    ttk,
    PhotoImage,
    Tk,
    messagebox,
    Menu,
    TOP,
    BOTH,
)
from modelo import Accionar_bd, extraer_datos_graficar
from tkinter.filedialog import askopenfilename
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk,
)
import pandas as pd


icono = "icono.ico"
fondo = "fondo.gif"


def info():
    """
    VENTANA DE PRESENTACIÓN DE LA APLICACIÓN
    """
    vent_info = Tk()
    vent_info.iconbitmap(icono)
    vent_info.title("Información")
    vent_info.resizable(0, 0)
    vent_info.config(relief="groove", bd=25, bg="light grey")
    vent_info.geometry("400x400")
    frame_info = Frame(vent_info)
    frame_info.place(x=25, y=20)
    frame_info.config(bg="white", width="300", height="300")
    Label(
        frame_info,
        text="Trabajo final Python intermedio\nBiblio App",
        font="none 12 bold",
        bg="white",
    ).place(x=25, y=30)
    Label(
        frame_info,
        text="Desarrolladores\n1. Lucia Leiva\n2. Diego Waicman\n3. Ximena Camacho\n4. Guido Frassetti\n5. Yanina Gonzalez",
        bg="white",
        fg="black",
        font="none 12 bold",
    ).place(x=60, y=80)
    Label(
        frame_info,
        text="UTN e-learning FRBA\n Año: 2021",
        bg="white",
        fg="black",
        font="none 12 bold",
    ).place(x=60, y=210)
    vent_info.mainloop()


def grafico_porcentaje_clasificacion():
    vent_porc = Tk()
    vent_porc.iconbitmap(icono)
    vent_porc.title("Porcentaje de libros por clasificación")
    vent_porc.geometry("600x600")
    df = extraer_datos_graficar()
    categorias = pd.DataFrame(df.Clasificacion.value_counts())
    categorias["Porcentaje"] = (
        categorias["Clasificacion"] * 100
    ) / categorias.Clasificacion.sum()
    labels = list(categorias.index.unique())
    explode = [0.1] * len(categorias)
    fig1, ax1 = plt.subplots()
    ax1.pie(
        categorias["Porcentaje"],
        explode=explode,
        labels=labels,
        autopct="%1.f%%",
        shadow=True,
        startangle=90,
    )
    ax1.axis("equal")
    canvas = FigureCanvasTkAgg(fig1, master=vent_porc)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, vent_porc)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    vent_porc.mainloop()


def grafico_cantidad_clasificacion():
    vent_graf_marca = Tk()
    vent_graf_marca.iconbitmap(icono)
    vent_graf_marca.title("Cantidad de libros por clasificación")
    vent_graf_marca.geometry("600x600")
    df = extraer_datos_graficar()
    fig = plt.figure()
    sns.countplot(x="Clasificacion", data=df)
    plt.ylabel("Cantidad de libros")
    canvas = FigureCanvasTkAgg(fig, master=vent_graf_marca)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, vent_graf_marca)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    vent_graf_marca.mainloop()


class Splash_screen:
    def __init__(self, ventana):
        self.root = ventana
        self.f = Frame(self.root)
        self.root.title(" ")
        self.root.iconbitmap(icono)
        self.root.resizable(0, 0)
        ancho_ventana = 1000
        alto_ventana = 667
        x_ventana = self.root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = (
            str(ancho_ventana)
            + "x"
            + str(alto_ventana)
            + "+"
            + str(x_ventana)
            + "+"
            + str(y_ventana)
        )
        self.root.geometry(posicion)
        self.fondo1 = PhotoImage(file=fondo)
        self.imagen = Label(self.root, image=self.fondo1).place(x=0, y=0)


class Ventana_principal:
    """
    VENTANA PRINCIPAL DE LA APLICACIÓN
    """

    def __init__(self, ventana):
        self.root = ventana
        """
             Posicionamiento y tamaño de ventana
        """
        ancho_ventana = 1160
        alto_ventana = 550
        x_ventana = self.root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = (
            str(ancho_ventana)
            + "x"
            + str(alto_ventana)
            + "+"
            + str(x_ventana)
            + "+"
            + str(y_ventana)
        )
        self.root.geometry(posicion)
        self.root.resizable(0, 0)

        self.tit = StringVar()
        self.des = StringVar()
        self.aut = StringVar()
        self.ed = StringVar()
        self.isbn1 = StringVar()
        self.clas = StringVar()
        self.agno = StringVar()
        self.img = StringVar()
        self.a = IntVar()
        self.opcion = StringVar()
        self.f = Frame(self.root)
        self.objeto_base = Accionar_bd()
        self.tree = ttk.Treeview(self.f)

        """
            DEFINICIÓN DEL MARCO DE LA APLICACIÓN
        """
        # Frame
        self.root.title("Biblio App")
        self.root.iconbitmap(icono)
        self.f.config(width=1020, height=1020)
        self.f.grid(row=15, column=0, columnspan=6)

        """
            DEFINICIÓN DE LAS ETIQUETAS DE LA PANTALLA
        """
        # Etiquetas
        self.superior = Label(
            self.root,
            text="INGRESE LOS DATOS DEL LIBRO",
            bg="grey",
            fg="white",
            width=40,
        )
        self.titulo = Label(self.root, text="Título", font="bold")
        self.descripcion = Label(self.root, text="Descripción", font="bold")
        self.autor = Label(self.root, text="Autor", font="bold")
        self.editorial = Label(self.root, text="Editorial", font="bold")
        self.isbn = Label(self.root, text="ISBN", font="bold")
        self.clasifica = Label(self.root, text="Clasificación", font="bold")
        self.anio = Label(self.root, text="Año", font="bold")

        self.registros = Label(
            self.root,
            text="DISPONIBILIDAD DE LIBROS",
            bg="grey",
            fg="white",
            width=40,
        )

        self.superior.grid(
            row=0, column=0, columnspan=7, padx=1, pady=1, sticky="w" + "e"
        )
        self.titulo.grid(row=1, column=0, sticky="w")
        self.descripcion.grid(row=2, column=0, sticky="w")
        self.autor.grid(row=3, column=0, sticky="w")
        self.editorial.grid(row=4, column=0, sticky="w")
        self.isbn.grid(row=5, column=0, sticky="w")
        self.clasifica.grid(row=6, column=0, sticky="w")
        self.anio.grid(row=7, column=0, sticky="w")

        """
            DEFINICIÓN DEL BOTÓN DE CARGA DE LA IMAGEN DEL LIBRO
        """
        boton_imagen = Button(
            self.root,
            text="Seleccionar Imagen",
            command=lambda: self.cargar_imagen(),
            width=20,
            bg="grey",
            fg="white",
        )
        boton_imagen.grid(row=8, column=0, sticky="w")

        """
            DEFINICIÓN DEL BOTÓN QUE MUESTRA LA IMAGEN DEL LIBRO
        """
        boton_tapa = Button(
            self.root,
            text="Ver Tapa",
            command=lambda: self.mostrar_tapa(self.img),
            width=20,
            bg="grey",
            fg="white",
        )
        boton_tapa.grid(row=8, column=1, sticky="w")

        self.registros.grid(
            row=9, column=0, columnspan=7, padx=1, pady=1, sticky="w" + "e"
        )

        """
            DEFINICIÓN DE LOS CAMPOS DE ENTRADA
        """
        # Entradas
        self.Ent1 = Entry(self.root, textvariable=self.tit, width=100)
        self.Ent1.grid(row=1, column=1)
        self.Ent2 = Entry(self.root, textvariable=self.des, width=100)
        self.Ent2.grid(row=2, column=1)
        self.Ent3 = Entry(self.root, textvariable=self.aut, width=100)
        self.Ent3.grid(row=3, column=1)
        self.Ent4 = Entry(self.root, textvariable=self.ed, width=100)
        self.Ent4.grid(row=4, column=1)
        self.Ent5 = Entry(self.root, textvariable=self.isbn1, width=100)
        self.Ent5.grid(row=5, column=1)
        self.Ent6 = Entry(self.root, textvariable=self.clas, width=100)
        self.Ent6.grid(row=6, column=1)
        self.Ent7 = Entry(self.root, textvariable=self.agno, width=100)
        self.Ent7.grid(row=7, column=1)
        self.Ent8 = Entry(self.root, textvariable=self.img, width=100)

        """
            DEFINICIÓN DE LOS BOTONES
        """
        # Botones
        self.boton_alta = Button(
            self.root, text="Alta", command=lambda: self.alta(), width=20
        )
        self.boton_alta.grid(row=1, column=3)

        self.boton_borrar = Button(
            self.root, text="Baja", command=lambda: self.borrar(), width=20
        )
        self.boton_borrar.grid(row=2, column=3)

        self.boton_modifica = Button(
            self.root,
            text="Modificación",
            command=lambda: self.modificar(),
            width=20,
        )
        self.boton_modifica.grid(row=3, column=3)

        self.boton_consulta = Button(
            self.root,
            text="Consulta",
            command=lambda: self.consulta(),
            width=20,
        )
        self.boton_consulta.grid(row=4, column=3)

        self.boton_reinicio = Button(
            self.root,
            text="Disponibilidad de Libros",
            command=lambda: self.reinicio_treeview(),
            width=20,
        )
        self.boton_reinicio.grid(row=5, column=3)

        def selectitem(a):
            curitem = self.tree.focus()

        """
            DEFINICIÓN DEL TREEVIEW
        """
        # Tree
        self.tree["columns"] = (
            "col1",
            "col2",
            "col3",
            "col4",
            "col5",
            "col6",
            "col7",
        )
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=150, minwidth=80)
        self.tree.column("col2", width=150, minwidth=80)
        self.tree.column("col3", width=150, minwidth=80)
        self.tree.column("col4", width=150, minwidth=80)
        self.tree.column("col5", width=150, minwidth=80)
        self.tree.column("col6", width=150, minwidth=80)
        self.tree.column("col7", width=150, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Título")
        self.tree.heading("col2", text="Descripción")
        self.tree.heading("col3", text="Autor")
        self.tree.heading("col4", text="Editorial")
        self.tree.heading("col5", text="ISBN")
        self.tree.heading("col6", text="Clasificación")
        self.tree.heading("col7", text="Año")
        self.tree.grid(row=9, column=0, columnspan=4)

        self.objeto_base.actualizar_treeview(self.tree)
        self.tree.bind("<<TreeviewSelect>>", self.selecciono_tree)

        """
            DEFINICIÓN DE LA BARRA DE SCROLL VERTICAL
        """
        scroll_vertical = ttk.Scrollbar(
            self.f, orient="vertical", command=self.tree.yview
        )
        scroll_vertical.grid(row=9, column=1000, sticky="ns")
        self.tree.configure(yscrollcommand=scroll_vertical.set)

        """
            DEFINICIÓN DE LA BARRA DE SCROLL HORIZONTAL POR SI 
            EN ALGÚN MOMENTO SE PUEDE NECESITAR.
            AHORA NO SE USA.
        """
        # Barra de scroll horizontal
        """
        scroll_horizontal = ttk.Scrollbar(
            self.f, orient="horizontal", command=self.tree.xview
        )
        scroll_horizontal.grid(row=1, column=0, columnspan=2, sticky="we")
        self.tree.configure(xscrollcommand=scroll_horizontal.set)
        """
        self.Ent1.focus_set()

        """
            DEFINICIÓN DEL MENÚ
        """
        # Menú
        menu_barra = Menu(self.root)  # Indica que crearé un menú
        self.root.config(menu=menu_barra)  # Muestra el menú
        opciones1 = Menu(
            menu_barra
        )  # Indica que trabajaré con una cascada (crearé un botón cascada)
        menu_barra.add_cascade(
            label="Ver gráficos", menu=opciones1
        )  # Nombre de la primera cascada
        opciones1.add_command(
            label="Porcentaje de libros por clasificación",
            command=grafico_porcentaje_clasificacion,
        )
        opciones1.add_separator()  # Separador
        opciones1.add_command(
            label="Cantidad de libros por clasificación",
            command=grafico_cantidad_clasificacion,
        )
        menu_barra.add_command(
            label="Sobre el programa..", command=info
        )  # Creo en el menú principal un botón simple

    def selecciono_tree(self, evento):
        current_item = self.tree.focus()
        if not current_item:
            return
        data = self.tree.item(current_item)
        titu, desc, auto, edi, isb, clasi, agnio, imag = data["values"]
        self.tit.set(titu)
        self.des.set(desc)
        self.aut.set(auto)
        self.ed.set(edi)
        self.isbn1.set(isb)
        self.clas.set(clasi)
        self.agno.set(agnio)
        self.img = imag

    def alta(
        self,
    ):
        self.objeto_base.alta(
            self.tit,
            self.des,
            self.aut,
            self.ed,
            self.isbn1,
            self.clas,
            self.agno,
            self.img,
            self.tree,
        )

        self.blanquear_campos()

    def borrar(
        self,
    ):
        self.objeto_base.baja(self.tit, self.tree)

        self.blanquear_campos()

    def modificar(
        self,
    ):
        self.objeto_base.modificar(
            self.tit,
            self.des,
            self.aut,
            self.ed,
            self.isbn1,
            self.clas,
            self.agno,
            self.img,
            self.tree,
        )

        self.blanquear_campos()

    def consulta(
        self,
    ):
        self.objeto_base.consultar(
            self.tit,
            self.des,
            self.aut,
            self.ed,
            self.isbn1,
            self.clas,
            self.agno,
            self.tree,
        )

        self.blanquear_campos()

    def reinicio_treeview(
        self,
    ):
        self.objeto_base.actualizar_treeview(self.tree)
        self.blanquear_campos()

    def cargar_imagen(
        self,
    ):
        self.img = askopenfilename()

    def mostrar_tapa(self, imagen):

        if imagen != "None":
            fondito = imagen
            fondo1 = Image.open(fondito)
            fondo1.show()
        else:
            messagebox.showinfo(
                message="No hay imagen de tapa cargada",
                title="Estado",
            )

        # CON PHOTOIMAGE ARROJA UN ERROR EXTRANIO
        #        self.tapa = Tk()
        #        self.tapa.iconbitmap(icono)
        #        self.tapa.geometry("400x400")
        #        self.tapa.resizable(0, 0)
        #        fondo1 = PhotoImage(file=fondito)
        #        self.imagen1 = Label(self.tapa, image=fondo1)
        #        self.imagen1.grid(row=0, column=0)

    def blanquear_campos(
        self,
    ):
        self.tit.set("")
        self.des.set("")
        self.aut.set("")
        self.ed.set("")
        self.isbn1.set("")
        self.clas.set("")
        self.agno.set("")
        self.Ent1.focus_set()
