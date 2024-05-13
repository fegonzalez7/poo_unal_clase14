# Programación Orientada a Objetos - UNAL

## Clase 14: Built-ins - funciones - iteradores

## Built-ins
Son las funciones incorporadas que están disponibles sin necesidad de importar ningún módulo adicional. Estas funciones realizan tareas comunes o cálculos en ciertos tipos de objetos sin ser métodos de una clase subyacente.

Las principales características de los builtins en Python son:

- **Funciones integradas**: Son funciones predefinidas y listas para usar sin necesidad de importar ningún módulo adicional.
- **Operaciones genéricas**: Estas funciones pueden operar en diferentes tipos de objetos que cumplan con ciertos requisitos, como tener determinados atributos o métodos.
- **Métodos especiales:** Algunos builtins son métodos especiales tipo *dunder* (`__`). Estos métodos especiales pueden ser sobrescritos en las clases definidas por el usuario para personalizar el comportamiento de ciertas operaciones.

Algunos ejemplos de builtins comunes en Python son:

- `len()`: Devuelve la longitud de un objeto iterable (listas, cadenas, conjuntos, etc.).
- `sum()`: Calcula la suma de los elementos de un iterable.
- `range()`: Genera una secuencia de números dentro de un rango específico.
- `isinstance()`: Verifica si un objeto es una instancia de una clase o tipo específico.
- `print()`: Imprime uno o más objetos en la salida estándar.
- `input()`: Solicita al usuario que ingrese una entrada desde el teclado.
- `open()`: Abre un archivo y devuelve un objeto de archivo para su posterior manipulación.

### len
Por defecto `len()` entrega la cantidad de objetos que tiene una colección. Sin embargo, `__len__` es un método ue se utiliza para definir el comportamiento de la función incorporada `len()` en objetos personalizados. Este método se invoca automáticamente cuando se llama a la función `len()` sobre un objeto de una clase definida.

- Es un método especial del tipo `__dunder__` que se define dentro de una clase.
- No se llama directamente, sino que es invocado internamente por la función len() cuando se aplica a un objeto de esa clase.
- Debe devolver un entero que representa la longitud o el número de elementos del objeto.
- Si no se define `__len__`en una clase, la función `len()` lanzará un error TypeError cuando se intente utilizarla con objetos de esa clase.

```python 
class MiLista:
  def __init__(self, elementos):
    self.elementos = elementos

  def __len__(self):
    return len(self.elementos)

mi_lista = MiLista([1, 2, 3, 4, 5])
print(f"La cantidad de elementos es: {len(mi_lista)}") 

```
### str
La función `__str__` es un método especial define cómo se representa un objeto como cadena de texto (representación legible del objeto). Es decir, determina la forma en que un objeto se imprime cuando se utiliza la función str() o cuando se inserta directamente en una cadena (e.g. cuando se le da `print()` a un objeto).

 - La función `__str__` está disponible para casi todos los objetos en Python. Si un objeto no define su propia implementación de `__str__`, se utiliza una implementación predeterminada que generalmente muestra la dirección de memoria del objeto.
 - Devuelve una cadena de texto que representa el objeto.

```python 
class MiLista:
  def __init__(self, elementos):
    self.elementos = elementos

  def __len__(self):
    return len(self.elementos)

  def __str__(self):
    return str(self.elementos)

mi_lista = MiLista([1, 2, 3, 4, 5])
print(f"La cantidad de elementos es: {len(mi_lista)}") 
print(mi_lista) 
```

### with 
La sentencia `with` permite "encapsular" el uso de un recurso dentro de un bloque de código, garantizando que el recurso se abra, se use y se cierre correctamente, incluso en caso de errores o excepciones.

- Se utiliza para gestionar recursos como archivos, bases de datos, conexiones de red y cualquier otro objeto que requiera apertura, uso y cierre explícitos.
- Garantiza que el recurso se cierre automáticamente al finalizar el bloque `with`, incluso si se produce una excepción.

```python 
# Abrir un archivo - forma tradicional
try:
  archivo = open("archivo.txt", "r")
  contenido = archivo.read()
  print(contenido)
finally:
  archivo.close()
except FileNotFoundError:
  print("Error: El archivo no se encuentra.")
except Exception as e:
  print(f"Error inesperado: {e}") 
```

```python 
# Abrir un archivo - con with
try:
  with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
  print("Error: El archivo no se encuentra.")
except Exception as e:
  print(f"Error inesperado: {e}")
```

### enumerate
Es una sentencia que permite iterar sobre una secuencia de elementos y obtener, simultáneamente, el índice y el valor de cada elemento en cada iteración. Esta función simplifica el proceso de recorrer una secuencia y acceder a sus elementos de manera indexada.

- La función enumerate recibe una secuencia como argumento, la cual puede ser una lista, un tupla, una cadena u otro tipo de iterable.
- Devuelve un objeto iterador que genera tuplas compuestas por dos elementos: el índice (entero) y el valor (elemento de la secuencia) en cada iteración.
- La posición actual del iterador se actualiza automáticamente con cada iteración, permitiendo recorrer toda la secuencia.
- Se utiliza comúnmente dentro de un bucle for para acceder a ambos, el índice y el valor, en cada iteración.

```python 
nombres = ["Juan", "María", "Pedro", "Ana"]

# forma anti-pro
i: int = 0
for nombre in nombres
  print(f"Índice: {i}, Nombre: {nombre}")
  i += 1

# forma pro
for indice, nombre in enumerate(nombres):
    print(f"Índice: {indice}, Nombre: {nombre}")
```

### zip
Es una sentencia integrada que combina elementos de dos o más secuencias iterables en una nueva secuencia de tuplas. Cada tupla en la nueva secuencia contiene elementos correspondientes de las secuencias originales, enlazados por su posición.

- La función `zip` recibe como argumentos dos o más secuencias iterables, las cuales pueden ser listas, tuplas, cadenas u otros tipos de iterables.
- Devuelve un nuevo objeto iterador que genera tuplas compuestas por elementos correspondientes de las secuencias originales.
- La cantidad de elemntos de la secuencia resultante es igual a la longitud mínima de las secuencias de entrada. Si una secuencia es más corta que las demás, se omiten los elementos faltantes en las tuplas de la secuencia resultante.
- Se utiliza comúnmente dentro de un bucle for para recorrer las secuencias combinadas y acceder a los elementos correspondientes en cada iteración.

```python 
nombres = ["Juan", "María", "Pedro", "Ana"]
edades = [30, 25, 28, 22]

# Combinar usando zip y recorrer en un bucle for
datos_combinados = zip(nombres, edades)

for nombre, edad in datos_combinados:
  print(f"Nombre: {nombre}, Edad: {edad}")
```

### map
Es una sentencia que permite aplicar una operación específica a cada elemento de una secuencia de datos iterable (listas, tuplas o cadenas de caracteres). 

- Permite transformar los elementos de una secuencia a través de la aplicación de una función.
- La función `map` genera un nuevo iterable que contiene los resultados de aplicar la función a cada elemento de la secuencia original.
- La función `map` no retorna los resultados de forma inmediata, sino que devuelve un objeto map que representa la transformación a realizar. Para obtener los resultados procesados, es necesario convertir el objeto `map` a una lista utilizando la función `list`.

```python 
def elevar_al_cuadrado(numero):
  return numero * numero

# Lista de números
numeros = [1, 2, 3, 4, 5]

# funcion como argumento
numeros_al_cuadrado = map(elevar_al_cuadrado, numeros)

# Conversión del objeto `map` a lista
resultado = list(numeros_al_cuadrado)

print(f"Lista original: {numeros}")
print(f"Lista al cuadrado: {resultado}")
```

## Funciones como objetos
En Python, las funciones son objetos de primera clase, lo que significa que pueden ser tratadas como cualquier otro objeto, con la capacidad de asignarles atributos, pasarlas como argumentos a otras funciones y almacenarlas en variables.

- Las funciones en Python se pueden asignar a variables.
```python 
cuadrado_lambda = lambda numero: numero * numero
resultado_funcion_lambda = cuadrado_lambda(5)
print(f"Resultado función lambda: {resultado_funcion_lambda}")
```

- Se pueden pasar como argumentos a otras funciones.
```python 
def sumar(a, b):
  return a + b

def multiplicar(a, b):
  return a * b

def aplicar_operacion(operacion, a, b):
  resultado = operacion(a, b)
  ## __name__ guarda el nombre de la funcion como string
  print(f"Resultado de aplicar {operacion.__name__}: {resultado}")

# Uso de la función 'aplicar_operacion'
aplicar_operacion(sumar, 5, 3)
aplicar_operacion(multiplicar, 5, 3)
```

- Se pueden devolver como resultado de otras funciones.
```python 
# concepto basico de closure
def crear_funcion_sumador(numero_base):
  # funcion_sumador es capaz de recordar el valor de numero_base
  def funcion_sumador(numero):
    return numero_base + numero
  # retorna la funcion_sumador (con el valor de numero_base guardado)
  return funcion_sumador

sumador_cinco = crear_funcion_sumador(5)
print(sumador_cinco)
resultado_sumador_cinco = sumador_cinco(3)

print(f"Resultado sumador 5: {resultado_sumador_cinco}")
```

- Se pueden almacenar en listas, tuplas y diccionarios.
```python 
def sumar(a, b):
  return a + b

def restar(a, b):
  return a - b

def multiplicar(a, b):
  return a * b

funciones = [sumar, restar, multiplicar]
resultado_suma = funciones[0](5, 3)  # resultado_suma = 8
print(f"Resultado suma: {resultado_suma}")

operaciones = (sumar, restar, multiplicar)
resultado_resta = operaciones[1](5, 3)  # resultado_resta = 2
print(f"Resultado resta: {resultado_resta}")

operadores = {
  "+": sumar,
  "-": restar,
  "*": multiplicar
}
resultado_multiplicacion = operadores["*"](5, 3)  # resultado_multiplicacion = 15
print(f"Resultado multiplicación: {resultado_multiplicacion}")
```
- Se pueden tener atributos asociados a ellas (aunque no es un uso común).
```python 
def sumar(a, b):
  """Función que suma dos números."""
  return a + b

# Asociar un atributo a la función
sumar.autor = "Juan Pérez"

# Acceder al atributo
print(f"Autor de la función sumar: {sumar.autor}")

# Ejemplo de uso de la función
resultado_suma = sumar(5, 3)
print(f"Resultado suma: {resultado_suma}")
```

## Introducción a los patrones de diseño
El objeto principal de la ingeniería es resolver problemas, cuando se identifican problemas con una estructura común, es posible plantear una metodlogía para resolver el problema en cuestión. Cuando se diseña un componente mecánico, como un eje, existe una series de pasos en los que se aplican ciertos criterios para llegar a la solución. Esto aplica a casi todas las rams de la ingeniería, para construir una estrucutra civil, para obtener un producto alimenticio, para obtener un circuito que procese una señal. La ingeniería de software NO es la excepción, existen problemas recurrentes, y a partir de ello se han planteado soluciones reutilizables que ofrecen una especie de plantilla para resolver el problema de forma efectiva. 

En general, un patrón de diseño propone un conjunto de objetos que interactuan de cierta manera para resolver un problema determinado. El trabajo de un programador es identificar el patrón de diseño adecuado para resolver el problema al que se enfrenta. 

Existen múltiples patrones de disseño, algunos se abordarán en este curso, sin embargo se deja a discresión de los que vean este material ampliar el tema (*btw:* Un programador *noob* es solo funciones, uno medio malo usa POO, pero uno muy pro aplica patrones de diseño ). 

### Iteradores
Un problema común entre colecciones es cómo ir accediendo a sus elementos de forma secuencial, sin tener que estar haciendo un llamado a toda la estructura que almacena los datos. Para ello se tiene el patrón de *iterador*, el cual es un objeto con dos métodos `next()` y `done()`. El primero le permite acceder al siguiente elemento de la colección y el segundo retorna True cuando no hay más elementos.

```python
# programaticamente sería algo así
while not iterator.done():
  item = iterator.next()
  # hacer algo
```

Un iterable es un objeto al cual se puede acceder a sus elementos de forma secuencial a través de un bucle (en Python, tradicionalmente un *for*). Los iterables deben implementar el método `__iter__`, el cual debe retorna un iterador, el cual actua como una especie de cursor en la secuencia de elementos del iterable.

En Python existen colecciones *built-in* que permiten iterar para acceder a sus elemenos, tales como: listas, tuplas, conjuntos y diccionarios.

```python
class GeneradorPares:
  """Implementa un iterador de números pares hasta un límite especificado."""
  def __init__(self, limite):
    self.limite = limite
    self.numero = 2

  # __iter__ debe retornar la instancia de un Iterador, dado que un iterador ya está iterando sobre sus propios elementos, normalmente se retorna a sí mismo
  def __iter__(self):
    return self

  # Permite definir el siguiente elemnto de la secuencia
  def __next__(self):
    if self.numero <= self.limite:
      valor = self.numero
      self.numero += 2
      return valor
    # en general no se implementa done(), pero se maneja la excepcion StopIteration  
    else:
      raise StopIteration

# Ejemplo de uso
limite = 10
for numero in GeneradorPares(limite):
  print(numero)
```

```python
class CapitalIterable:
  # Retorna un iterable con un iterador tipo CapitalIterator
  def __init__(self, string):
    self.string = string

  def __iter__(self):
    return CapitalIterator(self.string)


class CapitalIterator:
  def __init__(self, string):
    # Lista de palabras a capitalizar
    self.words = [w.capitalize() for w in string.split()]
    self.index = 0

  def __next__(self):
    # Se define como debe ser el siguiente elemento
    if self.index == len(self.words):
      raise StopIteration()
    word = self.words[self.index]
    self.index += 1
    return word

  def __iter__(self):
    return self


iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')
iterator = iter(iterable)
# Aplicacion de la logica de un iterador
while True:
  try:
    print(next(iterator))
  except StopIteration:
    break

# De forma simplificada
for i in iterable:
  print(i)
```

**Ejemplo:** Sistema para registrar eventos.
```python
class RegistroEventos:
  """Implementa un iterable para registrar y recorrer eventos."""

  def __init__(self):
    self.eventos = []

  def agregar_evento(self, tipo, mensaje, timestamp):
    """Agrega un nuevo evento al registro."""
    self.eventos.append((tipo, mensaje, timestamp))

  def __iter__(self):
    return RegistroEventosIterador(self.eventos)

class RegistroEventosIterador:
  """Implementa un iterador para recorrer eventos registrados."""

  def __init__(self, eventos):
    self.eventos = eventos
    self.indice = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.indice < len(self.eventos):
      evento = self.eventos[self.indice]
      self.indice += 1
      return evento
    else:
      raise StopIteration

registro = RegistroEventos()
registro.agregar_evento("INFO", "Aplicación iniciada", 1654321000)
registro.agregar_evento("AVISO", "Memoria baja", 1654321050)
registro.agregar_evento("ERROR", "Fallo en la conexión a la base de datos", 1654321100)

for evento in registro:
  tipo, mensaje, timestamp = evento
  print(f"[{timestamp}] {tipo}: {mensaje}")
```

## Reto 7: 
1. The menu once again....(I am running out of ideas). Well the task is quite easy, take the Menu code from Reto 3 and implement a new Class that creates and iterable with all the items in an order, it should allow looping and contain all item attributes.

