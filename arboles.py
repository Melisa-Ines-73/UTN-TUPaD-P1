
#Representa cada libro como un nodo con 4 atributos: 
#titulo, autor, anio y editorial
#Inicializa referencias izquierda y 
#derecha para conectar nodos.
class Nodo:
    def __init__(self, titulo, autor, anio, editorial):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.editorial = editorial
        self.izquierda = None
        self.derecha = None


class BibliotecaC: #define la estructura del árbol.
    def __init__(self): #crea una nueva instancia del árbol
        self.raiz = None #nodo inicial vacío

    def insertar(self, titulo, autor, anio, editorial): # Insertar un nuevo libro con los parametros indicados
        titulo = titulo.strip().lower()
        nuevo_nodo = Nodo(titulo, autor, anio, editorial) # Se crea una nueva instancia de Nodo, 
                                                            #que representa el libro dentro del árbol
        if self.raiz is None:                               
            self.raiz = nuevo_nodo #Si el árbol está vacío, el libro se convierte en la raíz del árbol.
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo) #Si el árbol ya tiene libros, se usa  para encontrar 
                                                            #la posición   correcta en el árbol.

#Compara el título del nuevo libro con el nodo actual.
#Si es menor, lo coloca a la izquierda; si es mayor, a la derecha.
    def _insertar_recursivo(self, nodo, nuevo_nodo):
        if nuevo_nodo.titulo < nodo.titulo:
            if nodo.izquierda is None:
                nodo.izquierda = nuevo_nodo
            else:
                self._insertar_recursivo(nodo.izquierda, nuevo_nodo) #recursión para seguir bajando en el árbol
        else:
            if nodo.derecha is None:
                nodo.derecha = nuevo_nodo
            else:
                self._insertar_recursivo(nodo.derecha, nuevo_nodo) #recursión para seguir bajando en el árbol


     #Busca un libro por su título dentro del árbol.
    def buscar(self, titulo):
        return self._buscar_recursivo(self.raiz, titulo)

    def _buscar_recursivo(self, nodo, titulo): #Comparando el título del libro con el nodo actual
        if nodo is None:        #Si nodo es None, el título no se encontro y no esta en la biblioteca
            return None
            
        if nodo.titulo == titulo:
            return nodo
        elif titulo < nodo.titulo:
            return self._buscar_recursivo(nodo.izquierda, titulo) # Si el título buscado es menor se continúa   
                                                                   #en el subárbol izquierdo     
        else:                                                        
            return self._buscar_recursivo(nodo.derecha, titulo) #Si el título buscado es mayor continúa 
                                                                #en el subárbol derecho
    
#Recorre  en orden -inorden-
    def _inorden(self, nodo): 
        if nodo:
            self._inorden(nodo.izquierda)
            print(f"Título: {nodo.titulo}, Autor: {nodo.autor}, Año: {nodo.anio}, Editorial: {nodo.editorial}")
            self._inorden(nodo.derecha)

    


#Se insertan los datos de los libros. 

biblioteca = BibliotecaC()
biblioteca.insertar("La metamorfosis", "Franz Kafka", 1996, "Losada")
biblioteca.insertar("Un elefante ocupa mucho espacio", "Elsa Bornemann", 2004, "Alfaguara")
biblioteca.insertar("El eternauta", "Héctor Germán Oesterheld", 2023, "Planeta")
biblioteca.insertar("Hamlet", "William Shakespeare", 1969, "Salvat")



# Buscar un libro ingresado por el usuario
titulo_buscar = input ("Ingrese el título del libro").strip().lower() #Elimina espacios y convertir a minúsculas
resultado = biblioteca.buscar(titulo_buscar) # para realizar la búsqueda
if resultado and resultado.titulo.lower().strip () == titulo_buscar:
    print(f"\nLibro encontrado: {resultado.titulo}, Autor: {resultado.autor}, Año: {resultado.anio}, Editorial: {resultado.editorial}")
else:
    print("\nLibro no encontrado")





 






