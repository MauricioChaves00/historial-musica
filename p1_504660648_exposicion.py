"""Demostración interactiva para exponer el historial musical.
Colocar este archivo en la misma carpeta que p1_504660648_Estructura.py.
"""
from p1_504660648_Estructura import HistorialMusical


def mostrar(historial):
    canciones = list(historial.recorrer())
    if not canciones:
        print('\nEl historial está vacío.')
        return
    print('\nHISTORIAL DE CANCIONES')
    for numero, nodo in enumerate(canciones, 1):
        marca = '  <-- ACTUAL' if nodo is historial.actual else ''
        print(f'{numero}. {nodo.titulo} - {nodo.artista}{marca}')
    print('Primera:', historial.primera.titulo)
    print('Última:', historial.ultima.titulo)


def main():
    historial = HistorialMusical()
    for titulo, artista in [('Canción A', 'Artista A'),
                            ('Canción B', 'Artista B'),
                            ('Canción C', 'Artista C')]:
        historial.agregar_cancion(titulo, artista)
    print('DEMO: LISTA DOBLEMENTE ENLAZADA')
    while True:
        print('\n1. Mostrar historial\n2. Agregar canción\n3. Avanzar\n4. Retroceder'
              '\n5. Buscar canción\n6. Eliminar canción\n7. Salir')
        opcion = input('Elegí una opción: ').strip()
        if opcion == '1':
            mostrar(historial)
        elif opcion == '2':
            titulo = input('Título: ')
            artista = input('Artista: ')
            try:
                historial.agregar_cancion(titulo, artista)
                print('Canción agregada al final.')
            except ValueError as error:
                print('Error:', error)
            mostrar(historial)
        elif opcion == '3':
            if historial.avanzar():
                print('Avanzaste a:', historial.actual.titulo)
            else:
                print('No hay una canción siguiente.')
            mostrar(historial)
        elif opcion == '4':
            if historial.retroceder():
                print('Retrocediste a:', historial.actual.titulo)
            else:
                print('No hay una canción anterior.')
            mostrar(historial)
        elif opcion == '5':
            titulo = input('Título a buscar: ')
            nodo = historial.buscar_cancion(titulo)
            print(f'Encontrada: {nodo.titulo} - {nodo.artista}' if nodo else 'No encontrada.')
        elif opcion == '6':
            titulo = input('Título a eliminar: ')
            print('Eliminación exitosa.' if historial.eliminar_cancion(titulo)
                  else 'No se encontró la canción.')
            mostrar(historial)
        elif opcion == '7':
            print('Fin de la demostración.')
            break
        else:
            print('Opción inválida. Elegí del 1 al 7.')


if __name__ == '__main__':
    main()
