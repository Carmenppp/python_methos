def procesar_opcion(num):
    if num == 1:
        ingresar_puntos_evaluacion()
    elif num == 2:
        mostrar_resultados()
    elif num == 3:
        print('Saliendo del programa')
        quit()
    else:
        print('Por favor ingrese un valor del 1 al 3')

def ingresar_puntos_evaluacion():
    while True:
        print('Ingrese una evaluación del 1 al 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point < 1 or point > 5:
                print('Ingrese un valor del 1 al 5')
            else:
                print('Ingrese un comentario')
                comment = input()
                post = f'Punto: {point} Comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print('Ingrese puntos de evaluación como números')

def mostrar_resultados():
    print('Resultados hasta el momento:')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

while True:
    print('Seleccione la acción que desea realizar')
    print('1: Ingresar puntos de evaluación y comentarios')
    print('2: Ver resultados hasta el momento')
    print('3: Salir')
    num = input()

    if num.isdecimal():
        num = int(num)
        procesar_opcion(num)
    else:
        print('Por favor ingrese un valor del 1 al 3')
