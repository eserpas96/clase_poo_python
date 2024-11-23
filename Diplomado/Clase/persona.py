from datetime import date
from Casa import Casa

class Persona:
    def __init__(self, primerNombre, apellidoPaterno, fecha_nacimiento: date, alias="", casa = None):
        self.primerNombre = primerNombre
        self.apellidoPaterno = apellidoPaterno
        self.alias = alias
        self.__fecha_nacimiento = fecha_nacimiento
        self.casa = casa

    def getNombreCompleto(self):
        return self.primerNombre + " " + self.apellidoPaterno + " aka " + self.alias
    
    def get_edad(self):
        hoy = date.today()
        return (hoy.year - self.__fecha_nacimiento.year
                - ((hoy.month, hoy.day)< (self.__fecha_nacimiento.month,
                                          self.__fecha_nacimiento.day))
                )

    def __repr__(self):
        return (f"Primer Nombre: {self.primerNombre}," 
                + f"Apellido Paterno {self.apellidoPaterno}"
                + f"Fecha de Nacimiento {self.__fecha_nacimiento}"
                + f"Casa: {self.casa}")