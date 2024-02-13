
from pathlib import Path
import os





def volver_inicio():
    opcion_inicio()



def leer_texto(ruta, receta):
    ruta_receta = Path(ruta_principal,ruta,receta)
    print(receta)
    print(ruta_receta.read_text())
    x = input()
    limpiar_pantalla()




def creador_receta(ruta):

    existe = False
    while not existe :
        print("escribe el nombre de tu receta:  ")
        nombre_receta = input() +'.txt'
        contenido_receta = input("escribe el contenido de la receta: ")
        ruta_nueva = Path(ruta_principal,ruta, nombre_receta)
        if not os.path.exists(ruta_nueva):
            Path(ruta_nueva).write_text(contenido_receta)
            print( f"Bien, La receta {nombre_receta} a sido creada ")
            x = input()
            existe = True
        else:
            print(f"Ya esta creada la receta {nombre_receta} ")
            existe = True
    limpiar_pantalla()

def mostar_recetas(ruta_recetas):


    lista_recetas =[]
    print("Recetas: \n")
    ruta_receta = Path(ruta_principal, ruta_recetas)
    if os.path.exists(ruta_receta):
        for item,ruta_recetas in enumerate(ruta_receta.iterdir()):

            if ruta_recetas.is_file():
                lista_recetas.append(ruta_recetas.name)
                print(f" \t [{item+1}] {ruta_recetas.name} ")

    return lista_recetas










def elegir_recetas(list):

    receta_elegida = "x"
    while not receta_elegida.isnumeric() or int(receta_elegida) not in range(1,len(list)+1) :
        receta_elegida = input("")

    limpiar_pantalla()
    return list[int(receta_elegida)-1]



def creador_categoria(ruta):



    existe = False

    while not existe:
        print("escribe el nombre de tu categoria ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta ,nombre_categoria)
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print( f"La categoria  '{nombre_categoria}' a sido creada")
            x = input()
            existe = True
        else:
            print(f"Ya esta creada la categoria {nombre_categoria} ")
            x = input()
    limpiar_pantalla()


def eliminador_receta(ruta):

    receta = Path(ruta_principal,ruta)
    if receta.exists():

        print(f"la receta {receta.name} ha sido eliminado.")
        Path(receta).unlink()
        x = input()
    else:
        print(f"El archivo {receta.name} no existe.")
        x = input()




def eliminador_categoria(ruta_categoria):

    print(ruta_categoria)
    categoria_eliminar = Path(ruta_principal,ruta_categoria)
    if categoria_eliminar.exists():
        print(f"la Categoria {categoria_eliminar.name} ha sido eliminada")
        Path.rmdir(categoria_eliminar)
        x = input()
    else:
        print(f"la categoria {categoria_eliminar} no existe ")
        x = input()


def elegir_categoria(lista):


    categoria_elegida = "x"
    while not categoria_elegida.isnumeric() or int(categoria_elegida) not in range(1,len(lista)+1) :
        categoria_elegida = input("")


    return  lista[int(categoria_elegida)-1]





def mostar_categoria(ruta):

    lista_categoria = []
    directorio_categoria = Path(ruta)
    print("Categorias: ")
    for item,categoria in enumerate(directorio_categoria.iterdir()):
        if categoria.is_dir():
            print(f" \t [{item+1}].{categoria.name} ")
            lista_categoria.append(categoria.name)


    return  lista_categoria


def opcion_inicio():
    opcion = "x"


    while not opcion.isnumeric()  or  int(opcion) in range(1,7):

        opcion = input("""Elegir una Opcion
            [1].Leer Receta.
            [2].Crear Recerta.
            [3].Crear Categoria.
            [4].Eliminar Receta.
            [5].Eliminar Categoria.
            [6].Finalizar Programa.
        """)


        if opcion == '1' :

            categia_elegida = mostar_categoria(ruta_principal)
            ruta_categoria = elegir_categoria(categia_elegida)
            list_recetas = mostar_recetas(ruta_categoria)
            if len(list_recetas) < 1:
                print("no hay recetas en esta categoría.")

            else:
                mi_receta = elegir_recetas(list_recetas)
                list_recetas(mi_receta)
                ruta_receta = elegir_recetas(list_recetas)
                leer_texto(ruta_categoria,ruta_receta)
            volver_inicio()

        elif opcion == '2' :

            categia_elegida = mostar_categoria(ruta_principal)
            ruta_categoria = elegir_categoria(categia_elegida)
            creador_receta(ruta_categoria)
            volver_inicio()

        elif opcion == '3' :

            creador_categoria(ruta_principal)
            volver_inicio()

        elif opcion == '4' :

            categia_elegida = mostar_categoria(ruta_principal)
            ruta_categoria = elegir_categoria(categia_elegida)
            list_recetas = mostar_recetas(ruta_categoria)
            if len(list_recetas) < 1:
                print("no hay recetas en esta categoría.Para eliminar")

            else:
                ruta_receta = elegir_recetas(list_recetas)
                eliminador_receta(Path(ruta_categoria, ruta_receta))

            volver_inicio()

        elif opcion == '5' :

            categia_elegida = mostar_categoria(ruta_principal)
            ruta_categoria = elegir_categoria(categia_elegida)
            eliminador_categoria(ruta_categoria)
            volver_inicio()



        elif opcion == '6' :
            print("Fin del Programa")
            break



def inicio():

    print("*"*50)

    print("Saludos Bienvenido al recetario.")
    print("*" * 50)
    print(f"Ruta de recetas: {ruta_principal}")
    print("*" * 50)
    print(f"Total de recetas: {contador_recetas(ruta_principal)}")
    print("*" * 50)
    x = input()
    limpiar_pantalla()




def contador_recetas(ruta):
    contador = 0

    for x in Path(ruta).glob("**/*.txt"):
        contador +=1

    return contador

def limpiar_pantalla():
    print('\n' * 60)


ruta_principal = Path(Path.home(),"Downloads","Recetas")
inicio()
opcion_inicio()





