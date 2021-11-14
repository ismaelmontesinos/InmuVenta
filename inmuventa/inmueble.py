from dataclasses import dataclass
from datetime import datetime

@dataclass
class Localizacion:
    """ Clase para representar el tipo localización """
    provincia: str 
    ciudad: str
    codigo_postal: int
    tipo_via: str
    nombre_via: str
    bloque: int 
    planta: int 
    numero_puerta: int
    puerta: str 

    def __init__(self, provincia, ciudad, codigo_postal, tipo_via, nombre_via, numero_bloque = None, planta = None, numero_puerta = None, puerta = None):
        self.provincia = provincia
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal
        self.tipo_via = tipo_via
        self.nombre_via = nombre_via
        self.bloque = numero_bloque
        self.planta = planta
        self.numero_puerta = numero_puerta
        self.puerta = puerta

@dataclass
class Inmueble:
    """ Clase que representa un inmueble"""
    id: str
    localizacion: Localizacion 
    precio: float
    descripcion: str
    num_dormitorios: int
    num_baños: int
    ultima_reforma: datetime
    metros_cuadrados: float
    garaje: bool
