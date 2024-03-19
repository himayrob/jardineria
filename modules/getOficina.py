import requests
from tabulate import tabulate
import os

def getAllDataDeOficina():
    peticion = requests.get("http://")
    data = peticion.json()
    return data

#import storage.oficina as of
# Devuelve un listado con el código de 
# oficina y la ciudad donde hay oficinas.

def getAllCodigoCiudad():#filtro 1
    codigoCiudad = []
    for val in getAllDataDeOficina():
        codigoCiudad.append({
            "código": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

# Devuelve un listado con la ciudad y el teléfono 
# de las oficinas de España.

def getAllCiudadTelefono(ciudad):#segundo filtro
    ciudadTelefono = []
    for val in getAllCiudadTelefono():
        if(val.get("ciudad") == ciudad):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "teléfono": val.get("telefono"),
                "oficinas": val.get("codigo_oficina"),
                "pais": val.get("pais")
            })
    return ciudadTelefono
