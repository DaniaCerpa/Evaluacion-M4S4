#Se crea clase padre (superclase) Persona 
class Persona:
    """
    Clase Padre que representa a una persona.
    Sus atributos seran nombre y velocidad. Se establece una velocidad de 12 km/hr por defecto.
    Su metodo sera movimiento() y calcula la velocidad promedio a la que se mueve la persona.
    """
    
    def __init__(self, nombre:str)-> None:
        self.nombre = nombre
        self.velocidad = 12
        
        
    def movimiento(self):
        return f"Una persona promedio se mueve a {self.velocidad} km por hora"

class Maratonista (Persona):
    """
    Clase hija (subclase) de la clase Persona. Representa a un Maratonista.
    Su atributos seran nombre y factor_maratonista. Se establece factor fijo de 1.5 por defecto.
    Su metodo sera movimiento() y calcula la velocidad promedio a la que se mueve el maratonista.
    """
    
    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        self.factor_maratonista = 1.5
        
    def movimiento(self):
        velocidad = self.velocidad* self.factor_maratonista
        return f"Un Maratonista promedio se mueve a {velocidad} km por hora"
    
class Ciclista (Persona):
    """
    Clase hija (subclase) de la clase Persona. Representa a un Ciclista.
    Su atributos seran nombre y factor_ciclista. Se establece factor fijo de 1.2 por defecto.
    Su metodo sera movimiento() y calcula la velocidad promedio a la que se mueve el ciclista.
    """
    def __init__(self, nombre:str) -> None:
        super().__init__(nombre)
        self.factor_ciclista = 1.2        

        
    def movimiento(self):
        velocidad = self.velocidad* self.factor_ciclista
        return f"Un Ciclista promedio se mueve a {velocidad} km por hora"


#Se crean instancias de clases y se imprimen sus respectivos metodos movimiento().
juanito = Persona("Juan")
print (juanito.movimiento())    
    
pepito = Maratonista("Pepito")
print(pepito.movimiento())

clarita = Ciclista("Clara")
print(clarita.movimiento())
