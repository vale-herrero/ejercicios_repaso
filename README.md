# ejercicios_repaso

Pregunta 1 (2 puntos)
 
Nick Fury, líder de la agencia S.H.I.E.L.D., tiene la difícil tarea de decidir qué vengador asignará a cada nueva misión (por ahora considere que solo se asignará un superhéroe por cada misión). Teniendo en cuenta el listado de superhéroes es el siguiente:
 
Nombre
Iron Man
The incredible Hulk
Khan
Thor
Captain América
Capitana Marvel
Ant-Man
Nick Fury
The Winter Soldier
 
Nos solicita desarrollar un árbol de decisión para resolver esta tarea con los siguientes requerimientos:
 
cada nodo hoja del árbol debe ser un superhéroe y en cada nodo intermedio inclusive la raíz debe haber una pregunta. Si la respuesta es sí, se debe desplazar hacia el subárbol izquierdo, si es no al subárbol derecho. Además, debéis desarrollar una función que determine el superhéroe para una misión;
Khan es ideal para misiones intergalácticas en equipo;
Ant-Man es excelente en misiones de recuperación donde sea necesario no se detectado;
para misiones de destrucción Hulk es una excelente opción;
el Capitán América es un supersoldado de ética incorruptible ideal para comandar misiones de defensa y de recuperación;
Capitana Marvel es muy poderosa y puede viajar por las distintas galaxias;
Khan es muy hábil y puede ser útil para varias misiones;
para misiones de recuperación donde requiera infiltrarse con personas del lugar, The Winter Soldier es la persona indicada;
Iron Man es un líder para planear misiones de defensa, además es un genio y domina el manejo de tecnología avanzada, cuenta con un traje muy poderoso;
cuando se requiere elegir cuál será la próxima acción para tomar y moverse rápidamente de un lugar a otro, es el propio Nick Fury es la opción más lógica;
Thor tiene el poder para destruir ejércitos completos;
no se debe utilizar árbol balanceado.
Pregunta 2 (2 puntos)
 
El gran almirante del MCU Khan “El Conquistador” es el estratega del multiverso y normalmente se encuentra desbordado de pedidos de sugerencia de cómo actuar por las variantes de el mismo de las diferentes épocas y Multiversos. Para lo cual nos solicita desarrollar un algoritmo que le permita atender los pedidos de ayuda de acuerdo con la prioridad de los mismo en base a los siguientes requerimientos:
 
se deben contemplar tres niveles de prioridad para la cola;
 
cada pedido de sugerencia cuenta con la siguiente información: nombre del “Khan” solicitante, multiverso en el que se encuentra o el más próximo y descripción del pedido;
 
aquellos pedidos que provengan del “Gran Conquistador”, del universo de 616 o la descripción mencione a “El que permanece” tendrán la mayor prioridad;
 
si el pedido es del “Khan que todo lo sabe” o la descripción menciona “Carnicero de Dioses” o universo “838” tendrán prioridad media;
 
el resto de los pedidos serán de prioridad baja;
 
realizar la atención de la cola almacenando los pedidos de mayor prioridad en una pila llamada “bitácora” para revisión y seguimiento;
 
luego de cada atención se podrá agregar un pedido a la cola.
Pregunta 3 (2 puntos)
 
Kamala Khan alias Ms. Marvel es una adolescente Musulmana Pakistaní-estadounidense de Nueva Jersey. En el MCU tiene un linaje mutante latente activado unos misteriosos anillos que le dan una polimorfa con la capacidad de estirar su cuerpo de casi cualquier forma imaginable. Kamala era una gran fan de los superhéroes, especialmente de Carol Danvers, la antigua Ms. Marvel y por eso se ha convertido en una experta en redes sociales, pero nos ha pedido ayuda para implementar un grafo social y los algoritmos necesarios para atender los siguientes requerimientos:
 
cargar superhéroes de la siguiente tabla como vértices (puntos o nodos con los que están conformado los grafos. Llamaremos grado de un vértice, al número de aristas de las que es extremo) del grafo;
 
 
TWITTER
Iron Man
The increíble Hulk
Khan
Thor
Captain América
Ant-Man
Nick Fury
The Winter Soldier
Iron Man
 
75
40
16
80
20
99
23
The increíble Hulk
75
 
50
67
79
38
99
41
Khan
40
50
 
17
75
52
85
28
Thor
16
67
17
 
11
50
90
36
Captain América
80
79
75
11
 
26
12
56
Ant-Man
20
38
52
50
26
 
55
61
Nick Fury
99
99
85
90
12
55
 
10
The Winter Soldier
23
41
28
36
56
61
10
 
 
 
INSTAGRAM
Iron Man
The increíble Hulk
Khan
Thor
Captain América
Ant-Man
Nick Fury
The Winter Soldier
Iron Man
 
61
44
66
56
74
11
65
The increíble Hulk
12
 
47
41
12
38
99
41
Khan
41
23
 
45
12
89
42
14
Thor
12
69
11
 
12
50
78
63
Captain América
89
19
72
11
 
26
12
56
Ant-Man
72
34
21
65
12
 
78
41
Nick Fury
12
87
35
99
42
15
 
10
The Winter Soldier
33
41
24
61
45
41
11
 
 
 
 
cargar estos superhéroes con las siguientes etiquetas: Twitter, Instagram respectivamente, que representan si la persona del vértice origen sigue o es amigo de la persona del vértice destino;
 
hallar el árbol de expansión máximo para cada red social –considere el grafo como no dirigido para este punto–, es decir que las conexiones deben ser las de mayor peso –ósea el que tenga mayor interacción–; para lo cual, si desea utilizar Prim o Kruskal sin modificar el código, puede determinar la arista (relación entre dos vértices de un grafo) de mayor peso y cuando aplique este algoritmo, debe que considerar el peso de cada arista será la arista de mayor peso menos el peso de la arista;
 
determine si es posible conectar la persona Capitana Marvel con Nick Fury a través de la red social Twitter;
 
determine si es posible conectar la persona The Winter Soldier con Iron Man a través de cualquier red social;
 
indique a todas las personas que sigue a través de su red de Instagram Thor.
Pregunta 4 (2 puntos)
 
Nick Fury se encuentra en los cuarteles generales de S.H.I.E.L.D. y debe visitar a varios superhéroes para convencerlos de unirse para formar un grupo de vengadores, dado que es un asunto de suma importancia nos solicita implementar un algoritmo que permita determinar el recorrido de menor distancia –el menor posible, no importa que sea el óptimo– y terminar dicho recorrido de vuelta en los cuarteles (solo se puede pasar una vez por cada lugar).
 
Considere los siguientes superhéroes: S.H.I.E.L.D.
 
Iron Man
The increíble Hulk
Khan
Thor
Captain América
Ant-Man
Nick Fury
The Winter Soldier
 
 
las distancias entre la localización de cada superhéroe están cargadas en la siguiente matriz:
 
 
Iron Man
The increíble Hulk
Khan
Thor
Captain América
Ant-Man
Nick Fury
The Winter Soldier
Iron Man
 
675
400
166
809
720
399
233
The increíble Hulk
675
 
540
687
179
348
199
401
Khan
400
540
 
107
752
521
385
280
Thor
166
687
107
 
111
540
990
361
Captain América
809
179
752
111
 
206
412
576
Ant-Man
720
348
521
540
206
 
155
621
Nick Fury
399
199
385
990
412
155
 
100
The Winter Soldier
233
401
280
361
576
621
100
 
 
 Pregunta 5 (2 puntos)
 
Dado un grafo no dirigido con personajes del MCU de la siguiente tabla:
 
 
Iron Man
The increíble Hulk
Khan
Thor
Captain América
Ant-Man
Nick Fury
The Winter Soldier
Iron Man
 
6
0
1
8
7
3
2
The increíble Hulk
6
 
0
6
1
8
9
1
Khan
0
0
 
1
2
1
5
0
Thor
1
6
1
 
1
5
9
3
Captain América
8
1
2
1
 
2
4
5
Ant-Man
7
8
1
5
2
 
1
6
Nick Fury
3
9
5
9
4
1
 
1
The Winter Soldier
2
1
0
3
5
6
1
 
 
Implementar los algoritmos necesarios para resolver las siguientes tareas:
 
cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
 
hallar el árbol de expansión máximo desde el vértice que contiene a Iron-Man, Thor y The Winter Soldier;
 
determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número
 
cargue todos los personajes de la tabla anterior
 
indicar qué personajes aparecieron en nueve episodios de la saga.
 
 Pregunta 6 (2 puntos)
Crea el siguiente módulo:
El módulo se denominará operaciones.py y contendrá 4 funciones para realizar una suma, una resta, un producto y una division entres dos números. Todas ellas devolverán el resultado.
En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:
TypeError: En caso de que se envíen valores a las funciones que no sean números. Además deberá aparecer un mensaje que informe Error: Tipo de dato no válido.
ZeroDivisionError: En caso de realizar una división por cero. Además deberá aparecer un mensaje que informe Error: No es posible dividir entre cero.
Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás importar el módulo y realizar las siguientes instrucciones. Observa si el comportamiento es el esperado:
from operaciones import *
 
a, b, c, d = (10, 5, 0, "Hola")
 
print( "{} + {} = {}".format(a, b, suma(a, b) ) )
print( "{} - {} = {}".format(b, d, resta(b, d) ) )
print( "{} * {} = {}".format(b, b, producto(b, b) ) )
print( "{} / {} = {}".format(a, c, division(a, c) ) )

 Pregunta 7 (2 puntos)
Crea un script llamado generador.py que cumpla las siguientes necesidades:
Debe incluir una función llamada leer_numero(). Esta función tomará 3 valores: ini, fin y mensaje. El objetivo es leer por pantalla un número >= que ini y <= que fin. Además a la hora de hacer la lectura se mostrará en el input el mensaje enviado a la función. Finalmente se devolverá el valor. Esta función tiene que devolver un número, y tiene que repetirse hasta que el usuario no lo escriba bien (lo que incluye cualquier valor que no sea un número del ini al fin).
Una vez la tengas creada, deberás crear una nueva función llamada generador, no recibirá ningún parámetro. Dentro leerás dos números con la función leer_numero():
El primer numero será llamado numeros, deberá ser entre 1 y 20, ambos incluidos, y se mostrará el mensaje ¿Cuantos números quieres generar? [1-20]:
El segundo número será llamado modo y requerirá un número entre 1 y 3, ambos incluidos. El mensaje que mostrará será: ¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal:.
Una vez sepas los números a generar y cómo redondearlos, tendrás que realizar lo siguiente:
Generarás una lista de números aleatorios decimales entre 0 y 100 con tantos números como el usuario haya indicado.
A cada uno de esos números deberás redondearlos en función de lo que el usuario ha especificado en el modo.
Para cada número muestra durante el redondeo, el número normal y después del redondeo.
Finalmente devolverás la lista de números redondeados.
El objetivo de este ejercicio es  la reutilización de código y los módulos random y math.

 Pregunta 8 (2 puntos)
Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea- toria– que resuelva las siguientes actividades:
 
realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
 determinar si un número está cargado en el árbol o no;
 eliminar tres valores del árbol;
 determinar la altura del subárbol izquierdo y del subárbol derecho;
 determinar la cantidad de ocurrencias de un elemento en el árbol;
 contar cuántos números pares e impares hay en el árbol.
 Pregunta 9 (2 puntos)
Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de cartas de baraja española–,resolver las siguientes actividades:
 generar las cartas del mazo de forma aleatoria;
 separar la pila mazo en cuatro pilas una por cada palo;
 ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.
