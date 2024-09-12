#La prueba Q es un método estadístico que permite evaluar si un dato proveniente de un determinado análisis debe ser descartado
#a la hora de analizar la población.
import msvcrt
from os import system
import numpy as np

Q90 = {3:0.941, 4:0.765, 5:0.642, 6:0.560, 7:0.507, 8:0.468, 9:0.437, 10:0.412, 15:0.338, 20:0.300, 25:0.277, 30:0.260}
Q95 = {3:0.970, 4:0.829, 5:0.710, 6:0.625, 7:0.568, 8:0.526, 9:0.466, 10:0.466, 15:0.384, 20:0.342, 25:0.317, 30:0.298}
Q99 = {3:0.994, 4:0.926, 5:0.821, 6:0.740, 7:0.680, 8:0.634, 9:0.598, 10:0.568, 15:0.475, 20:0.425, 25:0.393, 30:0.372}

def insertar_datos():               #Insertar datos y ordenarlos de menor a mayor.
    datos = []
    while True:
        try:
            datos.append(float(input('\nIngrese su valor, colocando un punto como separación decimal: ')))
        except ValueError:          #Verifica que si sale un error de ese tipo vuelva al principio del loop.
            print('Recuerda ingresar el número colocando un punto como separación decimal.')
            continue 
        
        system('cls')
        print(f'\nLos datos que ingresó son: {datos}')
        print('\nPara continuar agregando datos, presione [ENTER]\nSi ya terminó de agregar los datos, presione [ESCAPE]')
        
        tecla = msvcrt.getch()
        if tecla == b'\x1b':   #Escape
            break
        
    system('cls')
    n_datos = len(datos)
    print(f'Los datos que ingresó son: {datos}.\nEn total, ingresaste {n_datos} datos')
    print(f'Aprieta [1] Para confirmar.')
    print(f'Aprieta [2] Si quieres borrar un valor.')
    print(f'Aprieta [3] Si quieres editar un valor')
    print(f'Aprieta [4] Si quieres agregar un nuevo valor')
    
    key = 0
    while True:
        try:
            key = float(msvcrt.getch())
            break
        except ValueError:
            print('Ingresa una variable válida.')
            continue
    
    while key != 1:
        if key == 1:
            break
        
        if key == 2:
            eliminar = float(input('Selecciona el valor que quieres eliminar: '))
            while eliminar not in datos:
                eliminar = float(input('El valor que seleccionaste no se encuentra dentro de la lista de datos, por favor escoge otro: '))
            datos.remove(eliminar)
            n_datos = len(datos)
            system('cls')
            print(f'La nueva lista de datos es: {datos}, y tiene {len(datos)} datos')
            print(f'Aprieta [1] Para confirmar.')
            print(f'Aprieta [2] Si quieres borrar un valor.')
            print(f'Aprieta [3] Si quieres editar un valor')
            print(f'Aprieta [4] Si quieres agregar un nuevo valor')
            key = 0
            while True:
                try:
                    key = float(msvcrt.getch())
                    break
                except ValueError:
                    print('Ingresa una variable válida.')
                    continue
            
        if key == 3:
            try:
                editar = float(input('Selecciona el valor que quieres editar: '))
            except ValueError:
                print('El valor que seleccionaste no se encuentra dentro de la lista de datos, por favor escoge otro')
            indice = datos.index(editar)
            datos[indice] = float(input('Escribe nuevamente el valor: '))
            system('cls')
            print(f'La nueva lista de datos es: {datos}, y tiene {len(datos)} datos')
            print(f'Aprieta [1] Para confirmar.')
            print(f'Aprieta [2] Si quieres borrar un valor.')
            print(f'Aprieta [3] Si quieres editar un valor')
            print(f'Aprieta [4] Si quieres agregar un nuevo valor')
            key = 0
            while True:
                try:
                    key = float(msvcrt.getch())
                    break
                except ValueError:
                    print('Ingresa una variable válida.')
                    continue
        
        if key == 4:
            try:
                datos.append(float(input('\nIngrese su valor, colocando un punto como separación decimal: ')))
            except ValueError:          #Verifica que si sale un error de ese tipo vuelva al principio del loop.
                print('Recuerda ingresar el número colocando un punto como separación decimal.')
                continue 
            system('cls')
            datos.sort()
            print(f'La nueva lista de datos es: {datos}, y tiene {len(datos)} datos')
            print(f'Aprieta [1] Para confirmar.')
            print(f'Aprieta [2] Si quieres borrar un valor.')
            print(f'Aprieta [3] Si quieres editar un valor')
            print(f'Aprieta [4] Si quieres agregar un nuevo valor')
            key = 0
            while True:
                try:
                    key = float(msvcrt.getch())
                    break
                except ValueError:
                    print('Ingresa una variable válida.')
                    continue

        else:
            print('Por favor, selecciona una de las opciones para continuar.')
            key = key = float(msvcrt.getch())
        
    system('cls')
    datos.sort()
    print(f'Los datos ordenados de menor a mayor son:\n {datos}\n En total hay {n_datos}')
    valor = float(input('Por favor, escoge el valor sobre el cual quieres realizar la prueba Q: '))
    while valor not in datos:
        valor = float(input('El valor que seleccionaste no se encuentra dentro de la lista de datos, por favor escoge otro: '))
    return datos, n_datos, valor

def nivel_confianza():              #Selecciona un nivele de confianza.
    print('Selecciona un nivel de confianza: ')
    print('Aprieta [1] si quieres un nivel de confianza de 90%')
    print('Aprieta [2] si quieres un nivel de confianza de 95%')
    print('Aprieta [3] si quieres un nivel de confianza de 99%')
    while True:
        try:
            tecla = int(msvcrt.getch())
        except ValueError:
            print('Por favor, selecciona un número válido.')
            continue
        Nivel_Confianza = False
        if tecla == 1:
            system('cls')
            print('Escogiste un nivel de confianza del 90%')
            Nivel_Confianza = Q90
            break
        elif tecla == 2:
            system('cls')
            print('Escogiste un nivel de confianza del 95%')
            Nivel_Confianza = Q95
            break
        elif tecla == 3:
            system('cls')
            print('Escogiste un nivel de confianza del 99%')
            Nivel_Confianza = Q99   
            break 
        elif tecla not in range(1,4):
            print('Por favor, selecciona un número válido.')
    return Nivel_Confianza    

def q_crit(datos, n_datos,Nivel_Confianza):                       #Selecciona el Q crítico.
    if n_datos in range (3,11):
        qcr = Nivel_Confianza[n_datos]
        print(f'El Q crítico es igual a {qcr}')
    elif n_datos == 11:
        x_vals = [10, 15]
        y_vals = [Nivel_Confianza[10], Nivel_Confianza[15]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 12:
        x_vals = [10, 15]
        y_vals = [Nivel_Confianza[10], Nivel_Confianza[15]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 13:
        x_vals = [10, 15]
        y_vals = [Nivel_Confianza[10], Nivel_Confianza[15]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 14:
        x_vals = [10, 15]
        y_vals = [Nivel_Confianza[10], Nivel_Confianza[15]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 15:
        qcr = Nivel_Confianza[n_datos]
        print(f'El Q crítico es igual a {qcr}')
    elif n_datos == 16:
        x_vals = [15, 20]
        y_vals = [Nivel_Confianza[15], Nivel_Confianza[20]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 17:
        x_vals = [15, 20]
        y_vals = [Nivel_Confianza[15], Nivel_Confianza[20]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 18:
        x_vals = [15, 20]
        y_vals = [Nivel_Confianza[15], Nivel_Confianza[20]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 19:
        x_vals = [15, 20]
        y_vals = [Nivel_Confianza[15], Nivel_Confianza[20]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 20:
        qcr = Nivel_Confianza[n_datos]
        print(f'El Q crítico es igual a {qcr}')
    elif n_datos == 21:
        x_vals = [20, 25]
        y_vals = [Nivel_Confianza[20], Nivel_Confianza[25]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 22:
        x_vals = [20, 25]
        y_vals = [Nivel_Confianza[20], Nivel_Confianza[25]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 23:
        x_vals = [20, 25]
        y_vals = [Nivel_Confianza[20], Nivel_Confianza[25]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 24:
        x_vals = [20, 25]
        y_vals = [Nivel_Confianza[20], Nivel_Confianza[25]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 25:
        qcr = Nivel_Confianza[n_datos]
        print(f'El Q crítico es igual a {qcr}')
    elif n_datos == 26:
        x_vals = [25, 30]
        y_vals = [Nivel_Confianza[25], Nivel_Confianza[30]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 27:
        x_vals = [25, 30]
        y_vals = [Nivel_Confianza[25], Nivel_Confianza[30]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 28:
        x_vals = [25, 30]
        y_vals = [Nivel_Confianza[25], Nivel_Confianza[30]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 29:
        x_vals = [25, 30]
        y_vals = [Nivel_Confianza[25], Nivel_Confianza[30]]
        qcr = np.interp(n_datos,x_vals,y_vals)
        print(f'El valor de Q crítico se obtuvo por interpolación lineal y es igual a {qcr}')
    elif n_datos == 30:
        qcr = Nivel_Confianza[n_datos]
        print(f'El Q crítico es igual a {qcr}')
    elif n_datos > 30:
        print('Lo siento, solo puedo realizar esta prueba hasta un maximo de 30 datos :()')

    qcr = round(qcr, 3)
    return qcr


def Valor_Cercano(valor, datos):
    diferencias = []
    datos_sin_valor = [dato for dato in datos if dato != valor]
    diferencias = [abs(valor - dato) for dato in datos_sin_valor]
    valor_cercano = abs(min(diferencias) + valor)
    print(f'El valor mas cercano es {valor_cercano}')
    return valor_cercano

def calculo_q(valor, valor_cercano, datos):
    amplitud = (max(datos) - min(datos))
    numerador = abs(valor - valor_cercano)
    q = round((numerador / amplitud), 3) 
    print(f'El valor de Q es {q}')
    return q

def Prueba_Q():
    datos, n_datos, valor = insertar_datos()
    Nivel_Confianza = nivel_confianza()
    valor_cercano = Valor_Cercano(valor, datos)
    qcr = q_crit(datos, n_datos,Nivel_Confianza)
    q = calculo_q(valor,valor_cercano,datos)
    
    if q>qcr:
        print(f'Q es mayor Qcr, por lo cual deberías descartar el valor {valor}')
    elif q<qcr:
        print(f'Q es menor a Qcr, por lo cual conservar descartar el valor {valor}')
    
    print('Selecciona [ENTER] si te gustaría realizar nuevamente la prueba Q para el mismo conjunto de datos')
    print('Selecciona cualquier otra tecla si quieres finalizar')
    tecla = msvcrt.getch()
    while tecla == b'\r': #enter
        valor = float(input('Ingresa el nuevo valor: '))
        while valor not in datos:
            valor = float(input('El valor que seleccionaste no se encuentra dentro de la lista de datos, por favor escoge otro: '))
        Nivel_Confianza = nivel_confianza()
        valor_cercano = Valor_Cercano(valor, datos)
        qcr = q_crit(datos, n_datos,Nivel_Confianza)
        q = calculo_q(valor,valor_cercano,datos)
        if q<qcr:
            system('cls')
            print(f'Q es mayor Qcr, por lo cual deberías descartar el valor {valor}')
        elif q>qcr:
            system('cls')
            print(f'Q es menor a Qcr, por lo cual conservar descartar el valor {valor}')
            
        print('\n\nAprieta [ENTER] si te gustaría realizar nuevamente la prueba Q para el mismo conjunto de datos')
        print('Aprieta cualquier otra tecla si quieres finalizar')
        tecla = msvcrt.getch()
    print('Gracias por utilizar este código. Espero que te haya sido útil.')

Prueba_Q()