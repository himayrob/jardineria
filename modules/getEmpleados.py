#Ya no funciona, por lo que ahora usamos el import request <-----import storage.empleado as em
from tabulate import tabulate
import json
import requests
# Devuelve un listado con el nombre, apellidos y email 
# de los empleados cuyo jefe tiene un código de jefe igual a 7.


#definimos el servidor de getEmpleados
def getAllDataDeEmpleados():
    peticion = requests.get("http://")
    data = peticion.json()
    return data

def getAllNombreApellidoEmailJefe(codigo):#filtro 3
    nombreApellidoEmail = []
    for val in getAllDataDeEmpleados()::
        if(val.get("codigo_jefe") == codigo):
            nombreApellidoEmail.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                }
            )
    return getAllNombreApellidoEmailJefe

def getPuestoNameApellidosEmail(Director_General):
    PuestoNameApellidosEmail = []
    for val in getAllDataDeEmpleados()::
        if(val.get("codigo_Director General") == Director_General):
             PuestoNameApellidosEmail.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                })
    return getPuestoNameApellidosEmail 

# def menu():

print(getPuestoNameApellidosEmail)  



# import storage.empleado as em
# Devuelve un listado con el nombre, apellidos y email 
# de los empleados cuyo jefe tiene un código de jefe igual a 7.

# def getAllNombreApellidoEmailJefe(codigo):
#     nombreApellidoEmail = []
#     for val in getAllDataDeEmpleados()::
#         if(val.get("codigo_jefe") == codigo):
#             nombreApellidoEmail.append(
#                 {
#                     "nombre": val.get("nombre"),
#                     "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
#                     "email": val.get("email"),
#                     "jefe": val.get("codigo_jefe")
#                 }
#             )
#     return nombreApellidoEmail
