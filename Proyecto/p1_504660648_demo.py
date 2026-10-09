from p1_504660648_Estructura import HistorialMusical


def verificar_enlaces(historial):
    anterior = None
    encontro_actual = False

    for nodo in historial.recorrer():
        assert nodo.anterior is anterior

        if anterior is not None:
            assert anterior.siguiente is nodo

        if nodo is historial.actual:
            encontro_actual = True

        anterior = nodo

    assert anterior is historial.ultima

    if historial.primera is None:
        assert historial.ultima is None
        assert historial.actual is None
    else:
        assert historial.primera.anterior is None
        assert historial.ultima.siguiente is None
        assert encontro_actual


def main():
    historial = HistorialMusical()

    # Historial vacío y canción inexistente.
    assert historial.avanzar() is False
    assert historial.retroceder() is False
    assert historial.buscar_cancion("Inexistente") is None
    assert historial.eliminar_cancion("Inexistente") is False
    verificar_enlaces(historial)
    print("Correcto: historial vacío.")

    # Un único elemento.
    historial.agregar_cancion("Canción A", "Artista A")
    assert historial.actual is historial.primera
    assert historial.primera is historial.ultima
    assert historial.avanzar() is False
    assert historial.retroceder() is False
    verificar_enlaces(historial)
    print("Correcto: una sola canción.")

    # Varias canciones.
    historial.agregar_cancion("Canción B", "Artista B")
    historial.agregar_cancion("Canción C", "Artista C")
    verificar_enlaces(historial)

    print("\nHistorial:")
    for nodo in historial.recorrer():
        print(f"{nodo.titulo} - {nodo.artista}")

    # Búsqueda y navegación en ambos sentidos.
    assert historial.buscar_cancion(" canción b ").titulo == "Canción B"
    assert historial.buscar_cancion("Inexistente") is None
    assert historial.avanzar() is True
    assert historial.actual.titulo == "Canción B"
    assert historial.avanzar() is True
    assert historial.actual.titulo == "Canción C"
    assert historial.avanzar() is False
    assert historial.retroceder() is True
    assert historial.actual.titulo == "Canción B"
    print("\nCorrecto: búsqueda y navegación.")

    # Eliminar la canción intermedia y actual.
    eliminada = historial.actual
    assert historial.eliminar_cancion("Canción B") is True
    assert historial.actual.titulo == "Canción C"
    assert eliminada.anterior is None
    assert eliminada.siguiente is None
    verificar_enlaces(historial)
    print("Correcto: eliminación de la canción intermedia.")

    # Eliminar la primera.
    assert historial.eliminar_cancion("Canción A") is True
    assert historial.primera.titulo == "Canción C"
    verificar_enlaces(historial)

    # Eliminar la única restante.
    assert historial.eliminar_cancion("Canción C") is True
    verificar_enlaces(historial)
    print("Correcto: eliminación hasta quedar vacío.")

    # Volver a utilizar el historial después de vaciarlo.
    historial.agregar_cancion("Canción D", "Artista D")
    historial.agregar_cancion("Canción E", "Artista E")
    assert historial.avanzar() is True

    # Eliminar la última y actual: regresar a la anterior.
    assert historial.eliminar_cancion("Canción E") is True
    assert historial.actual.titulo == "Canción D"
    verificar_enlaces(historial)
    print("Correcto: eliminación de la última canción.")

    # Rechazar datos vacíos.
    try:
        historial.agregar_cancion(" ", "Artista")
    except ValueError:
        print("Correcto: rechazo de título vacío.")
    else:
        raise AssertionError("Se aceptó un título vacío.")

    print("\nTodas las comprobaciones terminaron correctamente.")


if __name__ == "__main__":
    main()