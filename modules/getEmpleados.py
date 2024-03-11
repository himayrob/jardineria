from tabulate import tabulate
import storage.empleado as em


def getnombreApellidosEmailEmpleados(codigo):
    nombreApellidosEmailempleados =[]
    for val in em.empleados:
        if (val.get("puesto") != "Representante Ventas" ):
            nombreApellidosEmailempleados.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": F'{val.get("apellido1")}{val.get("apellido2")}',
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe"),
                    "puesto": val.get("puesto")
                }
            )
    return nombreApellidosEmailempleados

def getAllCodigoPuestoNombreApellidos(nombre):
    PuestoNombreApellidos = []
    for val in em.empleados:
        if(val.get("nombre") == nombre):
            PuestoNombreApellidos.append(
                {
                    "Puesto": val.get("puesto"),
                    "Nombre": val.get("nombre"),
                    "Apellidos": f'{val.get("apellido1")}{val.get("apellido2")}',
                    "Email": val.get("email")
                }
            )
    return PuestoNombreApellidos

def getAllNombreApellidoNombresPuesto():
    NombreApellidoPuesto = []
    for val in em.empleados:
        if(val.get("puesto") != ("Representante Ventas")):
            NombreApellidoPuesto.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")}{val.get("apellido2")}',
                    "puesto": val.get("puesto")
                }
            )
    return NombreApellidoPuesto
def menu():
    while True:
        print(""" 
                                                                      
 |  _     | | __   | |__        | |  _ | | 
 |   / -| ' /  | '|  / -_(-< / ` / -) / -| '  | ' | / -/  / _ /  (-<
 ||_| ._||  __// _,_| _|||_| .|____,_,_//
         ||                                            |_|

1. Obtener los datos de un jefe con su codigo(codigo_jefe)
2. Obtener los datos de un jefe con su nombre(nombre_jefe)
3. Obtener los jefes que no tienen el titulo de "Representante de Ventas"
4. Regresar al Menu Principal""")
        opcion = int(input("\nIngrese la opcion que desea realizar: "))
        if opcion == 1:
            codigo = int(input("Ingrese el codigo del jefe: "))
            print(tabulate(getnombreApellidosEmailEmpleados(codigo), headers="keys", tablefmt="fancy_grid"))
        elif opcion == 2:
            nombre = int(input("Ingrese el nombre del jefe: "))
            print(tabulate(getAllCodigoPuestoNombreApellidos(nombre), headers="keys", tablefmt="fancy_grid"))
        elif opcion == 3:
            print(tabulate(getAllNombreApellidoNombresPuesto(), headers="keys", tablefmt="fancy_grid"))
        elif opcion == 4:
            break