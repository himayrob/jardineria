from tabulate import tabulate
import requests

# Definimos el servidor de getEmpleados
def getAllDataDeEmpleados():
    peticion = requests.get("http://172.16.103.18:5002")
    data = peticion.json()
    return data

def getAllNombreApellidoEmailJefe(codigoJefe):
    nombreApellidoEmail = []
    for val in getAllDataDeEmpleados():
        if codigoJefe == val.get('codigo_jefe'):
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
        if val.get('codigo_Director General') == Director_General:
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

            1. Código de jefe
            2. Director general

      """)  

        opcion = int(input("\nSeleccione una de las opciones: "))
        if opcion == 1:
            codigoJefe = int(input("Ingrese código de empleado: "))
            print(tabulate(getAllNombreApellidoEmailJefe(codigoJefe), headers="keys", tablefmt="github"))
        elif opcion == 2:
            Director_General = int(input("Ingrese código de Director General: "))
            print(tabulate(getPuestoNameApellidosEmail(Director_General), headers="keys", tablefmt="github"))

menu()
