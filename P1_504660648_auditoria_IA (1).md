# Auditoría de IA — Proyecto 1: historial musical

## 1. Prompt de una consulta nueva de revisión (texto íntegro)

> Estoy desarrollando un proyecto universitario de Estructuras de Datos en Python. El caso consiste en implementar un historial de canciones utilizando una lista doblemente enlazada.
> 
> Tengo una clase llamada `NodoCancion`, con los atributos `titulo`, `artista`, `anterior` y `siguiente`. También tengo una clase `HistorialMusical`, que utiliza las referencias `primera`, `ultima` y `actual` para administrar las canciones.
> 
> Necesito implementar el método `eliminar_cancion(self, titulo)` con las siguientes condiciones:
> 
> 1. Buscar la canción por su título y devolver `False` si no existe.
> 2. Permitir eliminar una canción ubicada al inicio, en medio o al final de la lista.
> 3. Actualizar correctamente las referencias `anterior` y `siguiente` de los nodos vecinos.
> 4. Actualizar las referencias `primera` y `ultima` cuando sea necesario.
> 5. Si se elimina la canción actual, seleccionar la siguiente canción disponible. Si no existe, seleccionar la anterior.
> 6. Si se elimina la única canción, dejar el historial vacío.
> 7. Desconectar las referencias del nodo eliminado y devolver `True` cuando la operación sea exitosa.
> 
> Quiero que el método utilice únicamente las referencias propias de una lista doblemente enlazada, sin convertirla en una lista tradicional de Python.
> 
> Por favor, proporcioná el código del método en Python, compatible con la estructura descrita, y una explicación breve de cómo funciona la actualización de los enlaces.

## 2. Respuesta de IA a esa consulta (texto íntegro)

Podés implementar el método de la siguiente manera, aprovechando las referencias anterior y siguiente de cada nodo:

```python
    def eliminar_cancion(self, titulo):
        nodo = self.buscar_cancion(titulo)

        if nodo is None:
            return False

        anterior = nodo.anterior
        siguiente = nodo.siguiente

        if anterior is None:
            self.primera = siguiente
        else:
            anterior.siguiente = siguiente

        if siguiente is None:
            self.ultima = anterior
        else:
            siguiente.anterior = anterior

        if self.actual is nodo:
            self.actual = siguiente if siguiente is not None else anterior

        nodo.anterior = None
        nodo.siguiente = None
        return True
```

Primero se busca el nodo por título. Si no se encuentra, se devuelve `False` sin modificar el historial. Si existe, se guardan los vecinos para actualizar sus enlaces: el nodo anterior apunta al siguiente y el siguiente apunta al anterior. Cuando el eliminado es el primero o el último, se actualizan `primera` o `ultima` respectivamente. Si era la canción actual, se elige la siguiente; si no hay siguiente, se toma la anterior. Si era la única, esas referencias quedan en `None`. Por último se desconecta el nodo y se devuelve `True`.

Este código supone que `buscar_cancion(titulo)` devuelve el nodo encontrado o `None`, tal como ocurre en tu implementación. No necesita convertir el historial en una lista de Python.

## 3. Revisión del método `eliminar_cancion` en la versión entregada

Se revisó la implementación del archivo `p1_504660648_Estructura.py`, siguiendo su orden:

1. `nodo = self.buscar_cancion(titulo)`: localiza el primer nodo cuyo título coincide. La búsqueda elimina espacios al comienzo y al final y no distingue mayúsculas y minúsculas. Si existen títulos repetidos, se elimina la primera coincidencia.
2. `if nodo is None: return False`: detiene la operación cuando el título no está en la lista. Así no se alteran referencias por una eliminación inexistente.
3. `anterior = nodo.anterior` y `siguiente = nodo.siguiente`: guarda ambos vecinos antes de reconectar, evitando perder las referencias necesarias.
4. `if anterior is None`: significa que el nodo está al inicio; se actualiza `primera`. Si hay un nodo anterior, su `siguiente` pasa a apuntar al vecino posterior del eliminado.
5. `if siguiente is None`: significa que el nodo está al final; se actualiza `ultima`. Si hay un nodo siguiente, su `anterior` pasa a apuntar al vecino previo del eliminado.
6. `if self.actual is nodo`: si se eliminó la canción seleccionada, se elige la siguiente si existe; si no, la anterior. Cuando se elimina la única canción, el valor pasa a `None`.
7. `nodo.anterior = None` y `nodo.siguiente = None`: separa el nodo eliminado de sus vecinos.
8. `return True`: confirma que encontró y eliminó un nodo.

## 4. Casos de borde y condiciones de parada

El archivo `p1_504660648_demo.py` utiliza aserciones para verificar el comportamiento. Se ejecutó la demo en Python y terminó con el mensaje `Todas las comprobaciones terminaron correctamente.` Se comprobaron los siguientes escenarios incluidos en ella:

| Escenario | Comprobación y resultado |
| --- | --- |
| Historial vacío | Avanzar y retroceder devuelven `False`; buscar devuelve `None`; eliminar devuelve `False`. Correcto. |
| Una sola canción | `primera`, `ultima` y `actual` apuntan al mismo nodo; no se puede avanzar ni retroceder. Correcto. |
| Varias canciones | Los enlaces se recorren de inicio a fin y `verificar_enlaces` comprueba las referencias recíprocas. Correcto. |
| Búsqueda por título | Se encuentra `" canción b "` sin importar espacios externos ni diferencias de mayúsculas. Correcto. |
| Eliminar un nodo intermedio y actual | Al eliminar B, la canción actual pasa a C, los enlaces vecinos se reconectan y el nodo eliminado se separa. Correcto. |
| Eliminar la primera y luego la única restante | Se actualizan `primera`, `ultima` y `actual` según corresponde hasta vaciar el historial. Correcto. |
| Reutilizar el historial y eliminar la última canción actual | Se vuelve a insertar y al eliminar E la canción actual regresa a D. Correcto. |
| Título vacío | Se rechaza mediante `ValueError`. Correcto. |

**Condiciones de parada:** el recorrido termina al llegar a un nodo `None`, porque no es una lista circular. `avanzar` y `retroceder` terminan devolviendo `False` cuando no existe un vecino en la dirección solicitada. `buscar_cancion` deja de buscar en la primera coincidencia o al finalizar el recorrido.

## 5. Hallazgos y correcciones

En las comprobaciones ejecutadas **no se encontraron fallos** en los casos cubiertos por la demo y no fue necesario cambiar el código para superarlas. Esto no equivale a demostrar que cualquier entrada posible esté cubierta. Por ejemplo, el historial permite canciones con el mismo título y la búsqueda/eliminación se basan solo en el título; por ello, entre títulos repetidos se toma la primera coincidencia. Es un comportamiento del diseño actual que convendría aclarar en una versión ampliada.

**Comparación de la nueva respuesta con el proyecto:** la solución de IA de la sección 2 mantiene la misma secuencia y condiciones que el método que está en GitHub. Las diferencias son de comentarios y estilo (por ejemplo, elegir siguiente/anterior con una expresión condicional). No se identificaron errores lógicos que obligaran a modificar el código del repositorio. Esta comparación se refiere a la consulta nueva, no permite saber si el código histórico provino de la misma respuesta.

## 6. Evidencia de ejecución

La demo se ejecutó con los archivos del repositorio y finalizó sin fallos en las aserciones. Mensaje final: `Todas las comprobaciones terminaron correctamente.`

## 7. Aclaración sobre el origen del registro

La consulta de la sección 1 y la respuesta de la sección 2 se redactaron en esta conversación como **nueva interacción para fines de revisión**. No son un registro recuperado de la generación inicial del método. Si la consigna exige precisamente aquella conversación inicial, sigue siendo necesario recuperarla o aclarar ante el profesor que no se conservó. No se inventó una fecha ni un historial previo.
