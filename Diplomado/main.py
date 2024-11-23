from persona import Persona
from datetime import date
from Casa import Casa

#Codigo de prueba
casaStark = Casa("Stark", "Winterfel")
persona = Persona("Jon","Snow",date(1978,12,31),casa=casaStark)
persona.alias = "Lord Snow"
print(persona)
print(persona.primerNombre)
print(persona.apellidoPaterno)
print(persona.alias)
print(persona.getNombreCompleto())
print(persona.get_edad())

casaLanni = Casa("Lannistrasse","Buenderburg")
cerseiLanniSterPersona = Persona("Cersei", "Lannister", date(1988,5,31), "The Queen", casa=casaLanni)

print(cerseiLanniSterPersona)
print(cerseiLanniSterPersona.primerNombre)
print(cerseiLanniSterPersona.apellidoPaterno)
print(cerseiLanniSterPersona.alias)
print(cerseiLanniSterPersona.getNombreCompleto())
print(cerseiLanniSterPersona.get_edad())