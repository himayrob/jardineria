# Ya no funciona, por lo que ahora usamos el import request <-----import storage.empleado as em
from tabulate import tabulate
import json
import requests
# Devuelve un listado con el nombre, apellidos y email
# de los empleados cuyo jefe tiene un código de jefe igual a 7.


# definimos el servidor de getEmpleados
def getAllDataDeEmpleados():
    peticion = requests.get("http://172.16.103.18:5002")
    data = peticion.json()
    return data


def getAllNombreApellidoEmailJefe(codigoJefe):  # filtro 3
    nombreApellidoEmail = []
    for val in getAllDataDeEmpleados():
        if (codigoJefe == val.get('codigo_jefe')):
            nombreApellidoEmail.append(
                {
                    "nombre": val.get('nombre'),
                    "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                    "email": val.get('email'),
                    "jefe": val.get('codigo_jefe')
                }
            )
    return nombreApellidoEmail


def getPuestoNameApellidosEmail(Director_General):
    PuestoNameApellidosEmail = []
    for val in getAllDataDeEmpleados():
        if (val.get('codigo_Director General') == Director_General):
            PuestoNameApellidosEmail.append(
                {
                    "nombre": val.get('nombre'),
                    "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                    "email": val.get('email'),
                    "jefe": val.get('codigo_jefe')
                })
    return PuestoNameApellidosEmail


def menu():
    while True:

        print("""
                    
█████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██╗███████╗████████╗██████╗  █████╗ ██████╗
██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
███████║██║  ██║██╔████╔██║██║██╔██╗ ██║██║███████╗   ██║   ██████╔╝███████║██████╔╝
██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║██║╚════██║   ██║   ██╔══██╗██╔══██║██╔══██╗
██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██║███████║   ██║   ██║  ██║██║  ██║██║  ██║
╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

██████╗  █████╗ ████████╗ ██████╗ ███████╗    ██████╗ ███████╗██╗
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔══██╗██╔════╝██║
██║  ██║███████║   ██║   ██║   ██║███████╗    ██║  ██║█████╗  ██║
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██║  ██║██╔══╝  ██║
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ██████╔╝███████╗███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═════╝ ╚══════╝╚══════╝

██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗ ██████╗
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔═══██╗
██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║
██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║
██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   ╚██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝

            1.codigo de jefe
            2.director general



      """)

        opcion = int(input("\nSelecione una de las opciones:"))
        if (opcion == 1):
            codigoJefe = int(input("ingrese codigo de empleado"))
            print(tabulate(getAllNombreApellidoEmailJefe(codigoJefe), headers="keys", tablefmt="github"))
        elif (opcion == 2):
            Director_General = int(input("Ingrese código de Director General: "))
            #print(tabulate(getPuestoNameApellidosEmail(Director_General), headers="keys", tablefmt="github"))
        break
