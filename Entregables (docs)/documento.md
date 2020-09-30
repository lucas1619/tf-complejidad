![enter image description here](https://www.laureate.net/wp-content/uploads/2019/03/10-UPC-Universidad-Peruana-de-Ciencias-Aplicadas.png)
<center><b>Complejidad Algorítmica – CC41</b></center> <br>
<center><b>Trabajo Parcial</b></center> <br>
<center> Carrera de Ingeniería de Software y Ciencias de la computación</center>
<center> Sección: ABCD </center>
<br>

# Alumnos:

 - u201711783 - Villegas Celis Carolina Milagros
 - u201914955 - Mendez Pastor Brigitte Melody
 - u201917621 - Moreno Olivos Lucas Alejandro
 
 
# Introducción

- El encontrar un camino más corto para llegar de un lugar a otro es algo muy importante para las empresas de delivery ahora, mientras más rápido llegas, más clientes obtienes; asimismo, en los juegos como los laberintos, el encontrar el camino hacia el final es muy importante por si estás jugando con otros compañeros y el que encuentra el camino gana, nuestro presente trabajo se trata del juego Quoridor, un juego que tiene como objetivo llegar primero hasta la base del rival. Además, en cada turno se debe escoger entre colocar dificultades como muros o avanzar. Dicho juego lo vamos a tratar como un problema de "Path Finding" donde se busca encontrar la ruta más corta entre dos nodos de un grafo con algoritmos eficientes considerando el tiempo de ejecución, el espacio en disco y la complejidad del mismo.

# Marco Teórico

## Complejidad Algorítmica

La complejidad algorítmica es una métrica que nos ayuda a describir el comportamiento de un algoritmo en términos de tiempo de ejecución y la memoria que requiere. Un problema puede tener distintas soluciones, pero más importante que hallar una solución es que esta sea viable y eficaz, el medir la complejidad de los algoritmos nos ayuda a saber cuál es el que debemos implementar.
Al tiempo de ejecución se le llama complejidad temporal y a la memoria requerida para solucionar un problema se le llama complejidad espacial, ambos dependen del tamaño del problema. La complejidad algorítmica no depende siempre del tiempo de ejecución, la cantidad de memoria consumida, el sistema en donde se corra el algoritmo y el estilo de programación implementado, sino del número de instrucciones necesarias para resolver el problema. Sin embargo, esto no siempre es así, los algoritmos de búsqueda y ordenamiento son una prueba de ello pues estos iteran hasta llegar a la solución deseada, estos algoritmos presentan el mejor y peor caso, por ejemplo: el mejor caso para el algoritmo de búsqueda sería cuando el número a buscar sea el primero del arreglo y el peor cuando este sea el último del arreglo. En la notación, se suele emplear la **contracción**, por ejemplo un algoritmo de complejidad Θ(3n² + 5n + 9) se reduce a Θ(n²), a continuación una tabla que muestra los órdenes de complejidad más comunes:
 
![alt text](https://miro.medium.com/max/390/1*A32Od1e1ZXSSGwuSP6N7vg.png)

## Pathfinding
Se le denomina de esta manera al área de inteligencia artificial que tiene como objetivo encontrar el mejor camino de un 
punto a otro en mapas representados digitalmente . Estos algoritmos tienen que definir por dónde dirigirse, basados en la información
que se tiene del ambiente. Existen diversos tipos de algoritmos como A*, ACO, JPS, etc que buscan reducir el tiempo de búsqueda y los
recursos utilizados, con el objetivo de hacer más eficiente la tarea. En este proyecto usaremos algunos de ellos y compararemos su eficiencia.

# Estado del arte

## Algoritmo Ant Colony Optimization(ACO)
 
El algoritmo de ACO fue propuesto por un científico italiano en el año 1992. La primera versión del algoritmo fue llamada Ant Systems 
La inspiración del algoritmo viene de la interacción y la coordinación de los organismos para dejar en cada acción un rastro que puede 
ser usado para detectar la ruta más eficiente haciendo que los otros organismos modifiquen su ruta actual como se puede ver en el caso de las colonias de hormigas.
 

### Cómo funciona este algoritmo:

El algoritmo se puede ser representado a través de gráficos ponderados donde la colonia de hormigas y la fuente de alimento actúan como vértices (o nodos); los caminos sirven como bordes y los valores de feromonas son los pesos asociados con los bordes.Sea la gráfica G = (V, E) donde V, E son los bordes y los vértices de la gráfica. Los vértices según nuestra consideración son Vs (vértice de origen - colonia de hormigas) y Vd (vértice de destino - origen de alimento).

Los dos bordes son E1  y E2 con longitudes L1 y L2 asignadas a cada uno. Ahora, se puede suponer que los valores de feromonas asociados (indicativos de su fuerza) son R1 y R2 para los vértices E1 y E2 respectivamente. Por lo tanto, para cada hormiga, 
la probabilidad inicial de selección de ruta (entre E1 y E2) se puede expresar de la siguiente manera:

![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20200430233709/ACO1.png)

Si R1> R2, la probabilidad de elegir E1 es mayor y viceversa. Ahora, mientras regresa por esta ruta más corta, digamos Ei, el valor de las feromonas se actualiza para la ruta correspondiente. La actualización se realiza en función de la longitud de las rutas y la tasa de evaporación de la feromona. Entonces, la actualización se puede realizar paso a paso de la siguiente manera:

1) De acuerdo con la longitud del camino
 ![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20200430233741/ACO2.png)
 En la actualización anterior, i = 1, 2 y 'K' sirven como parámetro del modelo. Además, la actualización depende de la longitud de la ruta. Cuanto más corto sea el camino, mayor será la feromona agregada.

2) De acuerdo con la tasa de evaporación de la feromona.
 ![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20200430233759/ACO3.png)
  El parámetro 'v' pertenece al intervalo (0, 1] que regula la evaporación de feromonas. Además, i = 1, 2.
En cada iteración, todas las hormigas se colocan en el vértice de origen Vs (colonia de hormigas). Posteriormente, las hormigas se mueven de Vs a Vd (fuente de alimento) siguiendo el paso 1. A continuación, todas las hormigas realizan su viaje de regreso y refuerzan el camino elegido según el paso.

### Pseudocódigo:

![alt text](https://fotos.subefotos.com/724ab5e5fa7a71b87658d5dc8d383a94o.png)

## Algoritmo A* 
Es una de las mejores técnicas para búsqueda de rutas y recorridos de grafos. A diferencia de otros, este es un algoritmo inteligente, muchos juegos utilizan este algoritmo para encontrar el camino más corto de forma __eficiente__ , cualidad que es altamente importante para este trabajo. Usaremos este algoritmo para poder encontrar el camino más corto a la meta y lo modificaremos de acuerdo a las condiciones que considera el juego **Quoridor**, de acuerdo al juego, el tablero se representará por un grafo.
 
### A continuación la explicación de este algoritmo:
 
Tenemos un grafo con múltiples nodos, y queremos llegar a un nodo específico desde el primer nodo lo más rápido posible.
 
Lo que hace el Algoritmo A* es que en cada paso elige un nodo de acuerdo a un valor __f__ que es la suma de __g__ y __h__, en cada paso elige el nodo con el menor valor de __f__ y continua el camino:
 
![alt text](https://latex.codecogs.com/gif.latex?f%28n%29%20%3D%20g%28n%29%20&plus;%20h%28n%29)
 
* n :     nodo previo en el camino
 
* g(n) :  costo del camino del nodo del inicio hasta n
 
* h(n) :  una heurística que estima el costo del camino más corto desde n hasta el nodo deseado
 
Consideremos que el grafo es este:
 
<a href="https://imgbb.com/"><img src="https://i.ibb.co/db1H6Hp/graph.png" alt="graph" border="0"></a>
 
Los números escritos en azul en las aristas representan la distancia entre los nodos y los números escritos con rojo representan el valor de la heurística
 
El algoritmo A* usa está formula  ![alt text](https://latex.codecogs.com/gif.latex?f%28n%29%20%3D%20g%28n%29%20&plus;%20h%28n%29)  para encontrar el camino más corto.
 
**Ejemplo: Queremos encontrar el camino más corto entre A y J**
 
**Nodo de inicio es A**
 
A se relaciona con B y F
 
Calcularemos el F(B) y el F(F)
 
F(B) = 6 + 8 = 14
 
F(F) = 3 + 6 = 9
 
El menor es F(F), F será nuestro nuevo nodo de inicio
 
**Nodo de inicio es F**
 
F se relaciona con G y H
 
Calcularemos el F(G) y el F(H)
 
F(G) = 4 + 5 = 9 ----> 4 = 3 + 1 ---> COSTO DEL CAMINO HASTA AHORA
 
F(H) = 10 + 3 = 13 ----> 10 = 3 + 7 ---> COSTO DEL CAMINO HASTA AHORA
 
El menor es F(G), G será nuestro nuevo nodo de inicio
 
**Nodo de inicio es G**
 
G solo se relaciona con I
 
Calcularemos el F(I)
 
F(I) = 7 + 1 = 8 ----> 7 = 3 + 1 + 3  ---> COSTO DEL CAMINO HASTA AHORA
 
I será el nuevo nodo de inicio
 
**Nodo de inicio es I**
 
I se relaciona con E, H y J
 
Calcularemos el F(E), el F(H) y el F(J)
 
F(E) = 12 + 3 = 15 ----> 12 = 3 + 1 + 3 + 5 ---> COSTO DEL CAMINO HASTA AHORA
 
F(H) = 9 + 3 = 12 ----> 10 = 3 + 1 + 3 + 2 ---> COSTO DEL CAMINO HASTA AHORA
 
F(J) = 10 + 0 = 10 ----> 10 = 3 + 1 + 3 + 3 ---> COSTO DEL CAMINO HASTA AHORA
 
El menor es F(J), J será nuestro nuevo nodo de inicio
 
**Como queriamos llegar al nodo J paramos ahí.**
 
Así quedaría el recorrido:
 
<a href="https://imgbb.com/"><img src="https://i.ibb.co/dDtthQY/path-graph.png" alt="path-graph" border="0"></a>
 
El camino fue **A F G I J**
 
### Complejidad del algoritmo:
Puede llevarnos viajar por todo el borde del grafo desde el nodo origen hasta el nodo que deseemos. Entonces, en el peor de los casos su complejidad es
 
![alt text](https://latex.codecogs.com/gif.latex?O%28E%29)

* E: Número de aristas en el gráfico 

# Metodología
La metodología que usamos para resolver este problema se divide en tres partes:

1. Investigación

2. Desarrollo

3. Tests y Experimentos

### Investigación:
Para dar inicio a la investigación, primero indagamos acerca del problema, debido a ello pudimos observar que debíamos hacer uso de algoritmos relacionados a la busqueda del camino más corto. Usaremos estos algoritmos para el movimiento de los peones a través de los obstáculos  o ,en otras palabras, Pathfinding. Asimismo, buscamos algoritmos que podrían ser útiles para nuestro trabajo, los que encontramos fueron A*, Dijkstra y Bellman Ford. Además, se hizo uso de la libreria pygames, para la parte gráfica del juego (representación del tablero y peones).


### Desarrollo:

En primer lugar, implementamos una lista doblemente enlazada, lo siguiente fue implementar un grafo, el cual era la combinación de un vector de listas doblemente enlazadas y dentro de ello, una función que permitía que las conexiones entre nodos se almacenen como listas de adyacencia. Elegimos implementarlo de esta manera, debido a que deseamos un acceso constante a los nodos, eso lo obtenemos del vector de listas doblemente enlazadas y además, un almacenado dinámico a sus adyacentes y la lista doblemente enlazada permite ello. De tal manera, que las operaciones de acceso e insertado en nuestro juego sean de O(1)

En segundo lugar, nuestro  objetivo fue implementar los algoritmos de path-finding. Con el proposito de avanzar el trabajo de manera más rápida, al ser un grupo de 3 integrantes, cada integrante implemento uno de los algoritmos de path-finding de acuerdo al grafo construido previamente. Al testear que los algoritmos funcionaban y encuentraban las rutas adecuadas pasamos al siguiente paso.

En tercer lugar, separamos el código de manera estructurada y ordenada, debido a que cada uno trabajo por su cuenta, el código estaba desordenado y decidimos ordenarlo en clases, las clases que identificamos fueron:

- Clase Lista Doblemente Enlazada (clase que contiene la implementación de la lista)
- Clase Tablero (clase que contiene la implementación del grafo entre otras funcionalidades del mismo)
- Clase Jugador (clase que contiene todas las funcionalidades del peon del juego)
- Clase Pensamiento (clase que contiene los algoritmos que seguirán los peones)
- Clase Quoridor (clase que contiene todo el juego)

En cuarto lugar, implementamos el pensamiento del jugador, ejemplo: cuando saltar, cuando cambiar de ruta, etc. 

En quinto lugar, implementamos la parte gráfica con la ayuda de la librería pygames. 

En último lugar, testeamos el juego de distintas maneras, lo cual nos confirmo que los algoritmos funcionaban de manera correcta 

### Tests y Experimentos:

La forma en la cual compararemos los algoritmos mencionados en la parte de investigación dentro del juego Quoridor es hacerlos competir entre ellos. Estas partidas recibiran como entrada 2 parámetros. El primero será el tamaño del tablero y el segundo el tiempo máximo que tendran los algoritmos por análisis del tablero. Recordemos que cada algoritmo tendra que hacer 2 análisis, el primero del jugador rival y el segundo de el mismo. 

Para la primera entrada de tablero tomaremos los valores de la siguiente lista: 
* 3
* 9
* 20
* 100
* 10000

Mientras que para la segunda entrada tomaremos los valores de la siguiente lista: 
* 10ms
* 50ms
* 100ms
* 500ms
* 1s
