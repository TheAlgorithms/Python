# Recorrido de Árbol Binario

## Resumen

La combinación de árboles binarios como estructuras de datos y el recorrido como algoritmo se relaciona con problemas clásicos, ya sea directa o indirectamente.

> Si puedes comprender el recorrido de árboles binarios, el recorrido de otros árboles complicados le resultará fácil.


Las siguientes son algunas formas comunes de atravesar árboles.

- Recorrido de Profundidad Primero (RPP): En-orden, Pre-orden, Post-orden DFS

- Recorrido de Orden a Nivel o Recorrido de Anchura Primero (RAP) BFS

Hay aplicaciones para RPP y RAP

La pila (stack) se puede utilizar para simplificar el proceso de recorrido RPP. Además, dado que el árbol es una estructura de datos recursiva, la recursión y la pila son dos puntos clave para RPP.

La pila se puede utilizar para simplificar el proceso del recorrido RPP. Además, dado que el árbol es una estructura de datos recursiva, la recursión y la pila son dos puntos clave para RPP.

Gráfico para RPP:

![binary-tree-traversal-dfs](https://tva1.sinaimg.cn/large/007S8ZIlly1ghluhzhynsg30dw0dw3yl.gif)

The key point of BFS is how to determine whether the traversal of each level has been completed. The answer is to use a variable as a flag to represent the end of the traversal of current level.

El punto clave de RAP es cómo determinar si se ha completado el recorrido de cada nivel. La respuesta es usar una variable como señal para representar el final del recorrido del nivel actual.

## Recorrido Pre-Orden

El orden de recorrido del recorrido pre-orden es `raíz-izquierda-derecha`.

Algoritmo Pre-orden

1. Visite el nodo raíz y empujelo en una pila.

2. Pop a node from the stack, and push its right and left child node into the stack respectively.

2. Abra un nodo de la pila e empuje sus nodos secundarios derecho e izquierdo en la pila, respectivamente.

3. Repita el paso 2.

Conclusión: este problema involucra la estructura de datos recursiva clásica (es decir, un árbol binario), y el algoritmo anterior demuestra cómo se puede llegar a una solución simplificada mediante el uso de una pila.

Si observa el panorama general, encontrará que el proceso de recorrido es el siguiente. `Visite los subárboles de la izquierda, respectivamente, de arriba a abajo, y visite los subárboles de la derecha, respectivamente, de abajo hacia arriba`. Si vamos a implementarlo desde esta perspectiva, las cosas serán algo diferentes. Para la parte `de arriba a abajo` podemos simplemente usar la recursividad, y para la parte `de abajo a arriba` podemos recurrir a la pila.


## Recorrido En-Orden


El orden de recorrido del recorrido en-orden es `izquierda-raíz-derecha`.

Entonces, el nodo raíz no se imprime primero. Las cosas se están complicando un poco aquí.

Algoritmo en-orden

1. Visite la raíz y empújela en una pila.

2. Si hay un nodo secundario izquierdo, empujelo en la pila. Repita este proceso hasta llegar a un nodo hoja.

     > En este punto, el nodo raíz y todos los nodos izquierdos están en la pila.

3. Comience a abrir nodos de la pila. Si un nodo tiene un nodo secundario derecho, empuje el nodo secundario en la pila. Repita el paso 2.

Vale la pena señalar que el recorrido en-orden de un árbol de búsqueda binario (BST) es una matriz ordenada, que es útil para encontrar soluciones simplificadas para algunos problemas.


## Recorrido Post-Orden

El orden de recorrido del recorrido post-orden es `izquierda-derecha-raíz`.

Este es un pequeño desafío. Se merece la etiqueta `dura` de LeetCode.

En este caso, el nodo raíz no se imprime como el primero sino como el último. Una manera astuta de hacerlo es:

Registre si el nodo actual ha sido visitado. Si 1) es un nodo hoja o 2) se han recorrido sus subárboles izquierdo y derecho, entonces se puede abrir de la pila.

En cuanto es `1) un nodo hoja`, puede saber fácilmente si un nodo es una hoja si tanto su izquierda como su derecha son `nulos`.

En cuanto a `2) ambos subárboles izquierdo y derecho han sido recorridos`, solo necesitamos una variable para registrar si un nodo ha sido visitado o no. En el peor de los casos, necesitamos registrar el estado de cada nodo y la complejidad del espacio es `O(n)`. Pero si lo piensa, como estamos usando una pila y comenzamos a imprimir el resultado de los nodos hoja, tiene sentido que solo registremos el estado del nodo actual que estamos abriendo en la pila, reduciendo la complejidad del espacio a `O(1)`.

## Recorrido de Orden a Nivel

The key point of level order traversal is how do we know whether the traversal of each level is done. The answer is that we use a variable as a flag representing the end of the traversal of the current level.

El punto clave del recorrido del orden a nivel es cómo sabemos si se realizó el recorrido de cada nivel. La respuesta es que usamos una variable como señal que representa el final del recorrido del nivel actual.

![binary-tree-traversal-bfs](https://tva1.sinaimg.cn/large/007S8ZIlly1ghlui1tpoug30dw0dw3yl.gif)

Algoritmo Orden de Nivel

1. Visite el nodo raíz, encolarlo en una cola FIFO(primero en entrar, primero en salir), coloque en la cola un indicador especial (estamos usando `nulo` aquí).

2. Decolar un nodo.

3. Si el nodo es igual a `nulo`, significa que se han visitado todos los nodos del nivel actual. Si la cola está vacía, no hacemos nada. O bien ponemos otro `nulo`.

4. Si el nodo no es `nulo`, lo que significa que el recorrido del nivel actual aún no ha terminado, encolamos en cola su subárbol izquierdo y subárbol derecho respectivamente.

## Marcado bicolar

Sabemos que hay una marca tricolor en el algoritmo de recolección de basura, que funciona como se describe a continuación.


- El color blanco representa "no visitado".

- El color gris representa "no todos los nodos secundarios visitados".

- El color negro representa "todos los nodos secundarios visitados".

Iluminado por el marcado tricolor, se puede inventar un método de marcado bicolor para resolver los tres problemas transversales con una solución.

La idea central es la siguiente:

- Usar un color para marcar si un nodo ha sido visitado o no. Los nodos aún por visitar están marcados en blanco y los nodos visitados están marcados en gris.

- Si estamos visitando un nodo blanco, conviértalo en gris y empuje su nodo secundario derecho, él mismo y su nodo secundario izquierdo en la pila, respectivamente.

- Si estamos visitando un nodo gris, imprímalo.

La implementación de algoritmos transversales de pedido previo y posterior se puede realizar fácilmente cambiando el orden de inserción de los nodos secundarios en la pila.

Referencia: [LeetCode](https://github.com/azl397985856/leetcode/blob/master/thinkings/binary-tree-traversal.en.md)