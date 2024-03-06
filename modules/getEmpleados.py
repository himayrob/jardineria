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